Ext.define("YourTable.view.Main", {
	extend: 'Ext.tab.Panel',
	requires: ['Ext.TitleBar'],

	config: {
		tabBarPosition: 'bottom',
		items: [
			{
				title: 'Add Receipt',
				id: 'addReceiptTab',
				iconCls: 'compose',
				layout: 'card',
				items: [
					{
						scrollable: true,
						styleHtmlContent: true,
						items: [
							{
								docked: 'top',
								xtype: 'titlebar',
								title: 'Record your Receipt'
							},
							{
								xtype: 'button',
								text: 'Upload a Picture',
								id: 'takePicture',
								ui: 'action',
								iconCls: 'action',
								iconMask: true,
								padding: 10,
								margin: 10
							},
							{
								xtype: 'button',
								text: 'Enter Receipt Info',
								id: 'enterReceipt',
								ui: 'action',
								iconCls: 'compose',
								iconMask: true,
								padding: 10,
								margin: 10,
								items: [{ xtype: "receiptPanel" }]
							}
						]
					}
				]
			},
			{
				title: 'History',
				iconCls: 'maps',
				items: [
					{
						docked: 'top',
						xtype: 'titlebar',
						title: 'See dining history'
					}
				]
			},
			{
				title: 'Account',
				iconCls: 'user',
				items: [
					{
						docked: 'top',
						xtype: 'titlebar',
						title: 'Manage Account'
					}
				]
			},
			{
				title: 'Settings',
				iconCls: 'settings',
				items: [
					{
						docked: 'top',
						xtype: 'titlebar',
						title: 'Change Settings'
					}
				]
			}
		]
	}
});
