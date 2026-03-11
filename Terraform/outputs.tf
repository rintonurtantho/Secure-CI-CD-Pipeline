output "container_app_url" {
  value = azurerm_container_app.payments.latest_revision_fqdn
}


