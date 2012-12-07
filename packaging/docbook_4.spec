Name:           docbook_4
BuildRequires:  fdupes
BuildRequires:  sgml-skel
BuildRequires:  unzip
Provides:       docbk_4
Provides:       docbook
Provides:       docbook-dtd
Provides:       docbook-dtds
Obsoletes:      docbk_4
Requires:       iso_ent
Requires:       libxml2
%define regcat /usr/bin/sgml-register-catalog
PreReq:         %{regcat} /usr/bin/xmlcatalog sgml-skel
PreReq:         sed grep awk
Summary:        DocBook DTD Version 4.x
License:        BSD-3-Clause ; MIT
Group:          Productivity/Publishing/DocBook
Version:        4.5
Release:        0
Source7:        CATALOG.docbook_4
# DocBook 4.1
Source410:      http://www.oasis-open.org/docbook/sgml/4.1/docbk41.zip
Source411:      http://www.oasis-open.org/docbook/xml/4.1/docbkx412.zip
# No RNG and XSD files for DB4.1
Source414:      CATALOG.db41xml
# DocBook 4.2
Source420:      http://www.oasis-open.org/docbook/sgml/4.2/docbook-4.2.zip
Source421:      http://www.oasis-open.org/docbook/xml/4.2/docbook-xml-4.2.zip
Source422:      http://www.oasis-open.org/docbook/rng/4.2/docbook-rng-4.2.zip
Source423:      http://www.oasis-open.org/docbook/xsd/4.2/docbook-xsd-4.2.zip
Source424:      CATALOG.db42xml
# DocBook 4.3
Source430:      http://www.docbook.org/sgml/4.3/docbook-4.3.zip
Source431:      http://www.docbook.org/xml/4.3/docbook-xml-4.3.zip
Source432:      http://www.docbook.org/rng/4.3/docbook-rng-4.3.zip
Source433:      http://www.docbook.org/xsd/4.3/docbook-xsd-4.3.zip
Source434:      CATALOG.db43xml
# DocBook 4.4
Source440:      http://www.oasis-open.org/docbook/sgml/4.4/docbook-4.4.zip
Source441:      http://www.oasis-open.org/docbook/xml/4.4/docbook-xml-4.4.zip
Source442:      http://www.docbook.org/rng/4.4/docbook-rng-4.4.zip
Source443:      http://www.docbook.org/xsd/4.4/docbook-xsd-4.4.zip
Source444:      CATALOG.db44xml
# DocBook 4.5
Source450:      http://www.oasis-open.org/docbook/sgml/4.5/docbook-4.5.zip
Source451:      http://www.oasis-open.org/docbook/xml/4.5/docbook-xml-4.5.zip
Source452:      http://www.docbook.org/rng/4.5/docbook-rng-4.5.zip
Source453:      http://www.docbook.org/xsd/4.5/docbook-xsd-4.5.zip
Source454:      CATALOG.db45xml
Patch0:         docbook-4-3-cat.diff
Patch1:         docbook-4-3.diff
Patch2:         docbook-4-3-xml-cat.diff
Patch3:         docbook.4.4.dcl.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Url:            http://www.oasis-open.org/docbook/

%description
DocBook is a schema. It is particularly well-suited to books and papers
about computer hardware and software (though it is not limited to these
applications at all). This package has SGML- and XML-DTD versions
included. Some versions of DocBook contain also a RELAX NG and W3C
Schema.

%define INSTALL install -m755 -s
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644
%define INSTALL_SCRIPT install -m755
%define sgml_dir %{_datadir}/sgml
%define sgml_docbook_dir %{sgml_dir}/docbook
%define sgml_docbook_dtd_dir %{sgml_docbook_dir}/dtd
%define sgml_docbook_custom_dir %{sgml_docbook_dir}/custom
%define sgml_docbook_style_dir %{sgml_docbook_dir}/stylesheet
%define xml_dir %{_datadir}/xml
%define xml_docbook_dir %{xml_dir}/docbook
%define xml_docbook_dtd_dir %{xml_docbook_dir}/schema/dtd
%define xml_docbook_rng_dir %{xml_docbook_dir}/schema/rng
%define xml_docbook_xsd_dir %{xml_docbook_dir}/schema/xsd
%define xml_docbook_custom_dir %{xml_docbook_dir}/custom
%define xml_docbook_style_dir %{xml_docbook_dir}/stylesheet
%define sgml_config_dir /var/lib/sgml
%define sgml_sysconf_dir %{_sysconfdir}/sgml
%define xml_config_dir /var/lib/xml
%define xml_sysconf_dir %{_sysconfdir}/xml

