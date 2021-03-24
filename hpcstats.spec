Name:		hpcstats		
Version:	1.6.3	
Release:	1%{?dist}.edf
Summary:	HPC cluster usage accounting and reporting software	

License:	Proprietary
URL:		http://github.com/edf-hpc/hpcstats
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	python3-setuptools
BuildRequires:	python3-sphinx
BuildRequires:	python3-sphinx_rtd_theme
Requires: rpm-cron
Requires: postgresql

%description
HPC cluster usage accounting and reporting software 
HPCStats imports raw data from various sources (Job schedulers, log
files, LDAP directories, etc. and insert everything into a coherent
and structured PostgreSQL database. Then, all these structured
information can be used to extract statistics about the usage of the HPC clusters.

%files
%doc README.md
%{python3_sitelib}
%{_bindir}/hpcstats

%package -n hpcstats-jobstats-agent
Summary: Jobstat agent of HPC cluster usage accounting software 
Requires: python3

%description -n hpcstats-jobstats-agent
This agent is typically installed on HPC cluster frontend. It provides all files required by the launcher to test end-to-end HPC cluster availability.

%files -n hpcstats-jobstats-agent
%{python3_sitelib}

%package -n hpcstats-jobstats-launcher
Summary: Jobstat launcher of HPC cluster usage accounting software 
Requires: python3
Requires: python3-paramiko

%description -n hpcstats-jobstats-launcher
The component launches the jobstats agent on all configured HPC cluster frontends.

%files -n hpcstats-jobstats-launcher
%{python3_sitelib}

%package -n hpcstats-fsusage-agent
Summary: FSUsage agent of HPC cluster usage accounting software 
Requires: python3

%description -n hpcstats-fsusage-agent
This agent is typically installed on HPC cluster frontend to log in a CSV file the usage rate of file systems.

%files -n hpcstats-fsusage-agent
%{python3_sitelib}

%package -n hpcstats-utils
Summary: Various utilities of HPC cluster usage accounting software 
Requires: python3
Requires: python3-psycopg2

%description -n hpcstats-utils
Set of various utilities for HPCStats accounting software:
   - script to encode passwords in configurations files.
   - script to add descriptions to BusinessCodes and Projects
   - script to add Domains

%files -n hpcstats-utils
%{python3_sitelib}

%global debug_package %{nil}

%prep
%setup -q


%build
CFLAGS="%{optflags}" python3 setup.py build


%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}


%changelog
* Thu Mar 18 2021 Nilce BOUSSAMBA <nilce-externe.boussamba@edf.fr>
- first rpm package
