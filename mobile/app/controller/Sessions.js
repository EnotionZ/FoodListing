Ext.define('YourTable.controller.Sessions', {
	extend: 'Ext.app.Controller',

	config: {
		refs: {
			takePictureBtn: '#takePicture',
			enterReceiptBtn: '#enterReceipt',
			tab: "#addReceiptTab",
			loginForm: 'formpanel'
		},
		control: {
			'#takePicture': { tap: 'doTakePicture' },
			'#enterReceipt': { tap: 'doEnterReceipt' },
			'#showAddCard': { tap: 'showAddCard' },
			'#addFoodEntry': { tap: 'addFoodEntry' }
		}
	},

	addFoodEntry: function() {
		alert("adding food entry");
		this.getTab().setActiveItem(this.ReceiptView);
	},

	showAddCard: function() {
		if(!this.AddCard) {
			this.AddCard = Ext.create("YourTable.view.AddCard");
			this.getTab().add(this.AddCard);
		}
		this.getTab().setActiveItem(this.AddCard);
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
		if(!this.ReceiptView) {
			this.ReceiptView = Ext.create("YourTable.view.Receipt");
			this.getTab().add(this.ReceiptView);
		}
		this.getTab().setActiveItem(this.ReceiptView);
	},

	doLogin: function() {
		var form   = this.getLoginForm(),
		values = form.getValues();

		MyApp.authenticate(values);
	}
});
