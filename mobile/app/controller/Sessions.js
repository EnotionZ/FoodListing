Ext.define('YourTable.controller.Sessions', {
	extend: 'Ext.app.Controller',

	config: {
		refs: {
			takePictureBtn: '#takePicture',
			enterReceiptBtn: '#enterReceipt',
			receiptTab: "#addReceiptTab",
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
				alert("fsdfsdfds");
				//imageView.setSrc(image);
			},
			quality: 75,
			width: 200,
			height: 200,
			destination: 'data'
		});
	},

	doEnterReceipt: function() {
		if(!this.ReceiptView) this.ReceiptView = Ext.create("YourTable.view.Receipt");
		debugger;
		this.getReceiptTab().removeAll();
		this.getReceiptTab().add(this.ReceiptView);
	},

	doLogin: function() {
		var form   = this.getLoginForm(),
		values = form.getValues();

		MyApp.authenticate(values);
	}
});
