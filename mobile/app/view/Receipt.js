Ext.define("YourTable.view.Receipt", {
	extend: "Ext.Panel",
	xtype: "receiptPanel",
	config: {
		styleHtmlContent: true,
		items: [
			{
				docked: 'top',
				xtype: 'titlebar',
				title: 'Enter Receipt Info'
			}
		],
		initialize: function() {
			this.callParent(arguments);
		},
		fullscreen: true
	}
});