%prep
%setup -n %{name} -c -T
%{INSTALL_DIR} dtd/4.{1,2,3,4,5} 4.{1,2,3,4,5}xml
echo "**** %{S:410}"
pushd dtd/4.1
  unzip -q -a %{S:410}
popd
pushd 4.1xml
  unzip -q -a %{S:411}
popd
pushd dtd/4.2
  unzip -q -a %{S:420}
popd
pushd 4.2xml
  unzip -q -a %{S:421}
popd
pushd dtd/4.3
  unzip -q -a %{S:430}
popd
pushd 4.3xml
  unzip -q -a %{S:431}
popd
pushd dtd/4.4
  unzip -q -a %{S:440}
%patch3 -p 0
popd
pushd 4.4xml
  unzip -q -a %{S:441}
popd
pushd dtd/4.5
  unzip -q -a %{S:450}
popd
pushd 4.5xml
  unzip -q -a %{S:451}
popd
%patch -p 1 -P 1 -p 0
%patch2 -p 1
# CATALOG.* files
cp %{S:7} %{S:414} %{S:424} %{S:434} %{S:444} %{S:454} .
chmod -R a+rX,g-w,o-w .
find . -type f | xargs chmod a-x

%build
CATALOG=docbook_41.xml
# # build root catalog fragment
xmlcatbin=/usr/bin/xmlcatalog
$xmlcatbin --create --noout $CATALOG
docbookdir=%{xml_docbook_dtd_dir}/4.1
$xmlcatbin --noout --add "public" \
    "-//OASIS//ELEMENTS DocBook XML Information Pool V4.1.2//EN" \
    "file://$docbookdir/dbpoolx.mod" $CATALOG
$xmlcatbin --noout --add "public" \
    "-//OASIS//DTD DocBook XML V4.1.2//EN" \
    "file://$docbookdir/docbookx.dtd" $CATALOG
$xmlcatbin --noout --add "public" \
    "-//OASIS//ENTITIES DocBook XML Character Entities V4.1.2//EN" \
    "file://$docbookdir/dbcentx.mod" $CATALOG
$xmlcatbin --noout --add "public" \
    "-//OASIS//ENTITIES DocBook XML Notations V4.1.2//EN" \
    "file://$docbookdir/dbnotnx.mod" $CATALOG
$xmlcatbin --noout --add "public" \
    "-//OASIS//ENTITIES DocBook XML Additional General Entities V4.1.2//EN" \
    "file://$docbookdir/dbgenent.mod" $CATALOG
$xmlcatbin --noout --add "public" \
    "-//OASIS//ELEMENTS DocBook XML Document Hierarchy V4.1.2//EN" \
    "file://$docbookdir/dbhierx.mod" $CATALOG
$xmlcatbin --noout --add "public" \
    "-//OASIS//DTD XML Exchange Table Model 19990315//EN" \
    "file://$docbookdir/soextblx.dtd" $CATALOG
$xmlcatbin --noout --add "public" \
    "-//OASIS//DTD DocBook XML CALS Table Model V4.1.2//EN" \
    "file://$docbookdir/calstblx.dtd" $CATALOG
$xmlcatbin --noout --add "rewriteSystem" \
    "http://www.oasis-open.org/docbook/xml/4.1.2" \
    "file://$docbookdir" $CATALOG
$xmlcatbin --noout --add "rewriteURI" \
    "http://www.oasis-open.org/docbook/xml/4.1.2" \
    "file://$docbookdir" $CATALOG
# === iso
isodir=$docbookdir/ent
$xmlcatbin --noout --add "public" \
    "ISO 8879:1986//ENTITIES Publishing//EN//XML" \
    "file://$isodir/iso-pub.ent" $CATALOG
$xmlcatbin --noout --add "public" \
    "ISO 8879:1986//ENTITIES Greek Letters//EN//XML" \
    "file://$isodir/iso-grk1.ent" $CATALOG
$xmlcatbin --noout --add "public" \
    "ISO 8879:1986//ENTITIES Box and Line Drawing//EN//XML" \
    "file://$isodir/iso-box.ent" $CATALOG
