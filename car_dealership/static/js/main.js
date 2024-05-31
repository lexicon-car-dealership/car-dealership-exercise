document.addEventListener('DOMContentLoaded', function () {
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
  const isFilterActive = window.localStorage.getItem('filtertab') === 'true';
  if(isFilterActive)
    navSearchFilters.classList.add('active')

  const headerElement = document.getElementById('header');
  filterButton.addEventListener('click', (event) => {
    event.preventDefault();
    const isFilterActive = navSearchFilters.classList.toggle('active');
    console.log('enter')
    window.localStorage.setItem('filtertab', isFilterActive);
    headerElement.style = isFilterActive ? 'grid-template-rows: 70px 50px' : '';
  })
  headerElement.style = isFilterActive ? 'grid-template-rows: 70px 50px' : '';
});
