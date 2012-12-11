%define	oname	yasp-scripted

Name:		plasma-applet-%{oname}
Version:	1.0.8a
Release:	1
Summary:	Yet Another Systemmonitor Plasmoid (scripted)
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		http://kde-apps.org/content/show.php?content=109367
Source0:	%{oname}-%{version}.tar.bz2
BuildRequires:	kdebase4-workspace-devel
Requires:	kdebase4-runtime
Provides:	plasma-applet

%description
Yet Another Systemmonitor Plasmoid (scripted) is a powerful system monitor.

%files
%doc README* GPLV2 yasp_scripts
%{_kde_libdir}/kde4/*.so
%{_kde_datadir}/kde4/services/*.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}

%build
%cmake_kde4
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

%clean
%__rm -rf %{buildroot}



%changelog
* Fri Jun 08 2012 Andrey Bondrov <abondrov@mandriva.org> 1.0.8a-1
+ Revision: 803471
- imported package plasma-applet-yasp-scripted


* Tue May 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1.0.8a-1mdv2010.2
- Initial build for Mandriva
