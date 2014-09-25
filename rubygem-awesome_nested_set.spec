%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name awesome_nested_set
%global rubyabi 1.9.1

Summary: An awesome nested set implementation for Active Record
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.1.6
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/collectiveidea/awesome_nested_set
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems) 
Requires: %{?scl_prefix}rubygem(activerecord) >= 3.0.0
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}ruby(rubygems) 
BuildRequires: %{?scl_prefix}ruby 
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
An awesome nested set implementation for Active Record.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{?scl_prefix}%{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/MIT-LICENSE


%changelog
* Mon Sep 22 2014 root - 2.1.6-1
- Initial package
