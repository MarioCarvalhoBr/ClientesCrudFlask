function confirmDelete(dataID) {
    // Configura o ID do cliente no botão de confirmação no modal
    var confirmBtn = document.getElementById('delete-confirm-btn');
    confirmBtn.onclick = function () {
        deleteData(dataID);
    };

    // Exibe o modal de confirmação
    var confirmModal = new bootstrap.Modal(document.getElementById('confirmDeleteModal'), {
        keyboard: false
    });
    confirmModal.show();
}

function createDataTable(table_name) {
    var produtosTable = new DataTable(table_name, {
        "responsive": true,
        "bJQueryUI": true,
        "autoWidth": false,
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'copy',
                text: 'Copiar'
            },
            {
                extend: 'csv',
                text: 'CSV'
            },
            {
                extend: 'excel',
                text: 'Excel'
            },
            {
                extend: 'pdf',
                text: 'PDF'
            },
            {
                extend: 'print',
                text: 'Imprimir'
            }
        ],
        language: {
            url: 'https://cdn.datatables.net/plug-ins/1.11.3/i18n/pt_br.json'
        }
    });

    // Set autoWidth como true
    produtosTable.columns.adjust().draw();

    return produtosTable;
}