Ext.define("YourTable.view.AddCard", {
	extend: "Ext.Panel",
	config: {
		styleHtmlContent: true,
		items: [
			{
				xtype: 'fieldset',
				title: 'Add Food Item',
				instructions: 'Please enter the information above.',
				defaults: {
					required: true,
					labelAlign: 'left',
					labelWidth: '40%'
				},
				items: [
					{
						xtype: 'textfield',
						name: 'name',
						label: 'Item Name',
						autoCapitalize: false
					},
					{
						xtype: 'spinnerfield',
						name: 'spinner',
						label: 'Quantity',
						increment: 1,
						minValue: 1
					},
					{
						xtype: 'textfield',
						name: 'name',
						label: 'Cost',
						autoCapitalize: false
					},
					{
						id: "addFoodEntry",
						xtype: 'button',
						text: 'Save',
						margin: 10
					}
				]
			}
		],
		fullscreen: true
	}
});
