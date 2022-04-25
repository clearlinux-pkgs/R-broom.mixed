#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-broom.mixed
Version  : 0.2.9.4
Release  : 4
URL      : https://cran.r-project.org/src/contrib/broom.mixed_0.2.9.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/broom.mixed_0.2.9.4.tar.gz
Summary  : Tidying Methods for Mixed Models
Group    : Development/Tools
License  : GPL-3.0
Requires: R-broom
Requires: R-coda
Requires: R-dplyr
Requires: R-forcats
Requires: R-furrr
Requires: R-purrr
Requires: R-stringr
Requires: R-tibble
Requires: R-tidyr
BuildRequires : R-broom
BuildRequires : R-coda
BuildRequires : R-dplyr
BuildRequires : R-forcats
BuildRequires : R-furrr
BuildRequires : R-purrr
BuildRequires : R-stringr
BuildRequires : R-tibble
BuildRequires : R-tidyr
BuildRequires : buildreq-R

%description
into tidy data frames along the lines of the 'broom' package.
    The package provides three

%prep
%setup -q -c -n broom.mixed
cd %{_builddir}/broom.mixed

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650295796

%install
export SOURCE_DATE_EPOCH=1650295796
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library broom.mixed
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library broom.mixed
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library broom.mixed
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc broom.mixed || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/broom.mixed/DESCRIPTION
/usr/lib64/R/library/broom.mixed/INDEX
/usr/lib64/R/library/broom.mixed/Meta/Rd.rds
/usr/lib64/R/library/broom.mixed/Meta/features.rds
/usr/lib64/R/library/broom.mixed/Meta/hsearch.rds
/usr/lib64/R/library/broom.mixed/Meta/links.rds
/usr/lib64/R/library/broom.mixed/Meta/nsInfo.rds
/usr/lib64/R/library/broom.mixed/Meta/package.rds
/usr/lib64/R/library/broom.mixed/Meta/vignette.rds
/usr/lib64/R/library/broom.mixed/NAMESPACE
/usr/lib64/R/library/broom.mixed/NEWS.Rd
/usr/lib64/R/library/broom.mixed/R/broom.mixed
/usr/lib64/R/library/broom.mixed/R/broom.mixed.rdb
/usr/lib64/R/library/broom.mixed/R/broom.mixed.rdx
/usr/lib64/R/library/broom.mixed/capabilities.csv
/usr/lib64/R/library/broom.mixed/doc/broom_mixed_intro.R
/usr/lib64/R/library/broom.mixed/doc/broom_mixed_intro.html
/usr/lib64/R/library/broom.mixed/doc/broom_mixed_intro.rmd
/usr/lib64/R/library/broom.mixed/doc/index.html
/usr/lib64/R/library/broom.mixed/extdata/8schools.stan
/usr/lib64/R/library/broom.mixed/extdata/MCMCglmm_example.rda
/usr/lib64/R/library/broom.mixed/extdata/R2jags_example.rds
/usr/lib64/R/library/broom.mixed/extdata/brms_example.rda
/usr/lib64/R/library/broom.mixed/extdata/efc.rds
/usr/lib64/R/library/broom.mixed/extdata/example_helpers.R
/usr/lib64/R/library/broom.mixed/extdata/gamlss_example.rds
/usr/lib64/R/library/broom.mixed/extdata/glmmADMB_example.rda
/usr/lib64/R/library/broom.mixed/extdata/glmmTMB_example.rda
/usr/lib64/R/library/broom.mixed/extdata/lme4_example.rda
/usr/lib64/R/library/broom.mixed/extdata/nlme_example.rda
/usr/lib64/R/library/broom.mixed/extdata/rstan_example.rds
/usr/lib64/R/library/broom.mixed/extdata/rstanarm_example.rds
/usr/lib64/R/library/broom.mixed/help/AnIndex
/usr/lib64/R/library/broom.mixed/help/aliases.rds
/usr/lib64/R/library/broom.mixed/help/broom.mixed.rdb
/usr/lib64/R/library/broom.mixed/help/broom.mixed.rdx
/usr/lib64/R/library/broom.mixed/help/paths.rds
/usr/lib64/R/library/broom.mixed/html/00Index.html
/usr/lib64/R/library/broom.mixed/html/R.css
/usr/lib64/R/library/broom.mixed/tests/test-all.R
/usr/lib64/R/library/broom.mixed/tests/testthat/helper-checkers.R
/usr/lib64/R/library/broom.mixed/tests/testthat/test-TMB.R
/usr/lib64/R/library/broom.mixed/tests/testthat/test-alltibbles.R
/usr/lib64/R/library/broom.mixed/tests/testthat/test-brms.R
/usr/lib64/R/library/broom.mixed/tests/testthat/test-gamlss.R
/usr/lib64/R/library/broom.mixed/tests/testthat/test-glmmTMB.R
/usr/lib64/R/library/broom.mixed/tests/testthat/test-lme4.R
/usr/lib64/R/library/broom.mixed/tests/testthat/test-lmertest.R
/usr/lib64/R/library/broom.mixed/tests/testthat/test-mcmc.R
/usr/lib64/R/library/broom.mixed/tests/testthat/test-nlme.R
/usr/lib64/R/library/broom.mixed/tests/testthat/test-rstanarm.R
