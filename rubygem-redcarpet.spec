%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name redcarpet
%global rubyabi 1.9.1

Summary: Markdown that smells nice
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.3.0
Release: 1%{?dist}
Group: Development/Languages
License: Apache 2.0
URL: http://github.com/vmg/redcarpet
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems) 
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}ruby(rubygems) 
BuildRequires: %{?scl_prefix}ruby-devel 
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A fast, safe and extensible Markdown to (X)HTML parser.


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
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --bindir .%{_bindir} \
            -V \
            --force %{SOURCE0}
%{?scl:"}
%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/redcarpet
%{gem_instdir}/bin
%{gem_instdir}/lib
%{gem_instdir}/Rakefile
%{gem_instdir}/README.markdown
%{gem_instdir}/Gemfile
%{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/ext
%exclude %{gem_instdir}/test
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/COPYING


%changelog
* Wed Sep 24 2014 root - 2.3.0-1
- Initial package
