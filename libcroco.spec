Name:             libcroco
Summary:          A CSS2 parsing library
Version:          0.6.2
Release: 	  5%{?dist}
License:          LGPLv2
Group:            System Environment/Libraries
Source:           http://download.gnome.org/sources/libcroco/0.6/%{name}-%{version}.tar.bz2
BuildRoot:        %{_tmppath}/%{name}-%{version}-root
Patch0:		  libcroco-0.6.1-multilib.patch

BuildRequires:    pkgconfig >= 0.8
BuildRequires:    glib2-devel >= 2.3
BuildRequires:    libxml2-devel >= 2.4.23

%description
CSS2 parsing and manipulation library for GNOME

%package devel
Summary:          Libraries and include files for developing with libcroco.
Group:            Development/Libraries
Requires:         %{name} = %{version}
Requires:         pkgconfig >= 0.8
Requires:         glib2-devel >= 2.0
Requires:         libxml2-devel >= 2.4.23

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with libcroco.

%prep
%setup -q -n libcroco-%{version}
%patch0 -p1 -b .multilib

%build
:%configure --enable-seleng=yes --enable-layeng=yes
make

%install
rm -rf $RPM_BUILD_ROOT
# create file that the new redhat debuginfo stuff demands
touch $RPM_BUILD_DIR/libcroco-%{version}/debugfiles.list

%makeinstall
# Clean out files that should not be part of the rpm.
# This is the recommended way of dealing with it for RH8
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING COPYING.LIB NEWS README 
%{_bindir}/csslint-0.6
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{_libdir}/*.so
%{_includedir}/libcroco-0.6
%{_bindir}/croco-0.6-config
%{_libdir}/pkgconfig/libcroco-0.6.pc

%changelog
* Fri Jan  8 2010 Owen Taylor <otaylor@redhat.com> - 0.6.2-5
- Fix URL source URL not to be download/gnome.org
  Related: rhbz 543948

* Tue Dec  8 2009 Matthias Clasen <mclasen@redhat.com> - 0.6.2-4
- Add source url

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb  4 2009 Matthias Clasen <mclasen@redhat.com> - 0.6.2-1
- Update to 0.6.2

* Tue Apr  1 2008 Matthias Clasen <mclasen@redhat.com> - 0.6.1-5
- Clean up dependencies

* Fri Feb  8 2008 Matthias Clasen <mclasen@redhat.com> - 0.6.1-4
- Rebuild for gcc 4.3

* Wed Oct 10 2007 Matthias Clasen <mclasen@redhat.com> - 0.6.1-3
- Rebuild
- Update license tag

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.6.1-2.1
- rebuild

* Tue May 23 2006 Matthias Clasen <mclasen@redhat.com> - 0.6.1-2
- Make config script a pkg-config wrapper to fix multilib conflict

* Mon Mar 13 2006 Matthias Clasen <mclasen@redhat.com> - 0.6.1-1
- Update to 0.6.1
- Drop upstreamed patches

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.6.0-6.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.6.0-6.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sat Oct 15 2005 Florian La Roche <laroche@redhat.com>
- link shared lib against -lglib-2.0 and -lxml2

* Wed Mar  2 2005 Matthias Clasen <mclasen@redhat.com> - 0.6.0-5
- Rebuild with gcc4

* Wed Sep 22 2004 Matthias Clasen <mclasen@redhat.com> - 0.6.0-4
- Move croco-config to the devel package

* Mon Sep 20 2004 Matthias Clasen <mclasen@redhat.com> - 0.6-3
- Don't memset() stack variables

* Tue Aug 31 2004 Matthias Clasen <mclasen@redhat.com> - 0.6-2
- Add missing ldconfig calls (#131279)

* Fri Jul 30 2004 Matthias Clasen <mclasen@redhat.com> - 0.6-1
- Update to 0.6

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Apr 10 2004 Warren Togami <wtogami@redhat.com>
- BR and -devel req libgnomeui-devel

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jan 27 2004 Jonathan Blandford <jrb@redhat.com> 0.4.0-1
- new version

* Wed Aug 13 2003 Jonathan Blandford <jrb@redhat.com> 0.3.0-1
- initial import into the tree.  Based on the spec file in the package
