
function get_language()
{
	return location.pathname.split('/')[1];
}

function setup_select_handler()
{
	$('#select-list').change(function() {

		document.location.href = '/' + get_language() + '/' + $(this).val();
	});
}

function setup_checkbox_handlers()
{
	list_items = $('.list-item')
	
	//list_items.find('input').off('click');

	list_items.click(function(event) {

		div_clicked = true;
		if ($(event.target).closest('input[type="checkbox"]').length > 0)
			div_clicked = false;

		checkbox = $(this);

		tag = checkbox.prop('tagName');
		is_input = true;
		if (tag != 'INPUT') {
			checkbox = checkbox.find('input');
		}

		console.log('wtf: "' + typeof(checkbox.prop('checked')) + ' ' + (checkbox.prop('checked') === true));
		list_slug = checkbox.data('list-slug');
		item_slug = checkbox.data('item-slug');

		/* Why the hell do we have to inverse the logic when the checkbox is clicked directly? */
		item_done = checkbox.prop('checked') === div_clicked ? 0 : 1;

		url = '/' + get_language() + '/' + list_slug + '/' + item_slug + '/mark-done/' + item_done + '/';

		$.ajax({
			url: url,
			success: function(response) {
				if (response['status'] != 0)
					alert('Failed to mark item as done');
				else
					checkbox.prop('checked', !checkbox.prop('checked'));
			},
			error: function() {
				alert('Failed to mark item as done');
			},
		});

		event.preventDefault();
		event.stopPropagation();
	});
}

$(document).ready(function() {

	setup_select_handler();

	setup_checkbox_handlers();
});
