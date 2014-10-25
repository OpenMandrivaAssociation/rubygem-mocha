# Generated from mocha-0.9.12.gem by gem2rpm5 -*- rpm-spec -*-
%define	rbname	mocha

Summary:	Mocking and stubbing library
Name:		rubygem-%{rbname}
Version:	1.1.0
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
Url:		http://mocha.rubyforge.org
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
Source1:	%{name}.rpmlintrc
BuildRequires:	rubygems
BuildArch:	noarch

%description
Mocking and stubbing library with JMock/SchMock syntax, which allows
mocking and stubbing of methods on real (non-mock) classes.

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

#----------------------------------------------------------------------------

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%gem_build -f '(examples|test)/'

%install
%gem_install
