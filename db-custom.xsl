<?xml version="1.0"?> <?emacs -*- mode: xml -*- ?>
<xsl:stylesheet xmlns="http://www.w3.org/1999/xhtml"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="1.0">

  <xsl:param name="default.encoding" select="'ISO-8859-1'"/>
  <xsl:param name="use.id.as.filename" select="1"/>
  <xsl:param name="html.ext" select="'.html'"/>
  <xsl:param name="funcsynopsis.style" select="'ansi'"/>

  <xsl:template name="user.head.content">
    <style type="text/css">
      <xsl:text>
html, body {
  font-family: sans-serif;
  color: black;
  background-color: white;
}
 
.programlisting, .funcsynopsis{
  margin-left: 5em;
  margin-right: 5em;
  padding: 0.5em;
  clear: both;
 
  color: black;
  background-color: #eeeeff;
  border: solid 1px #aaaaff;
}

hr {
  width: 80%;
  border: 0px;
  background-color: #7f7f7f;
}
      </xsl:text>
    </style>
  </xsl:template> 
</xsl:stylesheet>
