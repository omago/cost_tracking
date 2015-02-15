$(document).ready(function() {

    $('select[name=cost_category]').change(function(){
        var cost_category = $(this).val();
        $('select[name=cost_subcategory] option:gt(0)').remove();
        $.ajax({
            type: "GET",
            url: "/cost-subcategory/get-json-list/",
            data: {
              "category_id": cost_category
            },
            dataType: "json",
            success: function(subcategories) {
                var cost_subcategory = $('select[name=cost_subcategory]');

                $.each(subcategories, function(index, element) {
                    cost_subcategory.append("<option value=" + element.pk + ">" + element.fields.name + "</option>")
                });
            }
        });
    });

    $('select[name=cost_category_multiple]').change(function(){
        var cost_category = $(this).val();
        $('select[name=cost_subcategory_multiple] option').remove();
        $.ajax({
            type: "GET",
            url: "/cost-subcategory/get-json-list/",
            data: {
              "category_id": cost_category
            },
            dataType: "json",
            success: function(subcategories) {
                var cost_subcategory = $('select[name=cost_subcategory_multiple]');

                $.each(subcategories, function(index, element) {
                    cost_subcategory.append("<option value=" + element.pk + ">" + element.fields.name + "</option>")
                });
            }
        });
    });

    $(".open-next-div").click(function() {
        var parent = $(this).parent();
        var parent_class = parent.attr('class');

        if(parent_class == "open") {
            parent.removeClass("open");
            $(this).parent().next().hide();
        } else {
            parent.addClass("open");
            $(this).parent().next().show();
        }
    });

    $(".date").datepicker({ dateFormat: 'yy-mm-dd' });
    $(".datetime").datetimepicker({
        dateFormat: "yy-mm-dd",
        timeFormat: "hh:mm:ss",
        timeText: 'Vrijeme',
        hourText: 'Sati',
        minuteText: 'Minute',
        secondText: 'Sekunde',
        currentText: 'Sada',
        closeText: 'Završi',
        dayNames: ['Nedjelja','Ponedjeljak','Utorak','Srijeda','Četvrtak','Petak','Subota'],
        dayNamesShort: ['Ned','Pon','Uto','Sri','Čet','Pet','Sub'],
        dayNamesMin: ['Ned','Pon','Uto','Sri','Čet','Pet','Sub'],
        monthNames: ['Siječanj','Veljača','Ožujak','Travanj','Svibanj','Lipanj','Srpanj','Kolovoz','Rujan','Listopad','Studeni','Prosinac'],
        firstDay: 1
    });

    $(".grid .delete").click(function() {
        var entry_name  = $(this).parent().parent().children("td:nth-child(2)").children().html();

        if(entry_name == null) {
            entry_name  = $(this).parent().parent().children("td:nth-child(2)").html();
        }

        var url = $(this).attr("href");
        $("body").append("<div id='dialog-confirm' title='Potvrda brisanja' class='error'>Jeste li sigurni da \u017eelite obrisati <b>" + entry_name + "</b>?</div>");

        $("#dialog-confirm").dialog({
			resizable: false,
			height:140,
			modal: true,
			buttons: {
				"Da, obri\u0161i zapis": function() {
					window.location = url;
				},
				"Ne, otka\u017ei": function() {
					$(this).dialog("close");
                    $("#dialog-confirm").remove();
				}
			}
		});

        return false;
    });

    $(".autocomplete").each(function() {
        var url = $(this).attr("rel");
        $(this).autocomplete({
            source: function( request, response ) {
                $.ajax({
                    url: url,
                    dataType: "json",
                    data: {
                        "cost_name": request.term,
                        "cost_category": $("#id_cost_category").val(),
                        "cost_subcategory": $("#id_cost_subcategory").val()
                    },
                    success: function(data) {
                        var response_json = [];
                        $.each(data, function (index, value) {
                            response_json.push({"value": value.fields.name, "id": value.pk})
                        });
                        response(response_json);
                    }
                });
            },
            minLength: 2,
            select: function(event,ui) {
                var id_field = $(this).attr("id").replace("_autocomplete", "")
                $("input[id=" + id_field + "]").val(ui.item.id);
            }
        });
    })
});
