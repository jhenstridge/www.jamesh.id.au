#include <stdlib.h>
#include <libxml/parser.h>
#include <libxml/tree.h>
#include <libxml/HTMLparser.h>
#include <libxml/uri.h>

static void
ignore_errors(void *ctx, const char *msg, ...)
{
    /* nothing */
}

xmlNode *
parse_html_fragment(const char *buffer, size_t len, xmlCharEncoding encoding)
{
    /* wrapper for HTML fragment */
    static const char header[] = "<html><head><title></title></head><body>";
    static const char footer[] = "</body></html>";

    htmlParserCtxt *ctx;
    xmlDoc *htmldoc;
    xmlNode *body, *div, *child;
    xmlNs *xhtmlns;

    ctx = htmlCreatePushParserCtxt(NULL, NULL, NULL, 0, "foo", encoding);
    if (!ctx) {
	/* XXXX - could not create parser */
	return NULL;
    }
    xmlSetGenericErrorFunc(ctx, ignore_errors);
    /* do best effort to parse document */
    if (htmlParseChunk(ctx, header, sizeof(header)-1, 0) == 0) {
	if (htmlParseChunk(ctx, buffer, len, 0) == 0) {
	    htmlParseChunk(ctx, footer, sizeof(footer)-1, 1);
	}
    }
    /* get document from buffer */
    htmldoc = ctx->myDoc;
    htmlFreeParserCtxt(ctx);

    /* body is second child of root element */
    body = xmlDocGetRootElement(htmldoc)->children->next;

    div = xmlNewNode(NULL, "div");
    xhtmlns = xmlNewNs(div, "http://www.w3.org/1999/xhtml", NULL);
    xmlSetNs(div, xhtmlns);

    child = body->children;
    while (child) {
	xmlNode *nextchild = child->next;

	xmlUnlinkNode(child);
	xmlAddChild(div, child);
	child = nextchild;
    }
    xmlFreeDoc(htmldoc);

    return div;
}

void
resolve_relative(xmlNode *node, const char *base_uri)
{
    xmlNode *child;

    /* HTML spec mentioned 3 attributes on elements that we might want
     * to update */
    if (xmlHasProp(node, "src")) {
	xmlChar *uri = xmlBuildURI(xmlGetProp(node, "src"), base_uri);
	xmlSetProp(node, "src", uri);
	xmlFree(uri);
    }
    if (xmlHasProp(node, "href")) {
	xmlChar *uri = xmlBuildURI(xmlGetProp(node, "href"), base_uri);
	xmlSetProp(node, "href", uri);
	xmlFree(uri);
    }
    if (xmlHasProp(node, "cite")) {
	xmlChar *uri = xmlBuildURI(xmlGetProp(node, "cite"), base_uri);
	xmlSetProp(node, "cite", uri);
	xmlFree(uri);
    }

    for (child = node->children; child != NULL; child = child->next) {
	if (child->type == XML_ELEMENT_NODE)
	    resolve_relative(child, base_uri);
    }
}

xmlBuffer *
read_file(FILE *fp)
{
    xmlBuffer *ret;
    xmlChar buf[4096];
    size_t count;

    ret = xmlBufferCreate();
    if (!ret) return NULL;
    while ((count = fread(buf, sizeof(xmlChar), sizeof(buf), fp)) != 0) {
	xmlBufferAdd(ret, buf, count);
    }
    return ret;
}

int
main(int argc, char **argv)
{
    xmlBuffer *buf;
    xmlNode *div;
    xmlDoc *doc;

    /* parse stdin as an HTML fragment */
    buf = read_file(stdin);
    div = parse_html_fragment(xmlBufferContent(buf), xmlBufferLength(buf),
			      XML_CHAR_ENCODING_UTF8);

    /* optionally resolve relative URIs */
    if (argc >= 2)
	resolve_relative(div, argv[1]);

    /* embed parsed content into an XML document */
    doc = xmlNewDoc("1.0");
    xmlDocSetRootElement(doc, div);

    /* output */
    xmlDocFormatDump(stdout, doc, 1);

    xmlFreeDoc(doc);
    return 0;
}