$xmlcatbin --noout --add "public" \
    "ISO 8879:1986//ENTITIES Greek Symbols//EN//XML" \
    "file://$isodir/iso-grk3.ent" $CATALOG
$xmlcatbin --noout --add "public" \
    "ISO 8879:1986//ENTITIES Added Math Symbols: Negated Relations//EN//XML" \
    "file://$isodir/iso-amsn.ent" $CATALOG
$xmlcatbin --noout --add "public" \
    "ISO 8879:1986//ENTITIES Numeric and Special Graphic//EN//XML" \
    "file://$isodir/iso-num.ent" $CATALOG
$xmlcatbin --noout --add "public" \
    "ISO 8879:1986//ENTITIES Alternative Greek Symbols//EN//XML" \
    "file://$isodir/iso-grk4.ent" $CATALOG
$xmlcatbin --noout --add "public" \
    "ISO 8879:1986//ENTITIES Diacritical Marks//EN//XML" \
    "file://$isodir/iso-dia.ent" $CATALOG
$xmlcatbin --noout --add "public" \
    "ISO 8879:1986//ENTITIES Monotoniko Greek//EN//XML" \
    "file://$isodir/iso-grk2.ent" $CATALOG
$xmlcatbin --noout --add "public" \
    "ISO 8879:1986//ENTITIES Added Math Symbols: Arrow Relations//EN//XML" \
    "file://$isodir/iso-amsa.ent" $CATALOG
$xmlcatbin --noout --add "public" \
    "ISO 8879:1986//ENTITIES Added Math Symbols: Ordinary//EN//XML" \
    "file://$isodir/iso-amso.ent" $CATALOG
$xmlcatbin --noout --add "public" \
    "ISO 8879:1986//ENTITIES Russian Cyrillic//EN//XML" \
    "file://$isodir/iso-cyr1.ent" $CATALOG
$xmlcatbin --noout --add "public" \
    "ISO 8879:1986//ENTITIES General Technical//EN//XML" \
    "file://$isodir/iso-tech.ent" $CATALOG
$xmlcatbin --noout --add "public" \
    "ISO 8879:1986//ENTITIES Added Math Symbols: Delimiters//EN//XML" \
    "file://$isodir/iso-amsc.ent" $CATALOG
$xmlcatbin --noout --add "public" \
    "ISO 8879:1986//ENTITIES Added Latin 1//EN//XML" \
    "file://$isodir/iso-lat1.ent" $CATALOG
$xmlcatbin --noout --add "public" \
    "ISO 8879:1986//ENTITIES Added Math Symbols: Binary Operators//EN//XML" \
    "file://$isodir/iso-amsb.ent" $CATALOG
$xmlcatbin --noout --add "public" \
    "ISO 8879:1986//ENTITIES Added Latin 2//EN//XML" \
    "file://$isodir/iso-lat2.ent" $CATALOG
$xmlcatbin --noout --add "public" \
    "ISO 8879:1986//ENTITIES Added Math Symbols: Relations//EN//XML" \
    "file://$isodir/iso-amsr.ent" $CATALOG
$xmlcatbin --noout --add "public" \
    "ISO 8879:1986//ENTITIES Non-Russian Cyrillic//EN//XML" \
    "file://$isodir/iso-cyr2.ent" $CATALOG
