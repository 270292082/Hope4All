// search function

document.addEventListener('DOMContentLoaded', function()
{
    // get search bar and dropdown from index.html
    const searchInput = document.getElementById('live-search');
    const dropdown = document.getElementById('search-dropdown');

    // if there is no input or dropdown search result, exit (defence)
    if(!searchInput || !dropdown) return;

    // dropdown- fetch and display results
    searchInput.addEventListener('input', function()
    {
        const query = this.value.trim();
        // if input is empty
        if (query.length === 0)
        {
            dropdown.innerHTML = '';
            dropdown.style.display = 'none';
            return;
        }

        // fetch matching results from backend as JSON
        fetch(`/search_json?query=${encodeURIComponent(query)}`)
            .then(response => response.json())
            .then(results => {
                if (results.length === 0)
                {   
                    // if not found any
                    dropdown.innerHTML = "<div class='dropdown-item>No results found.</div>";
                }
                else
                {
                    // display each result as clickable items
                    dropdown.innerHTML = results.map(item =>
                        `<div class= 'dropdown-item' data-mid = "${item.MID}">${item.FirstName} ${item.LastName}, Age: ${item.Age}</div>`
                    ).join('');
                }
                dropdown.style.display = 'block';

                // attach click handler for navigation - for each dropdown item
                Array.from(dropdown.getElementsByClassName('dropdown-item')).forEach(function(elem)
                {
                    elem.addEventListener('click', function()
                    {
                        const mid = this.getAttribute('data-mid');

                        if (mid)
                        {
                            // redirect to viewing missing person information page
                            window.location.href = `/view/${mid}`
                        }
                    });
                });
            });
    });

    // to hide dropdown when input loses focus
    searchInput.addEventListener('blur', function()
    {
        setTimeout(() => {dropdown.style.display = 'none';}, 150);
    });

    // show dropdown when input regains focus - if there is result
    searchInput.addEventListener('focus', function()
    {
        if (dropdown.innerHTML.trim() !== '') dropdown.style.display = 'block';
    });


    // clear search on clicking anywhere in home page
    document.addEventListener('click', function(event)
	{
		// get form elements
		const searchForm = searchInput.closest('form');

		if (!searchForm.contains(event.target) && !dropdown.contains(event.target)) {
			searchInput.value = '';
			dropdown.style.display = 'none';
			dropdown.innerHTML = '';
		}
	});

    
    // clear on page reload/ back 
    window.addEventListener('pageshow', function()
    {
        searchInput.value = '';
        dropdown.innerHTML = '';
        dropdown.style.display = 'none';
    });
});