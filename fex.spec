Name: fex
Version: 2.0.0
Release: 1
License: Apache 2.0
URL: http://www.semicomplete.com/projects/fex/
Source0:  http://semicomplete.googlecode.com/files/%{name}-2.0.0.tar.gz
Summary: field split/extraction like cut/awk with less typing
Group: Applications/System
BuildRoot:    %{_tmppath}/%{name}-2.0.0-%{release}-root-%(%{__id_u} -n)


%description
Fex is a powerful field extraction tool. Fex provides a very concise language
for tokenizeing strings and extracting fields.

%prep
%setup

%build
make all

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} PREFIX="/usr"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0755)
/usr/bin/fex
/usr/share/man/man1/fex.1
