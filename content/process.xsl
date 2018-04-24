<?xml version='1.0'?> <!--*- mode: nxml -*-->
<!DOCTYPE xsl:stylesheet [
  <!ENTITY nbsp "&#160;">
  <!ENTITY nl   "&#10;">
  <!ENTITY copy "&#169;">
  <!ENTITY mdash   "&#8212;">
]>
<xsl:stylesheet xmlns="http://www.w3.org/1999/xhtml"
                xmlns:html="http://www.w3.org/1999/xhtml"
                xmlns:menu="http://www.daa.com.au/~james/menu-ns"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="1.0" exclude-result-prefixes="#default menu">

  <xsl:output method="xml"
    encoding="US-ASCII"
    doctype-public="-//W3C//DTD XHTML 1.0 Transitional//EN"
    doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"
    omit-xml-declaration="yes" />

  <xsl:param name="website.tree">website.xml</xsl:param>
  <xsl:param name="document.url">index.html</xsl:param>
  <xsl:param name="document.modtime"></xsl:param>
  <xsl:param name="document.copyrightyear">2004</xsl:param>

  <xsl:variable name="menu" select="document($website.tree)/menu:page" />

  <!-- some code to convert a simplified uri to a -->
  <xsl:template name="uri.make.relative">
    <xsl:param name="base.uri" select="'foo/baz'" />
    <xsl:param name="uri" select="'foo/bar'" />

    <xsl:choose>
      <xsl:when test="starts-with($uri, 'http:')">
	<xsl:value-of select="$uri" />
      </xsl:when>
      <xsl:when test="contains($base.uri, '/') and contains($uri, '/') and
             substring-before($base.uri, '/')=substring-before($uri, '/')">
        <xsl:call-template name="uri.make.relative">
          <xsl:with-param name="base.uri"
                          select="substring-after($base.uri, '/')" />
          <xsl:with-param name="uri"
                          select="substring-after($uri, '/')" />
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
        <xsl:call-template name="make.dot.dot.slashes">
          <xsl:with-param name="uri" select="$base.uri" />
        </xsl:call-template>
        <xsl:value-of select="$uri" />
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <xsl:template name="make.dot.dot.slashes">
    <xsl:param name="uri" select="'foo/bar'" />

    <xsl:if test="contains($uri, '/')">
      <xsl:text>../</xsl:text>
      <xsl:call-template name="make.dot.dot.slashes">
        <xsl:with-param name="uri" select="substring-after($uri, '/')" />
      </xsl:call-template>
    </xsl:if>
  </xsl:template>

  <!-- handling of main document -->
  <xsl:template match="html:html">
    <html>
      <xsl:copy-of select="@*" />
      <xsl:if test="not(@lang)">
	<xsl:attribute name="lang">
	  <xsl:text>en-AU</xsl:text>
	</xsl:attribute>
      </xsl:if>
      <xsl:if test="not(@xml:lang)">
	<xsl:attribute name="xml:lang">
	  <xsl:text>en-AU</xsl:text>
	</xsl:attribute>
      </xsl:if>
      <xsl:apply-templates />
    </html>
  </xsl:template>

  <xsl:template match="*" mode="output.link.elements">
    <link rel="home" title="{$menu/@label}">
      <xsl:attribute name="href">
	<xsl:call-template name="uri.make.relative">
	  <xsl:with-param name="base.uri" select="$document.url" />
	  <xsl:with-param name="uri" select="$menu/@href" />
	</xsl:call-template>
      </xsl:attribute>
    </link>
    <xsl:text>&nl;</xsl:text>
    <xsl:if test="..">
      <link rel="up" title="{../@label}">
	<xsl:attribute name="href">
	  <xsl:call-template name="uri.make.relative">
	    <xsl:with-param name="base.uri" select="$document.url" />
	    <xsl:with-param name="uri" select="../@href" />
	  </xsl:call-template>
	</xsl:attribute>
      </link>
      <xsl:text>&nl;</xsl:text>
    </xsl:if>
    <xsl:if test="preceding-sibling::*[last()]">
      <link rel="first" title="{preceding-sibling::*[last()]/@label}">
	<xsl:attribute name="href">
	  <xsl:call-template name="uri.make.relative">
	    <xsl:with-param name="base.uri" select="$document.url" />
	    <xsl:with-param name="uri" select="preceding-sibling::*[last()]/@href" />
	  </xsl:call-template>
	</xsl:attribute>
      </link>
      <xsl:text>&nl;</xsl:text>
    </xsl:if>
    <xsl:if test="preceding-sibling::*[1]">
      <link rel="prev" title="{preceding-sibling::*[1]/@label}">
	<xsl:attribute name="href">
	  <xsl:call-template name="uri.make.relative">
	    <xsl:with-param name="base.uri" select="$document.url" />
	    <xsl:with-param name="uri" select="preceding-sibling::*[1]/@href" />
	  </xsl:call-template>
	</xsl:attribute>
      </link>
      <xsl:text>&nl;</xsl:text>
    </xsl:if>
    <xsl:if test="following-sibling::*[1]">
      <link rel="next" title="{following-sibling::*[1]/@label}">
	<xsl:attribute name="href">
	  <xsl:call-template name="uri.make.relative">
	    <xsl:with-param name="base.uri" select="$document.url" />
	    <xsl:with-param name="uri" select="following-sibling::*[1]/@href" />
	  </xsl:call-template>
	</xsl:attribute>
      </link>
      <xsl:text>&nl;</xsl:text>
    </xsl:if>
    <xsl:if test="following-sibling::*[last()]">
      <link rel="last" title="{following-sibling::*[last()]/@label}">
	<xsl:attribute name="href">
	  <xsl:call-template name="uri.make.relative">
	    <xsl:with-param name="base.uri" select="$document.url" />
	    <xsl:with-param name="uri" select="following-sibling::*[last()]/@href" />
	  </xsl:call-template>
	</xsl:attribute>
      </link>
      <xsl:text>&nl;</xsl:text>
    </xsl:if>
  </xsl:template>

  <xsl:template match="html:head">
    <xsl:variable name="menunode" select="$menu//*[@href=$document.url]" />
    <xsl:copy>
      <xsl:apply-templates />
      <xsl:text>&nl;</xsl:text>
      <link rel="stylesheet" title="default" type="text/css">
        <xsl:attribute name="href">
          <xsl:call-template name="uri.make.relative">
            <xsl:with-param name="base.uri" select="$document.url" />
            <xsl:with-param name="uri" select="'style.css'" />
          </xsl:call-template>
        </xsl:attribute>
      </link>
      <xsl:text>&nl;</xsl:text>
      <xsl:if test="$menunode">
        <xsl:apply-templates mode="output.link.elements" select="$menunode" />
      </xsl:if>
    </xsl:copy>
  </xsl:template>

  <xsl:template match="html:body">
    <xsl:copy>
      <xsl:copy-of select="@*" />

      <xsl:apply-templates mode="render.menu.tree" select="$menu" />
      <xsl:text>&nl;</xsl:text>
      <xsl:apply-templates />
      <xsl:text>&nl;</xsl:text>
      <xsl:apply-templates mode="render.bottom.menu" select="$menu" />
      <xsl:text>&nl;</xsl:text>
      <div class="credits">
        <xsl:text>Copyright &copy; </xsl:text>
        <xsl:value-of select="$document.copyrightyear" />
        <xsl:text> &mdash; James Henstridge &lt;</xsl:text>
        <xsl:comment> foo</xsl:comment>
        <xsl:text>james</xsl:text>
        <xsl:comment>bar </xsl:comment>
        <xsl:text disable-output-escaping="yes">&amp;#64;</xsl:text>
        <xsl:comment> baz</xsl:comment>
	<xsl:text>jamesh</xsl:text>
        <xsl:comment>foo</xsl:comment>
        <xsl:text disable-output-escaping="yes">&amp;#x2E;id</xsl:text>
        <xsl:comment>bar</xsl:comment>
        <xsl:text>.au&gt;</xsl:text>
      </div>
    </xsl:copy>
  </xsl:template>

  <xsl:template match="*|comment()">
    <xsl:copy>
      <xsl:copy-of select="@*" />
      <xsl:apply-templates />
    </xsl:copy>
  </xsl:template>

  <xsl:template name="render.menu.link">
    <xsl:choose>
      <xsl:when test="@href = $document.url">
        <b>
          <xsl:value-of select="@label" />
        </b>
      </xsl:when>
      <xsl:otherwise>
        <a>
          <xsl:attribute name="href">
            <xsl:call-template name="uri.make.relative">
              <xsl:with-param name="base.uri" select="$document.url" />
              <xsl:with-param name="uri" select="@href" />
            </xsl:call-template>
          </xsl:attribute>
          <xsl:value-of select="@label" />
        </a>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <xsl:template match="/menu:page" mode="render.menu.tree">
    <div id="menu">
      <xsl:text>&nl;</xsl:text>
      <xsl:call-template name="render.menu.link" select="." />
      <xsl:text>&nl;</xsl:text>
      <ul>
        <xsl:text>&nl;</xsl:text>
        <xsl:apply-templates select="./menu:page[not(@nomenu)]"
                             mode="render.menu.tree" />
      </ul>
      <xsl:text>&nl;</xsl:text>
    </div>
  </xsl:template>

  <xsl:template match="menu:page" mode="render.menu.tree">
    <xsl:variable name="child.pages"
                  select="./menu:page" />
    <li>
      <xsl:call-template name="render.menu.link" select="." />
      <xsl:choose>
        <xsl:when test="@href = $document.url">
          <xsl:if test="$child.pages">
            <xsl:text>&nl;</xsl:text>
            <ul>
	      <xsl:text>&nl;</xsl:text>
              <xsl:apply-templates match="$child.pages"
                                   mode="render.menu.tree" />
            </ul>
          </xsl:if>
        </xsl:when>
        <xsl:otherwise>
          <xsl:if test="$child.pages and .//*[@href=$document.url]">
            <xsl:text>&nl;</xsl:text>
            <ul>
	      <xsl:text>&nl;</xsl:text>
              <xsl:apply-templates match="$child.pages"
                                   mode="render.menu.tree" />
            </ul>
          </xsl:if>
        </xsl:otherwise>
      </xsl:choose>
    </li>
    <xsl:text>&nl;</xsl:text>
  </xsl:template>

  <xsl:template match="*|text()" mode="render.menu.tree" />

  <xsl:template match="/menu:page" mode="render.bottom.menu">
    <div class="bottombar">
      <hr />
      <xsl:text>&nl;</xsl:text>
      <xsl:text>|&nl;</xsl:text>
      <xsl:call-template name="render.menu.link" select="."/>
      <xsl:text> |&nl;</xsl:text>
      <xsl:for-each select="./menu:page">
        <xsl:call-template name="render.menu.link" select="." />
        <xsl:text> |&nl;</xsl:text>
      </xsl:for-each>
    </div>
  </xsl:template>


</xsl:stylesheet>