# ====
%define FOR_ROOT_CAT for-catalog-%{name}-%{version}.xml
CATALOG=etc/xml/$CATALOG
rm -f %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --create %{FOR_ROOT_CAT}.tmp
for v in 4.2 4.3 4.4 4.5; do
  cat42=%{xml_docbook_dtd_dir}/$v/catalog.xml
  for s in \
    "-//OASIS//DTD DocBook XML V${v}//EN" \
    "-//OASIS//DTD DocBook CALS Table Model V${v}//EN" \
    "-//OASIS//DTD XML Exchange Table Model 19990315//EN" \
    "-//OASIS//ELEMENTS DocBook Information Pool V${v}//EN" \
    "-//OASIS//ELEMENTS DocBook Document Hierarchy V${v}//EN" \
    "-//OASIS//ENTITIES DocBook Additional General Entities V${v}//EN" \
    "-//OASIS//ENTITIES DocBook Notations V${v}//EN" \
    "-//OASIS//ENTITIES DocBook Character Entities V${v}//EN"
   do
   $xmlcatbin --noout --add "delegatePublic" "$s" \
     "file://$cat42" %{FOR_ROOT_CAT}.tmp
  done
  case $v in
    4.[345])
      $xmlcatbin --noout --add "delegatePublic" \
         "-//OASIS//ELEMENTS DocBook XML HTML Tables V${v}//EN" \
         "file://$cat42" %{FOR_ROOT_CAT}.tmp
      ;;
    *)
      true
  esac
  $xmlcatbin --noout --add "delegateSystem" \
    "http://www.oasis-open.org/docbook/xml/${v}" \
    "file://$cat42" %{FOR_ROOT_CAT}.tmp
  $xmlcatbin --noout --add "delegateURI" \
    "http://www.oasis-open.org/docbook/xml/${v}" \
    "file://$cat42" %{FOR_ROOT_CAT}.tmp
  $xmlcatbin --noout --add "rewriteSystem" \
    "http://www.oasis-open.org/docbook/xml/${v}" \
    "file://%{xml_docbook_dtd_dir}/${v}" %{FOR_ROOT_CAT}.tmp
  $xmlcatbin --noout --add "delegatePublic" \
    "ISO 8879:1986" \
    "file:///$CATALOG" %{FOR_ROOT_CAT}.tmp
done
# 41xml
for s in \
  "-//OASIS//DTD DocBook XML V4.1" \
  "-//OASIS//ELEMENTS DocBook Information Pool V4.1" \
  "-//OASIS//ELEMENTS DocBook Document Hierarchy V4.1" \
  "-//OASIS//ENTITIES DocBook Additional General Entities V4.1" \
  "-//OASIS//ENTITIES DocBook Notations V4.1" \
  "-//OASIS//ENTITIES DocBook Character Entities V4.1"
 do
 $xmlcatbin --noout --add "delegatePublic" "$s" \
   "file:///$CATALOG" %{FOR_ROOT_CAT}.tmp
done
$xmlcatbin --noout --add "delegateSystem" \
  "http://www.oasis-open.org/docbook/xml/4.1" \
  "file:///$CATALOG" %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --add "delegateURI" \
  "http://www.oasis-open.org/docbook/xml/4.1" \
  "file:///$CATALOG" %{FOR_ROOT_CAT}.tmp
# Create tag
sed '/<catalog/a\
  <group id="%{name}-%{version}">
/<\/catalog/i\
  </group>' \
  %{FOR_ROOT_CAT}.tmp > %{FOR_ROOT_CAT}

