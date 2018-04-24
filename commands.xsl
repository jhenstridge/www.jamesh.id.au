<?xml version='1.0'?> <!--*- mode: xml -*-->
<!DOCTYPE xsl:stylesheet [
  <!ENTITY nbsp "&#160;">
  <!ENTITY nl   "&#10;">
]>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="1.0">
  <xsl:output method="text" />

  <xsl:template match="text()" />

  <xsl:template match="page">
    <xsl:text>process_file </xsl:text>
    <xsl:value-of select="@href" />
    <xsl:text>&nl;</xsl:text>
    <xsl:apply-templates />
  </xsl:template>
  <xsl:template match="file">
    <xsl:text>copy_file </xsl:text>
    <xsl:value-of select="@href" />
    <xsl:text>&nl;</xsl:text>
    <xsl:apply-templates />
  </xsl:template>
</xsl:stylesheet>
