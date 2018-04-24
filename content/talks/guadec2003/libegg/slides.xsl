<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
        xmlns="http://www.w3.org/1999/xhtml"
        xmlns:s="http://www.oscom.org/2003/SlideML/1.0/"
        xmlns:exsl="http://exslt.org/common"
        extension-element-prefixes="exsl"
        exclude-result-prefixes="s exsl">

  <xsl:output method="xml" indent="yes" encoding="US-ASCII"
       doctype-public="-//W3C//DTD XHTML 1.0 Transitional//EN"
       doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"
       omit-xml-declaration="yes" />

  <xsl:param name="lang" select="'en-AU'"/>

  <xsl:param name="file.extension" select="'.html'" />

  <xsl:variable name="nl">
    <xsl:text>
</xsl:text>
  </xsl:variable>

  <xsl:template match="/s:slideset">
    <xsl:call-template name="index"/>

    <xsl:call-template name="title"/>

    <xsl:for-each select="s:slide">
      <xsl:call-template name="htmldoc">
        <xsl:with-param name="filename">
          <xsl:text>slide</xsl:text>
          <xsl:value-of select="position()"/>
	  <xsl:value-of select="$file.extension" />
        </xsl:with-param>
        <xsl:with-param name="content">
          <xsl:call-template name="slide">
            <xsl:with-param name="position" select="position()"/>
          </xsl:call-template>
        </xsl:with-param>
      </xsl:call-template>
    </xsl:for-each>
  </xsl:template>

  <xsl:template name="htmldoc">
    <xsl:param name="filename">foo<xsl:value-of select="$file.extension" /></xsl:param>
    <xsl:param name="content"/>

    <xsl:message>
      <xsl:text>Writing </xsl:text>
      <xsl:value-of select="$filename"/>
      <xsl:text> ...</xsl:text>
    </xsl:message>
    <exsl:document href="{$filename}"
      method="xml"
      indent="yes"
      media-type="application/xhtml+xml"
      doctype-public="-//W3C//DTD XHTML 1.0 Transitional//EN"
      doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"
      standalone="no">
      <xsl:copy-of select="$content"/>
    </exsl:document>
  </xsl:template>

  <xsl:template name="copy.contents">
    <xsl:param name="content"/>
    <xsl:copy-of
    select="$content/*|$content/text()|$content/comment()"/>
  </xsl:template>

  <xsl:template name="index">
    <xsl:call-template name="htmldoc">
      <xsl:with-param name="filename" select="concat('index',$file.extension)"/>
      <xsl:with-param name="content">
        <html lang="{$lang}">
          <xsl:value-of select="$nl"/>
          <head>
            <xsl:value-of select="$nl"/>
            <title>
              <xsl:value-of select="s:metadata/s:title"/>
            </title>
            <xsl:value-of select="$nl"/>
            <script type="text/javascript" src="slides.js"></script>
            <xsl:value-of select="$nl"/>
            <link rel="stylesheet" type="text/css" href="slides.css"/>
            <link rel="stylesheet" type="text/css" href="custom.css"/>
            <xsl:value-of select="$nl"/>
          </head>
          <xsl:value-of select="$nl"/>
          <body>
            <xsl:value-of select="$nl"/>
            <h1>
              <xsl:value-of select="s:metadata/s:title"/>
            </h1>
            <xsl:value-of select="$nl"/>
            <p>
              <a href="title{$file.extension}" onclick="return open_presentation('title{$file.extension}')">
                Open presentation in chromeless window
              </a>
            </p>
            <xsl:value-of select="$nl"/>
            <ol>
              <xsl:value-of select="$nl"/>
              <li>
                <a href="title{$file.extension}">
                  Title Page
                </a>
              </li>
              <xsl:value-of select="$nl"/>
              <xsl:for-each select="s:slide">
                <li>
                  <a href="slide{position()}{$file.extension}">
                    <xsl:value-of select="s:title"/>
                  </a>
                </li>
                <xsl:value-of select="$nl"/>
              </xsl:for-each>
            </ol>
            <xsl:value-of select="$nl"/>
          </body>
          <xsl:value-of select="$nl"/>
        </html>
      </xsl:with-param>
    </xsl:call-template>
  </xsl:template>

  <xsl:template name="title">
    <xsl:call-template name="htmldoc">
      <xsl:with-param name="filename" select="concat('title',$file.extension)"/>
      <xsl:with-param name="content">
        <html lang="{$lang}">
          <xsl:value-of select="$nl"/>
          <head>
            <xsl:value-of select="$nl"/>
            <title>
              <xsl:value-of select="s:metadata/s:title"/>
            </title>
            <xsl:value-of select="$nl"/>
            <link rel="up" title="Index" href="index{$file.extension}" />
            <xsl:value-of select="$nl"/>
            <link rel="next" title="s:slide[0]/s:title" href="slide1{$file.extension}" />
            <xsl:value-of select="$nl"/>
            <link rel="stylesheet" type="text/css" href="slides.css"/>
            <link rel="stylesheet" type="text/css" href="custom.css"/>
            <xsl:value-of select="$nl"/>
            <xsl:call-template name="std.scripts"/>
          </head>
          <xsl:value-of select="$nl"/>
          <body>
            <xsl:value-of select="$nl"/>
            <div id="titlepage">
              <xsl:value-of select="$nl"/>
              <h1>
                <xsl:value-of select="s:metadata/s:title"/>
              </h1>
              <xsl:value-of select="$nl"/>
              <xsl:if test="s:metadata/s:subtitle">
                <p class="subtitle">
                  <xsl:value-of select="s:metadata/s:subtitle"/>
                </p>
                <xsl:value-of select="$nl"/>
              </xsl:if>

              <div class="confgroup">
                <xsl:value-of select="$nl"/>
                <div class="conftitle">
                  <xsl:value-of select="s:metadata/s:confgroup/s:conftitle"/>
                </div>
                <div class="address">
                  <xsl:value-of select="s:metadata/s:confgroup/s:address"/>
                </div>
              </div>

              <div class="authorgroup">
                <xsl:value-of select="$nl"/>
                <xsl:for-each select="s:metadata/s:authorgroup/s:author">
                  <div class="author">
                    <xsl:value-of select="$nl"/>
                    <span class="givenname">
                      <xsl:value-of select="s:givenname"/>
                    </span>
                    <xsl:value-of select="$nl"/>
                    <span class="familyname">
                      <xsl:value-of select="s:familyname"/>
                    </span>
                    <xsl:value-of select="$nl"/>
                    <span class="email">
                      <xsl:text>&lt;</xsl:text>
                      <xsl:value-of select="substring-before(s:email, '@')"/>
                      <xsl:comment> foo </xsl:comment>
                      <xsl:text>@</xsl:text>
                      <xsl:comment> bar </xsl:comment>
                      <xsl:value-of select="substring-after(s:email, '@')"/>
                      <xsl:text>&gt;</xsl:text>
                    </span>
                    <xsl:value-of select="$nl"/>
                  </div>
                  <xsl:value-of select="$nl"/>
                </xsl:for-each>
                <xsl:value-of select="$nl"/>
              </div>

            </div>
            <xsl:value-of select="$nl"/>
            <xsl:if test="s:metadata/s:abstract">
              <div id="notes">
                <xsl:value-of select="$nl"/>
                <xsl:call-template name="copy.contents">
                  <xsl:with-param name="content"
                                  select="s:metadata/s:abstract"/>
                </xsl:call-template>
                <xsl:value-of select="$nl"/>
              </div>
              <xsl:value-of select="$nl"/>
            </xsl:if>
          </body>
          <xsl:value-of select="$nl"/>
        </html>
      </xsl:with-param>
    </xsl:call-template>
  </xsl:template>

  <xsl:template name="slide">
    <xsl:param name="position">42</xsl:param>

    <xsl:variable name="prev" select="preceding-sibling::s:slide"/>
    <xsl:variable name="next" select="following-sibling::s:slide"/>

    <html lang="{$lang}">
      <xsl:value-of select="$nl"/>
      <head>
        <xsl:value-of select="$nl"/>
        <title>
          <xsl:value-of select="s:title"/>
        </title>
        <xsl:value-of select="$nl"/>

        <link rel="up" title="Index" href="index{$file.extension}" />
        <xsl:value-of select="$nl"/>
        <xsl:choose>
          <xsl:when test="$prev">
            <link rel="prev" title="{$prev/s:title}"
                  href="slide{$position - 1}{$file.extension}" />
          </xsl:when>
          <xsl:otherwise>
            <link rel="prev" title="{/s:slideset/s:metadata/s:title}"
                  href="title{$file.extension}"/>
          </xsl:otherwise>
        </xsl:choose>
        <xsl:value-of select="$nl"/>
        <xsl:if test="$next">
          <link rel="next" title="{$next/s:title}"
                href="slide{$position+1}{$file.extension}" />
        </xsl:if>
        <xsl:value-of select="$nl"/>
        <link rel="stylesheet" type="text/css" href="slides.css"/>
        <link rel="stylesheet" type="text/css" href="custom.css"/>
        <xsl:value-of select="$nl"/>
        <xsl:call-template name="std.scripts"/>
      </head>
      <xsl:value-of select="$nl"/>
      <body>
        <xsl:value-of select="$nl"/>
        <div id="content">
          <xsl:value-of select="$nl"/>
          <h1>
            <xsl:value-of select="s:title"/>
          </h1>
          <xsl:value-of select="$nl"/>
          <xsl:call-template name="copy.contents">
            <xsl:with-param name="content" select="s:content"/>
          </xsl:call-template>
          <xsl:value-of select="$nl"/>
        </div>
        <xsl:value-of select="$nl"/>

        <xsl:if test="s:notes">
          <div id="notes">
            <xsl:value-of select="$nl"/>
            <xsl:call-template name="copy.contents">
              <xsl:with-param name="content" select="s:notes"/>
            </xsl:call-template>
            <xsl:value-of select="$nl"/>
          </div>
          <xsl:value-of select="$nl"/>
        </xsl:if>


        <div id="navfooter">
          <xsl:value-of select="$nl"/>
          <span id="slidenumber">
            <xsl:text>Slide </xsl:text>
            <xsl:value-of select="$position"/>
            <xsl:text> / </xsl:text>
            <xsl:value-of select="count(/s:slideset/s:slide)"/>
          </span>
          <xsl:value-of select="$nl"/>

          <xsl:choose>
            <xsl:when test="$prev">
              <a id="prev" title="{$prev/s:title}"
                href="slide{$position - 1}{$file.extension}">Prev</a>
            </xsl:when>
            <xsl:otherwise>
              <a id="prev" title="{/s:slideset/s:metadata/s:title}"
                  href="title{$file.extension}">Prev</a>
            </xsl:otherwise>
          </xsl:choose>
          <xsl:value-of select="$nl"/>
          <xsl:if test="$next">
            <a id="next" title="{$next/s:title}"
                  href="slide{$position + 1}{$file.extension}">Next</a>
            <xsl:value-of select="$nl"/>
          </xsl:if>
        </div>
        <xsl:value-of select="$nl"/>
      </body>
      <xsl:value-of select="$nl"/>
    </html>
  </xsl:template>

  <xsl:template name="std.scripts">
    <!-- the following is used to give screen relative font sizes -->
    <style type="text/css" media="screen, projection" id="screen-style">
      html, body { font-size: 24pt; }
    </style>
    <xsl:value-of select="$nl"/>
    <script type="text/javascript" src="slides.js"></script>
    <xsl:value-of select="$nl"/>
  </xsl:template>

</xsl:stylesheet>
