
SRCDIR=content
DESTDIR=build.tmp

copyrightyear=`date +%Y`

copy_file() {
    local filename dirname

    filename="$1"
    dirname=`dirname "$DESTDIR/$filename"`
    mkdir -p "$dirname"
    cp -f "$SRCDIR/$filename" "$DESTDIR/$filename" || {
	echo "could not copy file $filename" >&2
	exit 1
    }
}

copy_dir() {
    local dir filename

    dir="$1"
    files="`(cd $SRCDIR && find $dir -type f)`"
    if [ -n "$files" ]; then
	for filename in $files; do
	    copy_file $filename
	done
    fi
}

process_file() {
    local filename dirname tmpfile website documenturl

    filename="$1"
    dirname=`dirname "$DESTDIR/$filename"`
    mkdir -p "$dirname"

    website=`pwd`/content/website.xml
    if [ `basename "$filename"` = 'index.html' ]; then
	documenturl=`echo "$filename" | sed 's/index\.html$//'`
    else
	documenturl="$filename"
    fi
    xsltproc --stringparam website.tree "$website" \
	--stringparam document.url "$documenturl" \
        --stringparam document.copyrightyear $copyrightyear \
	$SRCDIR/process.xsl $SRCDIR/$filename > $DESTDIR/$filename || {
	echo "Could not parse file $filename" >&2
	exit 1
    }
    xmllint -noout -valid "$DESTDIR/$filename" || echo "$filename does not validate"
}

process_docbook() {
    local filename dirname

    filename="$1"
    dirname=`dirname "$DESTDIR/$filename"`

    xmlto xhtml-nochunks -m db-custom.xsl -o $dirname $SRCDIR/$filename
    copy_file "$filename"
}

process_file index.html
copy_file style.css
copy_file james.jpeg
copy_file .htaccess
copy_dir .icons

# software
process_file software/index.html
process_file software/pygtk/index.html
copy_file software/pygtk/pygtk.jpeg
process_file software/pygimp/index.html
copy_file software/pygimp/gimp-python.jpeg
copy_file software/pygimp/pygimp.sgml
copy_file software/pygimp/pygimp.html
copy_file software/pygimp/end-note.html
copy_file software/pygimp/gimp-module-procedures.html
copy_file software/pygimp/gimp-objects.html
copy_file software/pygimp/procedural-database.html
copy_file software/pygimp/structure-of-plugin.html
copy_file software/pygimp/support-modules.html
process_file software/libglade/index.html
process_file software/jhbuild/index.html
process_file software/fontilus/index.html
copy_file software/fontilus/fontilus-screenshot.png
copy_file software/fontilus/fontilus-thumb-icons.png
copy_file software/fontilus/fontilus-thumb-list.png
copy_file software/fontilus/fontilus-font-viewer.png
copy_file software/fontilus/fontilus-context-menu.png
process_file software/nautilus-rpm/index.html
copy_file software/nautilus-rpm/nautilus-rpm-screenshot.png
process_file software/gnorpm/index.html
copy_file software/gnorpm/gnorpm-0.6.gif
process_file software/www-sql/index.html
copy_file software/www-sql/Changelog
copy_file software/www-sql/www-sql.html

# talks
process_file talks/index.html
copy_dir talks/guadec2000
copy_dir talks/guadec2001
copy_dir talks/guadec2002
copy_dir talks/lca2003
copy_dir talks/guadec2003
copy_dir talks/lca2004

# articles
process_file articles/index.html
process_docbook articles/libxml-sax/libxml-sax.xml
process_file articles/mailman-spamassassin/index.html
copy_file articles/mailman-spamassassin/spamd.py
copy_file articles/mailman-spamassassin/SpamAssassin.py
copy_file articles/mailman-spamassassin/mmlearn

# fractals website
process_file fractals/index.html
copy_file fractals/images/fract-bg.gif
process_file fractals/ifs/intro.html
process_file fractals/ifs/javaifs.html
copy_file fractals/ifs/ifs.java
copy_file fractals/ifs/ifs.class
process_file fractals/ifs/triangle.html
process_file fractals/ifs/fern.html
process_file fractals/ifs/spiral.html
process_file fractals/ifs/dragon.html
process_file fractals/ifs/formula.html
process_file fractals/mandel/intro.html
process_file fractals/mandel/formula.html
copy_file fractals/mandel/Cmplx.java
copy_file fractals/mandel/Cmplx.class
copy_file fractals/mandel/Controls.java
copy_file fractals/mandel/Controls.class
copy_file fractals/mandel/FracPanel.java
copy_file fractals/mandel/FracPanel.class
process_file fractals/mandel/Mandel.html
copy_file fractals/mandel/Mandel.java
copy_file fractals/mandel/Mandel.class
process_file fractals/mandel/Mandel3.html
copy_file fractals/mandel/Mandel3.java
copy_file fractals/mandel/Mandel3.class
process_file fractals/mandel/Mandel4.html
copy_file fractals/mandel/Mandel4.java
copy_file fractals/mandel/Mandel4.class
process_file fractals/mandel/Phoenix.html
copy_file fractals/mandel/Phoenix.java
copy_file fractals/mandel/Phoenix.class
process_file fractals/mandel/Newton3.html
copy_file fractals/mandel/Newton3.java
copy_file fractals/mandel/Newton3.class
process_file fractals/orbit/intro.html
process_file fractals/orbit/popcorn.html
copy_file fractals/orbit/popcorn.java
copy_file fractals/orbit/popcorn.class
process_file fractals/orbit/gingerbread.html
copy_file fractals/orbit/gingerbread.java
copy_file fractals/orbit/gingerbread.class
process_file fractals/orbit/hopalong.html
copy_file fractals/orbit/hopalong.java
copy_file fractals/orbit/hopalong.class
process_file fractals/orbit/threeply.html
copy_file fractals/orbit/threeply.java
copy_file fractals/orbit/threeply.class
process_file fractals/orbit/quadruptwo.html
copy_file fractals/orbit/quadruptwo.java
copy_file fractals/orbit/quadruptwo.class
process_file fractals/orbit/inv_julia.html
copy_file fractals/orbit/inv_julia.java
copy_file fractals/orbit/inv_julia.class

# copy over, maintaining timestamps
mkdir -p build
rsync -rlpc --delete $DESTDIR/ build || exit 1
rm -rf $DESTDIR
