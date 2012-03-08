Ext.define("YourTable.view.Receipt", {
	extend: "Ext.Panel",
	xtype: "receiptPanel",
	config: {
		styleHtmlContent: true,
		items: [
			{
				docked: 'top',
				xtype: 'toolbar',
				items: [
					{ ui: 'back', text: 'Back' },
					{ id: 'showAddCard', ui: 'round', text: 'Add Entry' }
				]
			}
		],
		fullscreen: true
	}
});
