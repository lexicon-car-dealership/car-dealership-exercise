document.addEventListener('DOMContentLoaded', function () {
  // const filterForm = document.getElementById('filter_form');
  // const searchInput = document.getElementById('filter_form_search');

  // searchInput.addEventListener('keypress', function (event) {
  //   if (event.key === 'Enter') {
  //     event.preventDefault();
  //     const urlParams = new URLSearchParams(new FormData(filterForm));
  //     const searchQuery = searchInput.value;
  //     urlParams.set('search', searchQuery);
  //     window.location.href = `${filterForm.action}?${urlParams.toString()}`;
  //   }
  // });
  //profile stuff
  const profileDropdown = document.getElementById('navbarDropdown');
  if (profileDropdown) {
    const menuBar = document.getElementById('menu-bar');
    profileDropdown.addEventListener('click', () => {
    menuBar.classList.toggle('active');
  })
  }
  //filters
  const filterButton = document.getElementById('filter-toggle');
  const navSearchFilters = document.getElementById('nav-search-filters');
  filterButton.addEventListener('click', (event) => {
    event.preventDefault();
    navSearchFilters.classList.toggle('active');
  })
});
