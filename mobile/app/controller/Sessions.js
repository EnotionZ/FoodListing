Ext.define('YourTable.model.FoodItem', {
	extend: 'Ext.data.Model',

	config: {
		fields: [
			{ name: 'name',     type: 'string' },
			{ name: 'quantity', type: 'integer' },
			{ name: 'cost',    type: 'integer' }
		]
	}
});

Ext.define('YourTable.controller.Sessions', {
	extend: 'Ext.app.Controller',

	config: {
		refs: {
			takePictureBtn: '#takePicture',
			enterReceiptBtn: '#enterReceipt',
			tab: "#addReceiptTab",
			listing: "#foodItemListing"
		},
		control: {
			'#takePicture': { tap: 'doTakePicture' },
			'#enterReceipt': { tap: 'doEnterReceipt' },
			'#showAddCard': { tap: 'showAddCard' },
			'#addFoodEntry': { tap: 'addFoodEntry' }
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

	addFoodEntry: function() {
		this.getTab().setActiveItem(this.ReceiptView);
		//this.ReceiptView.add(Ext.create('YourTable.view.ReceiptItem'));
		this.ReceiptView.add({html: "new item"});
	},

	showAddCard: function() {
		if(!this.AddCard) {
			this.AddCard = Ext.create("YourTable.view.AddCard");
			this.getTab().add(this.AddCard);
		}
		this.getTab().setActiveItem(this.AddCard);
	},

	doEnterReceipt: function() {
		if(!this.ReceiptView) {
			this.ReceiptView = Ext.create("YourTable.view.Receipt");
			this.getTab().add(this.ReceiptView);
		}
		this.getTab().setActiveItem(this.ReceiptView);
	}

});
