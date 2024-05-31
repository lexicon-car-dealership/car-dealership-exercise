document.addEventListener('DOMContentLoaded', function () {
  const profileDropdown = document.getElementById('navbarDropdown');
  if (profileDropdown) {
    const menuBar = document.getElementById('menu-bar');
    profileDropdown.addEventListener('click', () => {
      menuBar.classList.toggle('active');
    });
  }
  //filters
  const filterButton = document.getElementById('filter-toggle');
  const navSearchFilters = document.getElementById('nav-search-filters');
  const isFilterActive = window.localStorage.getItem('filtertab') === 'true';
  if (isFilterActive) navSearchFilters.classList.add('active');

  filterButton.addEventListener('click', event => {
    event.preventDefault();
    const isFilterActive = navSearchFilters.classList.toggle('active');
    window.localStorage.setItem('filtertab', isFilterActive);
  });
});
