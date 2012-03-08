Ext.define("YourTable.view.ReceiptItem", {
	//extend: "Ext.Container",
	xtype: "receiptPanel",
	config: {
		styleHtmlContent: true,
		items: [
			{
				layout: "hbox",
				items: [
					{ text: 'Item' },
					{ text: 'Qty' },
					{ text: 'Price' }
				]
			}
		],
		fullscreen: true
	}
});
