# Generated from mocha-0.9.12.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	mocha

Summary:	Mocking and stubbing library
Name:		rubygem-%{rbname}

Version:	0.10.5
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://mocha.rubyforge.org
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
Source1:        %{name}.rpmlintrc
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Mocking and stubbing library with JMock/SchMock syntax, which allows
mocking and stubbing of methods on real (non-mock) classes.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(examples|test)/'

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/examples
%{ruby_gemdir}/gems/%{rbname}-%{version}/examples/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*



%changelog
* Wed Feb 29 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.10.5-1
+ Revision: 781468
- version update 0.10.5

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - imported package rubygem-mocha

* Wed Dec 01 2010 Rémy Clouard <shikamaru@mandriva.org> 0.9.10-1mdv2011.0
+ Revision: 604612
- import rubygem-mocha

