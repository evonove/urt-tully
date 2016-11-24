$( document ).ready(function doPoll() {
	$.ajax({
		url: "https://tech-team-unipgracingteam.herokuapp.com",
		method: "GET",
		contentType: "application/json",
		dataType: "json"
	})
		.done(function( json ) {
			json = json.results[0]
			$( "#rpm" ).text(json.rpm);
			$( "#inj1" ).text(json.inj1);
			$( "#inj2" ).text(json.inj2);
			$( "#ign1" ).text(json.ign1);
			$( "#ign2" ).text(json.ign2);
			$( "#wtemp" ).text(json.wtemp);
			$( "#airtemp" ).text(json.airtemp);
			$( "#airp" ).text(json.airp);
			$( "#oilt" ).text(json.oilt);
			$( "#tps" ).text(json.tps);
			$( "#lambda_1" ).text(json.lambda_1);
			$( "#lambda_trg" ).text(json.lambda_trg);
			$( "#speed_fl" ).text(json.speed_fl);
			$( "#speed_fr" ).text(json.speed_fr);
			$( "#speed_rl" ).text(json.speed_rl);
			$( "#speed_rr" ).text(json.speed_rr);
			$( "#vbatt" ).text(json.vbatt);
			$( "#aux" ).text(json.aux);
			$( "#det" ).text(json.det);
			$( "#fcmp" ).text(json.fcmp);
			$( "#ecu_error" ).text(json.ecu_error);
			$( "#fpga_error" ).text(json.fpga_error);
			$( "#status" ).text(json.status);
			$( "#delta" ).text(json.delta);
			$( "#dwell" ).text(json.dwell);
			$( "#map_tc_sel" ).text(json.map_tc_sel);
			$( "#slpf_fl" ).text(json.slpf_fl);
			$( "#slpf_fr" ).text(json.slpf_fr);
			$( "#slpf_rl" ).text(json.slpf_rl);
			$( "#slpf_rr" ).text(json.slpf_rr);
			$( "#cutoff" ).text(json.cutoff);
			$( "#time" ).text(json.time);
			$( "#aux_data1" ).text(json.aux_data1);
			$( "#aux_data2" ).text(json.aux_data2);
			$( "#aux_data3" ).text(json.aux_data3);
			$( "#aux_data4" ).text(json.aux_data4);
			$( "#aux_data5" ).text(json.aux_data5);
			$( "#aux_data6" ).text(json.aux_data6);
			$( "#aux_data7" ).text(json.aux_data7);
			$( "#aux_data8" ).text(json.aux_data8);
			$( "#aux_data9" ).text(json.aux_data9);
			$( "#aux_data10" ).text(json.aux_data10);
			$( "#aux_data11" ).text(json.aux_data11);
			$( "#aux_data12" ).text(json.aux_data12);
			$( "#aux_data13" ).text(json.aux_data13);
			$( "#aux_data14" ).text(json.aux_data14);
			$( "#aux_data15" ).text(json.aux_data15);
			$( "#aux_data16" ).text(json.aux_data16);
			$( "#aux_data17" ).text(json.aux_data17);
			$( "#aux_data18" ).text(json.aux_data18);
			$( "#aux_data19" ).text(json.aux_data19);
			$( "#aux_data20" ).text(json.aux_data20);
			$( "#aux_data21" ).text(json.aux_data21);
			$( "#aux_data22" ).text(json.aux_data22);
			$( "#aux_data23" ).text(json.aux_data23);
			$( "#aux_data24" ).text(json.aux_data24);
			$( "#aux_data25" ).text(json.aux_data25);
			$( "#aux_data26" ).text(json.aux_data26);
			$( "#aux_data27" ).text(json.aux_data27);
			$( "#aux_data28" ).text(json.aux_data28);
			$( "#aux_data29" ).text(json.aux_data29);
			$( "#aux_data30" ).text(json.aux_data30);
			$( "#aux_data31" ).text(json.aux_data31);
			$( "#aux_data32" ).text(json.aux_data32);
		})

			.fail(function( xhr, status, errorThrown ) {
    		console.log( "Error: " + errorThrown );
    		console.log( "Status: " + status );
    		console.dir( xhr );
  })
			setTimeout(doPoll,500);
});