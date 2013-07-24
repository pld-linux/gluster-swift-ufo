# TODO: openstack-swift packages
Summary:	GlusterFS Unified File and Object Storage
Summary(pl.UTF-8):	GlusterFS UFO - ujednolicony sposób przechowywania plików i obiektów
Name:		gluster-swift-ufo
Version:	3.4.0
Release:	0.1
License:	Apache
Group:		Application/File
Source0:	http://download.gluster.org/pub/gluster/glusterfs/LATEST/%{name}-%{version}.tar.gz
# Source0-md5:	614628f29cd47fba95d1530363d7900b
URL:		http://www.gluster.org/
BuildRequires:	python >= 1:2.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	memcached
Requires:	python >= 1:2.6
Requires:	openstack-swift >= 1.4.8
Requires:	openstack-swift-account >= 1.4.8
Requires:	openstack-swift-container >= 1.4.8
Requires:	openstack-swift-object >= 1.4.8
Requires:	openstack-swift-proxy >= 1.4.8
Obsoletes:	gluster-swift
Obsoletes:	gluster-swift-plugin
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gluster Unified File and Object Storage unifies NAS and object storage
technology. This provides a system for data storage that enables users
to access the same data as an object and as a file, simplifying
management and controlling storage costs.

%description -l pl.UTF-8
Gluster UFO (Unified File and Object Storage) unifikuje technologie
przechowywania danych NAS i obiektów. Udostępnia system przechowywania
danych pozwalający użytkownikom na dostęp do tych samych danych jako
obiektu i jako pliku, co upraszcza zarządzanie i kontrolę kosztów.

%prep
%setup -q -n ufo

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/swift,%{_bindir}}

%{__python} setup.py install \
	--optimize=1 \
	--skip-build \
	--root $RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/test

%py_postclean

cp -a etc/* $RPM_BUILD_ROOT%{_sysconfdir}/swift
install bin/gluster-swift-gen-builders $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/gluster-swift-gen-builders
%{py_sitescriptdir}/gluster
%{py_sitescriptdir}/gluster_swift_ufo-1.1-py*.egg-info
%dir %{_sysconfdir}/swift
%dir %{_sysconfdir}/swift/account-server
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/swift/account-server/1.conf-gluster
%dir %{_sysconfdir}/swift/container-server
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/swift/container-server/1.conf-gluster
%dir %{_sysconfdir}/swift/object-server
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/swift/object-server/1.conf-gluster
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/swift/swift.conf-gluster
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/swift/proxy-server.conf-gluster
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/swift/fs.conf-gluster
