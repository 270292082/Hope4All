// language function

document.addEventListener('DOMContentLoaded', function()
{
    const languageImg = document.getElementById('openLanguageSelection');
    const selection = document.getElementById('languageSelection');

    if(languageImg && selection)
    {
        languageImg.addEventListener('click', function(event) {
            selection.style.display = selection.style.display == 'block' ? 'none' : 'block';
            event.stopPropagation();
        });

        // hide popup when clicked anywhere
        document.addEventListener('click', function() {
            selection.style.display = 'none';
        });

        // prevent pop up selection from closing when selected
        selection.addEventListener('click', function(event) {
            event.stopPropagation();
        });

        // reload to prevent language change error
        //selection.querySelectorAll('.language-selection a').forEach(function(a) {
            //a.addEventListener('click', function(e) {
                //e.preventDefault();
                //window.location.href = this.href;
            //});
        //});
    }
});