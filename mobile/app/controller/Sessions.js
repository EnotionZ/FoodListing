Ext.define('YourTable.controller.Sessions', {
	extend: 'Ext.app.Controller',

	config: {
		refs: {
			takePictureBtn: '#takePicture',
			enterReceiptBtn: '#enterReceipt',
			loginForm: 'formpanel'
		},
		control: {
			'#takePicture': {
				tap: 'doTakePicture'
			},
			'#enterReceipt': {
				tap: 'doEnterReceipt'
			}
		}
	},

	doTakePicture: function() {
		Ext.device.Camera.capture({
			success: function(image) {
				//imageView.setSrc(image);
			},
			quality: 75,
			width: 200,
			height: 200,
			destination: 'data'
		});
	},

	doEnterReceipt: function() {
		alert("enter receipt");
	},

	doLogin: function() {
		var form   = this.getLoginForm(),
		values = form.getValues();

		MyApp.authenticate(values);
	}
});