%install
%{INSTALL_DIR} $RPM_BUILD_ROOT%{sgml_config_dir}
%{INSTALL_DIR} $RPM_BUILD_ROOT%{xml_config_dir}
%{INSTALL_DATA} CATALOG.* $RPM_BUILD_ROOT%{sgml_config_dir}
# for CATALOG.* links
%define my_all_cat docbook_4 db41xml db42xml db43xml db44xml db45xml
for v in 4.1 4.2 4.3 4.4 4.5; do
  vl=${v/\.}
  %{INSTALL_DIR} $RPM_BUILD_ROOT%{sgml_docbook_dtd_dir}/$v
  %{INSTALL_DATA} dtd/${v}/* $RPM_BUILD_ROOT%{sgml_docbook_dtd_dir}/${v}
  %{INSTALL_DIR} $RPM_BUILD_ROOT%{xml_docbook_dtd_dir}/$v
  cp -a ${v}xml/* $RPM_BUILD_ROOT%{xml_docbook_dtd_dir}/$v
  ln -s %{xml_docbook_dtd_dir}/$v $RPM_BUILD_ROOT%{sgml_docbook_dtd_dir}/${v}xml
  ln -sf %{sgml_config_dir}/CATALOG.db${vl}xml \
    $RPM_BUILD_ROOT%{sgml_dir}/CATALOG.db${vl}xml
done
ln -sf %{sgml_docbook_dtd_dir}/4.1 $RPM_BUILD_ROOT%{sgml_dir}/%{name}.1
ln -sf %{sgml_config_dir}/CATALOG.%{name} \
  $RPM_BUILD_ROOT%{sgml_dir}/CATALOG.%{name}
ln -sf %{sgml_config_dir}/CATALOG.%{name} \
  $RPM_BUILD_ROOT%{sgml_dir}/CATALOG.docbk41
cat_dir=%{buildroot}/etc/xml
%{INSTALL_DIR} $cat_dir
%{INSTALL_DATA} %{FOR_ROOT_CAT} docbook_41.xml $cat_dir
# rng
%{INSTALL_DIR} $RPM_BUILD_ROOT%{xml_docbook_rng_dir}/{4.3,4.4} \
               $RPM_BUILD_ROOT%{xml_docbook_xsd_dir}/{4.3,4.4}
unzip -q -a -d $RPM_BUILD_ROOT%{xml_docbook_rng_dir}/4.2 %{S:422}
unzip -q -a -d $RPM_BUILD_ROOT%{xml_docbook_rng_dir}/4.3 %{S:432}
unzip -q -a -d $RPM_BUILD_ROOT%{xml_docbook_rng_dir}/4.4 %{S:442}
unzip -q -a -d $RPM_BUILD_ROOT%{xml_docbook_rng_dir}/4.5 %{S:452}
# w3c schema
unzip -q -a -d $RPM_BUILD_ROOT%{xml_docbook_xsd_dir}/4.2 %{S:422}
unzip -q -a -d $RPM_BUILD_ROOT%{xml_docbook_xsd_dir}/4.3 %{S:433}
unzip -q -a -d $RPM_BUILD_ROOT%{xml_docbook_xsd_dir}/4.4 %{S:443}
unzip -q -a -d $RPM_BUILD_ROOT%{xml_docbook_xsd_dir}/4.5 %{S:453}
# cleanup
%fdupes $RPM_BUILD_ROOT

%post
if [ -x %{regcat} ]; then
  for c in %{my_all_cat}; do
    %{regcat} -a  %{sgml_dir}/CATALOG.$c \
      >/dev/null 2>&1 || true
  done
fi
if [ -x /usr/bin/edit-xml-catalog ]; then
  /usr/bin/edit-xml-catalog --group --catalog /etc/xml/suse-catalog.xml \
      --add /etc/xml/%{FOR_ROOT_CAT}
fi

%postun
if [ "$1" = "0" -a -x %{regcat} ]; then
  for c in %{my_all_cat}; do
    %{regcat} -r %{sgml_dir}/CATALOG.$c \
      >/dev/null 2>&1 || true
  done
fi
# remove entries only on removal of file
if [ ! -f %{xml_sysconf_dir}/%{FOR_ROOT_CAT} -a -x /usr/bin/edit-xml-catalog ] ; then
  /usr/bin/edit-xml-catalog --group --catalog /etc/xml/suse-catalog.xml \
      --del %{name}-%{version}
fi

%files
%defattr(-, root, root)
%config %{sgml_config_dir}/CATALOG.*
%{sgml_dir}/CATALOG.*
%{sgml_docbook_dtd_dir}/4.1
%{sgml_docbook_dtd_dir}/4.2
%{sgml_docbook_dtd_dir}/4.3
%{sgml_docbook_dtd_dir}/4.4
%{sgml_docbook_dtd_dir}/4.5
#
%{sgml_docbook_dtd_dir}/4.1xml
%{sgml_docbook_dtd_dir}/4.2xml
%{sgml_docbook_dtd_dir}/4.3xml
%{sgml_docbook_dtd_dir}/4.4xml
%{sgml_docbook_dtd_dir}/4.5xml
#
%{xml_docbook_dtd_dir}/4.1
%{xml_docbook_dtd_dir}/4.2
%{xml_docbook_dtd_dir}/4.3
%{xml_docbook_dtd_dir}/4.4
%{xml_docbook_dtd_dir}/4.5
#
%{xml_docbook_rng_dir}/4.2
%{xml_docbook_rng_dir}/4.3
%{xml_docbook_rng_dir}/4.4
%{xml_docbook_rng_dir}/4.5
#
%{xml_docbook_xsd_dir}/4.2
%{xml_docbook_xsd_dir}/4.3
%{xml_docbook_xsd_dir}/4.4
%{xml_docbook_xsd_dir}/4.5
#
%config %{xml_sysconf_dir}/docbook_41.xml
%config %{xml_sysconf_dir}/%{FOR_ROOT_CAT}
%dir %{sgml_dir}/docbook/dtd
%{sgml_dir}/docbook_4.1
# %dir %{xml_dir}
# %dir %{xml_docbook_dir}
%dir %{xml_docbook_dir}/schema
%dir %{xml_docbook_dtd_dir}
%dir %{xml_docbook_rng_dir}
%dir %{xml_docbook_xsd_dir}

%changelog
