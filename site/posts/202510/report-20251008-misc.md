---
date: '2025-10-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7e5f65d...MicrosoftDocs:fa0a155
summary: この更新により、個人情報（PII）に関連するエンティティカテゴリのリストが最新の状態に保たれ、情報の一貫性が向上しました。また、Azure AI言語サービスの目次ファイルも更新され、新しいトピックが追加され、AI技術を利用する際のドキュメントの信頼性とアクセシビリティが向上しました。新機能として、PIIエンティティに関する更新が行われ、さらに目次にも新しいAI関連トピックが追加されました。これは、ユーザーエクスペリエンスの向上と情報のアクセス性を高める目的があります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7e5f65d...MicrosoftDocs:fa0a155){target="_blank"}

# ハイライト

この更新により、個人情報（PII）に関連するエンティティカテゴリのリストが最新の状態に保たれ、情報の一貫性が向上しました。また、Azure AI言語サービスの目次ファイルが更新され、新しいトピックが追加されました。これにより、AI技術を利用する際のドキュメントの信頼性とアクセシビリティが向上しました。

## 新機能

- エンティティカテゴリリストが最新のPIIエンティティを反映するように更新。

## 破壊的変更

- 特に報告されていません。

## その他の更新

- `entity-categories-list.md`と`entity-categories.md`の表が整理され、情報が見やすくなりました。
- `toc.yml`に新しいAI関連トピックが追加され、ドキュメントの一貫性が強化されました。

# インサイト

エンティティカテゴリの更新では、個人情報（PII）に関するドキュメントの品質と正確性を高めることが目的です。この更新により、PIIエンティティを扱う全てのステークホルダーにとって、より一貫性のある、わかりやすい情報提供ができるようになっています。具体的には、エントリの並びや細かい名称の統一が行われ、例えば「ABA Routing Number」が「American Bankers Association Routing Number」という正式名称に変更されました。

さらに、目次ファイルの更新では、Azure AI言語サービスに関連する新たなトピックが追加され、ユーザーがアクセスしやすい構造になっています。特に「会話型言語理解」や「カスタム質問応答」などの追加により、ユーザーはこれまで以上に幅広い機能を利用することが可能になりました。また、「責任あるAIの使用」に関する新しい項目が導入され、AI技術の倫理的な利用を推進しています。

この一連のアップデートは、AI技術の継続的な進歩とそれに伴うユーザーエクスペリエンスの向上を示しています。特に、透明性とデータ保護に関するガイダンスは、AIを利用する上での安心感をユーザーに提供します。ドキュメントの改良により、情報のアクセスしやすさが向上し、利便性も高められています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [entity-categories-list.md](#item-05522d) | minor update | エンティティカテゴリリストの更新 | modified | 3 | 4 | 7 | 
| [entity-categories.md](#item-ba2623) | minor update | エンティティカテゴリの内容更新 | modified | 446 | 446 | 892 | 
| [toc.yml](#item-12f1f0) | minor update | 目次ファイルの更新 | modified | 256 | 243 | 499 | 


# Modified Contents
## articles/ai-services/language-service/personally-identifiable-information/concepts/entity-categories-list.md{#item-05522d}

<details>
<summary>Diff</summary>
````diff
@@ -15,9 +15,9 @@ ms.custom:
 
 # Recognized PII entities list
 
-| Entity | Entity | Entity |
+| Entity | Entity | Entity|
 |--|--|--|
-| [ABA Routing Number](entity-categories.md#type-aba-routing-number) | [Address](entity-categories.md#type-address) | [Age](entity-categories.md#type-age) |
+|[Address](entity-categories.md#type-address)| [Age](entity-categories.md#type-age) | [American Bankers Association Routing Number](entity-categories.md#type-american-bankers-association-routing-number) |
 | [Argentina National Identity Number](entity-categories.md#type-argentina-national-identity-number) | [Australia Bank Account Number](entity-categories.md#type-australia-bank-account-number) | [Australia Business Number](entity-categories.md#type-australia-business-number) |
 | [Australia Company Number](entity-categories.md#type-australia-company-number) | [Australia Drivers License Number](entity-categories.md#type-australia-drivers-license-number) | [Australia Medical Account Number](entity-categories.md#type-australia-medical-account-number) |
 | [Australia Passport Number](entity-categories.md#type-australia-passport-number) | [Australia Tax File Number](entity-categories.md#type-australia-tax-file-number) | [Austria Identity Card](entity-categories.md#type-austria-identity-card) |
@@ -72,5 +72,4 @@ ms.custom:
 | [United Kingdom National Health Number](entity-categories.md#type-united-kingdom-national-health-number) | [United Kingdom National Insurance Number](entity-categories.md#type-united-kingdom-national-insurance-number) | [United Kingdom Unique Taxpayer Number](entity-categories.md#type-united-kingdom-unique-taxpayer-number) |
 | [United States Bank Account Number](entity-categories.md#type-united-states-bank-account-number) | [United States Drivers License Number](entity-categories.md#type-united-states-drivers-license-number) | [United States Drug Enforcement Agency Number](entity-categories.md#type-united-states-drug-enforcement-agency-number) |
 | [United States Individual Taxpayer Identification](entity-categories.md#type-united-states-individual-taxpayer-identification) | [United States Social Security Number](entity-categories.md#type-united-states-social-security-number) | [United States/United Kingdom Passport Number](entity-categories.md#type-united-statesunited-kingdom-passport-number) |
-| [URL](entity-categories.md#type-url) | [VIN 🆕](entity-categories.md#type-vin-preview) |  |
-
+| [URL](entity-categories.md#type-url) | [VIN 🆕](entity-categories.md#type-vin-preview) |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンティティカテゴリリストの更新"
}
```

### Explanation
この変更では、`entity-categories-list.md`ファイルにおいて、個人的に識別可能な情報（PII）エンティティに関連する表が更新されました。具体的には、エンティティのテーブル構造がわずかに調整され、エントリ間のスペースが削除され、テーブルの整合性が向上しました。これにより、視覚的に整然とした印象を与え、情報の読みやすさが改善されています。

また、一部のエンティティが追加・削除されており、特に「アメリカ銀行口座番号」や「アメリカ個人納税者識別番号」などの項目が明確に記載されています。この更新により、PIIエンティティに関する情報が最新かつでも整理され、文書全体の整合性と信頼性を高めています。

## articles/ai-services/language-service/personally-identifiable-information/concepts/entity-categories.md{#item-ba2623}

<details>
<summary>Diff</summary>
````diff
@@ -52,7 +52,7 @@ The Azure Language PII extraction API uses Natural Language Processing (NLP) tec
 
 ## Personal
 
-Any data, collected or stored, that can be used to identify or contact a specific individual is considered personal information. This may include information that identifies someone directly, such as their name or social security number. It can also refer to data that, when linked with other information, could lead to identification—for example, an address or dates of birth.).
+Any data, collected or stored, that can be used to identify or contact a specific individual is considered personal information. This data may include information that identifies someone directly, such as their name or social security number. It can also refer to data that, when linked with other information, could lead to identification—for example, an address or dates of birth.).
 
 ### Type: Address
 
@@ -131,11 +131,11 @@ Any data, collected or stored, that can be used to identify or contact a specifi
 Any financial information is connected to a particular individual that can, through identifying details, be traced back to that person. 
 
 
-### Type: ABA Routing Number
+### Type: American Bankers Association Routing Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|American Bankers Association (ABA)|To retrieve this entity type, specify **ABARoutingNumber** in the **piiCategories** request parameter. If **ABARoutingNumber** is detected, It appears in the **PII** response payload.|[ABARoutingNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **ABARoutingNumber** in the **piiCategories** request parameter. If **ABARoutingNumber** is detected, It appears in the **PII** response payload.|[ABARoutingNumber]|
 
 ### Type: Bank Account Number (preview) 
 
@@ -193,63 +193,63 @@ Any identifiable Azure information like authentication information and connectio
 
 ### Type: Azure Document DB Auth Key
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Microsoft|To retrieve this entity type, specify **AzureDocumentDBAuthKey** in the **piiCategories** request parameter. If **AzureDocumentDBAuthKey** is detected, It appears in the **PII** response payload.|[AzureDocumentDBAuthKey]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **AzureDocumentDBAuthKey** in the **piiCategories** request parameter. If **AzureDocumentDBAuthKey** is detected, It appears in the **PII** response payload.|[AzureDocumentDBAuthKey]|
 
 ### Type: Azure IAAS Database Connection And SQL String
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Microsoft|To retrieve this entity type, specify **AzureIAASDatabaseConnectionAndSQLString** in the **piiCategories** request parameter. If **AzureIAASDatabaseConnectionAndSQLString** is detected, It appears in the **PII** response payload.|[AzureIAASDatabaseConnectionAndSQLString]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **AzureIAASDatabaseConnectionAndSQLString** in the **piiCategories** request parameter. If **AzureIAASDatabaseConnectionAndSQLString** is detected, It appears in the **PII** response payload.|[AzureIAASDatabaseConnectionAndSQLString]|
 
 ### Type: Azure IoT Connection String
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Microsoft|To retrieve this entity type, specify **AzureIoTConnectionString** in the **piiCategories** request parameter. If **AzureIoTConnectionString** is detected, It appears in the **PII** response payload.|[AzureIoTConnectionString]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **AzureIoTConnectionString** in the **piiCategories** request parameter. If **AzureIoTConnectionString** is detected, It appears in the **PII** response payload.|[AzureIoTConnectionString]|
 
 ### Type: Azure Publish Setting Password
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Microsoft|To retrieve this entity type, specify **AzurePublishSettingPassword** in the **piiCategories** request parameter. If **AzurePublishSettingPassword** is detected, It appears in the **PII** response payload.|[AzurePublishSettingPassword]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **AzurePublishSettingPassword** in the **piiCategories** request parameter. If **AzurePublishSettingPassword** is detected, It appears in the **PII** response payload.|[AzurePublishSettingPassword]|
 
 ### Type: Azure Redis Cache String
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Microsoft|To retrieve this entity type, specify **AzureRedisCacheString** in the **piiCategories** request parameter. If **AzureRedisCacheString** is detected, It appears in the **PII** response payload.|[AzureRedisCacheString]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **AzureRedisCacheString** in the **piiCategories** request parameter. If **AzureRedisCacheString** is detected, It appears in the **PII** response payload.|[AzureRedisCacheString]|
 
 ### Type: Azure SAS
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Microsoft|To retrieve this entity type, specify **AzureSAS** in the **piiCategories** request parameter. If **AzureSAS** is detected, It appears in the **PII** response payload.|[AzureSAS]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **AzureSAS** in the **piiCategories** request parameter. If **AzureSAS** is detected, It appears in the **PII** response payload.|[AzureSAS]|
 
 ### Type: Azure Service Bus String
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Microsoft|To retrieve this entity type, specify **AzureServiceBusString** in the **piiCategories** request parameter. If **AzureServiceBusString** is detected, It appears in the **PII** response payload.|[AzureServiceBusString]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **AzureServiceBusString** in the **piiCategories** request parameter. If **AzureServiceBusString** is detected, It appears in the **PII** response payload.|[AzureServiceBusString]|
 
 ### Type: Azure Storage Account Generic
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Microsoft|To retrieve this entity type, specify **AzureStorageAccountGeneric** in the **piiCategories** request parameter. If **AzureStorageAccountGeneric** is detected, It appears in the **PII** response payload.|[AzureStorageAccountGeneric]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **AzureStorageAccountGeneric** in the **piiCategories** request parameter. If **AzureStorageAccountGeneric** is detected, It appears in the **PII** response payload.|[AzureStorageAccountGeneric]|
 
 ### Type: Azure Storage Account Key
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Microsoft|To retrieve this entity type, specify **AzureStorageAccountKey** in the **piiCategories** request parameter. If **AzureStorageAccountKey** is detected, It appears in the **PII** response payload.|[AzureStorageAccountKey]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **AzureStorageAccountKey** in the **piiCategories** request parameter. If **AzureStorageAccountKey** is detected, It appears in the **PII** response payload.|[AzureStorageAccountKey]|
 
 ### Type: SQL Server Connection String
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Microsoft|To retrieve this entity type, specify **SQLServerConnectionString** in the **piiCategories** request parameter. If **SQLServerConnectionString** is detected, It appears in the **PII** response payload.|[AzureStorageAccountKey]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **SQLServerConnectionString** in the **piiCategories** request parameter. If **SQLServerConnectionString** is detected, It appears in the **PII** response payload.|[AzureStorageAccountKey]|
 
 
 ## Government
@@ -258,827 +258,827 @@ Any government-issued identification that can be used along or combined with oth
 
 ### Type: Argentina National Identity Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Argentina|To retrieve this entity type, specify **ARNationalIdentityNumber** in the **piiCategories** request parameter. If **ARNationalIdentityNumber** is detected, It appears in the **PII** response payload.|[ARNationalIdentityNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **ARNationalIdentityNumber** in the **piiCategories** request parameter. If **ARNationalIdentityNumber** is detected, It appears in the **PII** response payload.|[ARNationalIdentityNumber]|
 
 ### Type: Australia Bank Account Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Australia|To retrieve this entity type, specify **AUBankAccountNumber** in the **piiCategories** request parameter. If **AUBankAccountNumber** is detected, It appears in the **PII** response payload.|[AUBankAccountNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **AUBankAccountNumber** in the **piiCategories** request parameter. If **AUBankAccountNumber** is detected, It appears in the **PII** response payload.|[AUBankAccountNumber]|
 
 ### Type: Australia Business Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Australia|To retrieve this entity type, specify **AUBusinessNumber** in the **piiCategories** request parameter. If **AUBusinessNumber** is detected, It appears in the **PII** response payload.|[AUBusinessNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **AUBusinessNumber** in the **piiCategories** request parameter. If **AUBusinessNumber** is detected, It appears in the **PII** response payload.|[AUBusinessNumber]|
 
 ### Type: Australia Company Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Australia|To retrieve this entity type, specify **AUCompanyNumber** in the **piiCategories** request parameter. If **AUCompanyNumber** is detected, It appears in the **PII** response payload.|[AUCompanyNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **AUCompanyNumber** in the **piiCategories** request parameter. If **AUCompanyNumber** is detected, It appears in the **PII** response payload.|[AUCompanyNumber]|
 
 ### Type: Australia Drivers License Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Australia|To retrieve this entity type, specify **AUDriversLicenseNumber** in the **piiCategories** request parameter. If **AUDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[AUDriversLicenseNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **AUDriversLicenseNumber** in the **piiCategories** request parameter. If **AUDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[AUDriversLicenseNumber]|
 
 ### Type: Australia Medical Account Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Australia|To retrieve this entity type, specify **AUMedicalAccountNumber** in the **piiCategories** request parameter. If **AUMedicalAccountNumber** is detected, It appears in the **PII** response payload.|[AUMedicalAccountNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **AUMedicalAccountNumber** in the **piiCategories** request parameter. If **AUMedicalAccountNumber** is detected, It appears in the **PII** response payload.|[AUMedicalAccountNumber]|
 
 ### Type: Australia Passport Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Australia|To retrieve this entity type, specify **AUPassportNumber** in the **piiCategories** request parameter. If **AUPassportNumber** is detected, It appears in the **PII** response payload.|[AUPassportNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **AUPassportNumber** in the **piiCategories** request parameter. If **AUPassportNumber** is detected, It appears in the **PII** response payload.|[AUPassportNumber]|
 
 ### Type: Australia Tax File Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Australia|To retrieve this entity type, specify **AUTaxFileNumber** in the **piiCategories** request parameter. If **AUTaxFileNumber** is detected, It appears in the **PII** response payload.|[AUTaxFileNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **AUTaxFileNumber** in the **piiCategories** request parameter. If **AUTaxFileNumber** is detected, It appears in the **PII** response payload.|[AUTaxFileNumber]|
 
 ### Type: Austria Identity Card
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Austria|To retrieve this entity type, specify **ATIdentityCard** in the **piiCategories** request parameter. If **ATIdentityCard** is detected, It appears in the **PII** response payload.|[ATIdentityCard]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **ATIdentityCard** in the **piiCategories** request parameter. If **ATIdentityCard** is detected, It appears in the **PII** response payload.|[ATIdentityCard]|
 
 ### Type: Austria Tax Identification Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Austria|To retrieve this entity type, specify **ATTaxIdentificationNumber** in the **piiCategories** request parameter. If **ATTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[ATTaxIdentificationNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **ATTaxIdentificationNumber** in the **piiCategories** request parameter. If **ATTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[ATTaxIdentificationNumber]|
 
 ### Type: Austria Value Added Tax Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Austria|To retrieve this entity type, specify **ATValueAddedTaxNumber** in the **piiCategories** request parameter. If **ATValueAddedTaxNumber** is detected, It appears in the **PII** response payload.|[ATValueAddedTaxNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **ATValueAddedTaxNumber** in the **piiCategories** request parameter. If **ATValueAddedTaxNumber** is detected, It appears in the **PII** response payload.|[ATValueAddedTaxNumber]|
 
 ### Type: Belgium National Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Belgium|To retrieve this entity type, specify **BENationalNumber** in the **piiCategories** request parameter. If **BENationalNumber** is detected, It appears in the **PII** response payload.|[BENationalNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **BENationalNumber** in the **piiCategories** request parameter. If **BENationalNumber** is detected, It appears in the **PII** response payload.|[BENationalNumber]|
 
 ### Type: Belgium Value Added Tax Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Belgium|To retrieve this entity type, specify **BEValueAddedTaxNumber** in the **piiCategories** request parameter. If **BEValueAddedTaxNumber** is detected, It appears in the **PII** response payload.|[BEValueAddedTaxNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **BEValueAddedTaxNumber** in the **piiCategories** request parameter. If **BEValueAddedTaxNumber** is detected, It appears in the **PII** response payload.|[BEValueAddedTaxNumber]|
 
 
 ### Type: Brazil CPF Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Brazil|To retrieve this entity type, specify **BRCPFNumber** in the **piiCategories** request parameter. If **BRCPFNumber** is detected, It appears in the **PII** response payload.|[BRCPFNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **BRCPFNumber** in the **piiCategories** request parameter. If **BRCPFNumber** is detected, It appears in the **PII** response payload.|[BRCPFNumber]|
 
 ### Type: Brazil Legal Entity Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Brazil|To retrieve this entity type, specify **BRLegalEntityNumber** in the **piiCategories** request parameter. If **BRLegalEntityNumber** is detected, It appears in the **PII** response payload.|[BRLegalEntityNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **BRLegalEntityNumber** in the **piiCategories** request parameter. If **BRLegalEntityNumber** is detected, It appears in the **PII** response payload.|[BRLegalEntityNumber]|
 
 ### Type: Brazil National IDRG
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Brazil|To retrieve this entity type, specify **BRNationalIDRG** in the **piiCategories** request parameter. If **BRNationalIDRG** is detected, It appears in the **PII** response payload.|[BRNationalIDRG]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **BRNationalIDRG** in the **piiCategories** request parameter. If **BRNationalIDRG** is detected, It appears in the **PII** response payload.|[BRNationalIDRG]|
 
 ### Type: Bulgaria Uniform Civil Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Bulgaria|To retrieve this entity type, specify **BGUniformCivilNumber** in the **piiCategories** request parameter. If **BGUniformCivilNumber** is detected, It appears in the **PII** response payload.|[BGUniformCivilNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **BGUniformCivilNumber** in the **piiCategories** request parameter. If **BGUniformCivilNumber** is detected, It appears in the **PII** response payload.|[BGUniformCivilNumber]|
 
 ### Type: Canada Bank Account Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Canada|To retrieve this entity type, specify **CABankAccountNumber** in the **piiCategories** request parameter. If **CABankAccountNumber** is detected, It appears in the **PII** response payload.|[CABankAccountNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **CABankAccountNumber** in the **piiCategories** request parameter. If **CABankAccountNumber** is detected, It appears in the **PII** response payload.|[CABankAccountNumber]|
 
 ### Type: Canada Drivers License Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Canada|To retrieve this entity type, specify **CADriversLicenseNumber** in the **piiCategories** request parameter. If **CADriversLicenseNumber** is detected, It appears in the **PII** response payload.|[CADriversLicenseNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **CADriversLicenseNumber** in the **piiCategories** request parameter. If **CADriversLicenseNumber** is detected, It appears in the **PII** response payload.|[CADriversLicenseNumber]|
 
 ### Type: Canada Health Service Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Canada|To retrieve this entity type, specify **CAHealthServiceNumber** in the **piiCategories** request parameter. If **CAHealthServiceNumber** is detected, It appears in the **PII** response payload.|[CAHealthServiceNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **CAHealthServiceNumber** in the **piiCategories** request parameter. If **CAHealthServiceNumber** is detected, It appears in the **PII** response payload.|[CAHealthServiceNumber]|
 
 ### Type: Canada Passport Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Canada|To retrieve this entity type, specify **CAPassportNumber** in the **piiCategories** request parameter. If **CAPassportNumber** is detected, It appears in the **PII** response payload.|[CAPassportNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **CAPassportNumber** in the **piiCategories** request parameter. If **CAPassportNumber** is detected, It appears in the **PII** response payload.|[CAPassportNumber]|
 
 ### Type: Canada Personal Health Identification
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Canada|To retrieve this entity type, specify **CAPersonalHealthIdentification** in the **piiCategories** request parameter. If **CAPersonalHealthIdentification** is detected, It appears in the **PII** and **PHI** response payload.|[CAPersonalHealthIdentification]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **CAPersonalHealthIdentification** in the **piiCategories** request parameter. If **CAPersonalHealthIdentification** is detected, It appears in the **PII** and **PHI** response payload.|[CAPersonalHealthIdentification]|
 
 ### Type: Canada Social Insurance Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Canada|To retrieve this entity type, specify **CASocialInsuranceNumber** in the **piiCategories** request parameter. If **CASocialInsuranceNumber** is detected, It appears in the **PII** response payload.|[CASocialInsuranceNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **CASocialInsuranceNumber** in the **piiCategories** request parameter. If **CASocialInsuranceNumber** is detected, It appears in the **PII** response payload.|[CASocialInsuranceNumber]|
 
 ### Type: Chile Identity Card Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Chile|To retrieve this entity type, specify **CLIdentityCardNumber** in the **piiCategories** request parameter. If **CLIdentityCardNumber** is detected, It appears in the **PII** response payload.|[CLIdentityCardNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **CLIdentityCardNumber** in the **piiCategories** request parameter. If **CLIdentityCardNumber** is detected, It appears in the **PII** response payload.|[CLIdentityCardNumber]|
 
 ### Type: China Resident Identity Card Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|China|To retrieve this entity type, specify **CNResidentIdentityCardNumber** in the **piiCategories** request parameter. If **CNResidentIdentityCardNumber** is detected, It appears in the **PII** response payload.|[CNResidentIdentityCardNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **CNResidentIdentityCardNumber** in the **piiCategories** request parameter. If **CNResidentIdentityCardNumber** is detected, It appears in the **PII** response payload.|[CNResidentIdentityCardNumber]|
 
 ### Type: Croatia Identity Card Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Croatia|To retrieve this entity type, specify **HRIdentityCardNumber** in the **piiCategories** request parameter. If **HRIdentityCardNumber** is detected, It appears in the **PII** response payload.|[HRIdentityCardNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **HRIdentityCardNumber** in the **piiCategories** request parameter. If **HRIdentityCardNumber** is detected, It appears in the **PII** response payload.|[HRIdentityCardNumber]|
 
 ### Type: Croatia National ID Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Croatia|To retrieve this entity type, specify **HRNationalIDNumber** in the **piiCategories** request parameter. If **HRNationalIDNumber** is detected, It appears in the **PII** response payload.|[HRNationalIDNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **HRNationalIDNumber** in the **piiCategories** request parameter. If **HRNationalIDNumber** is detected, It appears in the **PII** response payload.|[HRNationalIDNumber]|
 
 ### Type: Croatia Personal Identification Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Croatia|To retrieve this entity type, specify **HRPersonalIdentificationNumber** in the **piiCategories** request parameter. If **HRPersonalIdentificationNumber** is detected, It appears in the **PII** response payload.|[HRPersonalIdentificationNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **HRPersonalIdentificationNumber** in the **piiCategories** request parameter. If **HRPersonalIdentificationNumber** is detected, It appears in the **PII** response payload.|[HRPersonalIdentificationNumber]|
 
 ### Type: Cyprus Identity Card
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Cyprus|To retrieve this entity type, specify **CYIdentityCard** in the **piiCategories** request parameter. If **CYIdentityCard** is detected, It appears in the **PII** response payload.|[CYIdentityCard]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **CYIdentityCard** in the **piiCategories** request parameter. If **CYIdentityCard** is detected, It appears in the **PII** response payload.|[CYIdentityCard]|
 
 ### Type: Cyprus Tax Identification Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Cyprus|To retrieve this entity type, specify **CYTaxIdentificationNumber** in the **piiCategories** request parameter. If **CYTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[CYTaxIdentificationNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **CYTaxIdentificationNumber** in the **piiCategories** request parameter. If **CYTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[CYTaxIdentificationNumber]|
 
 ### Type: Czech Republic Personal Identity Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Czech Republic|To retrieve this entity type, specify **CZPersonalIdentityNumber** in the **piiCategories** request parameter. If **CZPersonalIdentityNumber** is detected, It appears in the **PII** response payload.|[CZPersonalIdentityNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **CZPersonalIdentityNumber** in the **piiCategories** request parameter. If **CZPersonalIdentityNumber** is detected, It appears in the **PII** response payload.|[CZPersonalIdentityNumber]|
 
 ### Type: Denmark Personal Identification Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Denmark|To retrieve this entity type, specify **DKPersonalIdentificationNumber** in the **piiCategories** request parameter. If **DKPersonalIdentificationNumber** is detected, It appears in the **PII** response payload.|[DKPersonalIdentificationNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **DKPersonalIdentificationNumber** in the **piiCategories** request parameter. If **DKPersonalIdentificationNumber** is detected, It appears in the **PII** response payload.|[DKPersonalIdentificationNumber]|
 
 ### Type: Estonia Personal Identification Code
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Estonia|To retrieve this entity type, specify **EEPersonalIdentificationCode** in the **piiCategories** request parameter. If **EEPersonalIdentificationCode** is detected, It appears in the **PII** response payload.|[EEPersonalIdentificationCode]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **EEPersonalIdentificationCode** in the **piiCategories** request parameter. If **EEPersonalIdentificationCode** is detected, It appears in the **PII** response payload.|[EEPersonalIdentificationCode]|
 
 ### Type: European Union Debit Card Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|European Union|To retrieve this entity type, specify **EUDebitCardNumber** in the **piiCategories** request parameter. If **EUDebitCardNumber** is detected, It appears in the **PII** response payload.|[EUDebitCardNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **EUDebitCardNumber** in the **piiCategories** request parameter. If **EUDebitCardNumber** is detected, It appears in the **PII** response payload.|[EUDebitCardNumber]|
 
 ### Type: European Union Drivers License Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|European Union|To retrieve this entity type, specify **EUDriversLicenseNumber** in the **piiCategories** request parameter. If **EUDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[EUDriversLicenseNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **EUDriversLicenseNumber** in the **piiCategories** request parameter. If **EUDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[EUDriversLicenseNumber]|
 
 ### Type: European Union GPS Coordinates
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|European Union|To retrieve this entity type, specify **EUGPSCoordinates** in the **piiCategories** request parameter. If **EUGPSCoordinates** is detected, It appears in the **PII** response payload.|[EUGPSCoordinates]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **EUGPSCoordinates** in the **piiCategories** request parameter. If **EUGPSCoordinates** is detected, It appears in the **PII** response payload.|[EUGPSCoordinates]|
 
 ### Type: European Union National Identification Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|European Union|To retrieve this entity type, specify **EUNationalIdentificationNumber** in the **piiCategories** request parameter. If **EUNationalIdentificationNumber** is detected, It appears in the **PII** response payload.|[EUNationalIdentificationNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **EUNationalIdentificationNumber** in the **piiCategories** request parameter. If **EUNationalIdentificationNumber** is detected, It appears in the **PII** response payload.|[EUNationalIdentificationNumber]|
 
 ### Type: European Union Passport Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|European Union|To retrieve this entity type, specify **EUPassportNumber** in the **piiCategories** request parameter. If **EUPassportNumber** is detected, It appears in the **PII** response payload.|[EUPassportNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **EUPassportNumber** in the **piiCategories** request parameter. If **EUPassportNumber** is detected, It appears in the **PII** response payload.|[EUPassportNumber]|
 
 ### Type: European Union Social Security Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|European Union|To retrieve this entity type, specify **EUSocialSecurityNumber** in the **piiCategories** request parameter. If **EUSocialSecurityNumber** is detected, It appears in the **PII** response payload.|[EUSocialSecurityNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **EUSocialSecurityNumber** in the **piiCategories** request parameter. If **EUSocialSecurityNumber** is detected, It appears in the **PII** response payload.|[EUSocialSecurityNumber]|
 
 ### Type: European Union Tax Identification Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|European Union|To retrieve this entity type, specify **EUTaxIdentificationNumber** in the **piiCategories** request parameter. If **EUTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[EUTaxIdentificationNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **EUTaxIdentificationNumber** in the **piiCategories** request parameter. If **EUTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[EUTaxIdentificationNumber]|
 
 ### Type: Finland European Health Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Finland|To retrieve this entity type, specify **FIEuropeanHealthNumber** in the **piiCategories** request parameter. If **FIEuropeanHealthNumber** is detected, It appears in the **PII** response payload.|[FIEuropeanHealthNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **FIEuropeanHealthNumber** in the **piiCategories** request parameter. If **FIEuropeanHealthNumber** is detected, It appears in the **PII** response payload.|[FIEuropeanHealthNumber]|
 
 ### Type: Finland National ID
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Finland|To retrieve this entity type, specify **FINationalID** in the **piiCategories** request parameter. If **FINationalID** is detected, It appears in the **PII** response payload.|[FINationalID]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **FINationalID** in the **piiCategories** request parameter. If **FINationalID** is detected, It appears in the **PII** response payload.|[FINationalID]|
 
 ### Type: Finland Passport Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Finland|To retrieve this entity type, specify **FIPassportNumber** in the **piiCategories** request parameter. If **FIPassportNumber** is detected, It appears in the **PII** response payload.|[FIPassportNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **FIPassportNumber** in the **piiCategories** request parameter. If **FIPassportNumber** is detected, It appears in the **PII** response payload.|[FIPassportNumber]|
 
 ### Type: France Drivers License Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|France|To retrieve this entity type, specify **FRDriversLicenseNumber** in the **piiCategories** request parameter. If **FRDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[FRDriversLicenseNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **FRDriversLicenseNumber** in the **piiCategories** request parameter. If **FRDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[FRDriversLicenseNumber]|
 
 ### Type: France Health Insurance Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|France|To retrieve this entity type, specify **FRHealthInsuranceNumber** in the **piiCategories** request parameter. If **FRHealthInsuranceNumber** is detected, It appears in the **PII** response payload.|[FRHealthInsuranceNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **FRHealthInsuranceNumber** in the **piiCategories** request parameter. If **FRHealthInsuranceNumber** is detected, It appears in the **PII** response payload.|[FRHealthInsuranceNumber]|
 
 ### Type: France National ID
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|France|To retrieve this entity type, specify **FRNationalID** in the **piiCategories** request parameter. If **FRNationalID** is detected, It appears in the **PII** response payload.|[FRNationalID]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **FRNationalID** in the **piiCategories** request parameter. If **FRNationalID** is detected, It appears in the **PII** response payload.|[FRNationalID]|
 
 ### Type: France Passport Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|France|To retrieve this entity type, specify **FRPassportNumber** in the **piiCategories** request parameter. If **FRPassportNumber** is detected, It appears in the **PII** response payload.|[FRPassportNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **FRPassportNumber** in the **piiCategories** request parameter. If **FRPassportNumber** is detected, It appears in the **PII** response payload.|[FRPassportNumber]|
 
 ### Type: France Social Security Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|France|To retrieve this entity type, specify **FRSocialSecurityNumber** in the **piiCategories** request parameter. If **FRSocialSecurityNumber** is detected, It appears in the **PII** response payload.|[FRSocialSecurityNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **FRSocialSecurityNumber** in the **piiCategories** request parameter. If **FRSocialSecurityNumber** is detected, It appears in the **PII** response payload.|[FRSocialSecurityNumber]|
 
 ### Type: France Tax Identification Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|France|To retrieve this entity type, specify **FRTaxIdentificationNumber** in the **piiCategories** request parameter. If **FRTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[FRTaxIdentificationNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **FRTaxIdentificationNumber** in the **piiCategories** request parameter. If **FRTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[FRTaxIdentificationNumber]|
 
 ### Type: France Value Added Tax Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|France|To retrieve this entity type, specify **FRValueAddedTaxNumber** in the **piiCategories** request parameter. If **FRValueAddedTaxNumber** is detected, It appears in the **PII** response payload.|[FRValueAddedTaxNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **FRValueAddedTaxNumber** in the **piiCategories** request parameter. If **FRValueAddedTaxNumber** is detected, It appears in the **PII** response payload.|[FRValueAddedTaxNumber]|
 
 ### Type: Germany Drivers License Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Germany|To retrieve this entity type, specify **DEDriversLicenseNumber** in the **piiCategories** request parameter. If **DEDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[DEDriversLicenseNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **DEDriversLicenseNumber** in the **piiCategories** request parameter. If **DEDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[DEDriversLicenseNumber]|
 
 ### Type: Germany Identity Card Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Germany|To retrieve this entity type, specify **DEIdentityCardNumber** in the **piiCategories** request parameter. If **DEIdentityCardNumber** is detected, It appears in the **PII** response payload.|[DEIdentityCardNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **DEIdentityCardNumber** in the **piiCategories** request parameter. If **DEIdentityCardNumber** is detected, It appears in the **PII** response payload.|[DEIdentityCardNumber]|
 
 ### Type: Germany Passport Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Germany|To retrieve this entity type, specify **DEPassportNumber** in the **piiCategories** request parameter. If **DEPassportNumber** is detected, It appears in the **PII** response payload.|[DEPassportNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **DEPassportNumber** in the **piiCategories** request parameter. If **DEPassportNumber** is detected, It appears in the **PII** response payload.|[DEPassportNumber]|
 
 ### Type: Germany Tax Identification Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Germany|To retrieve this entity type, specify **DETaxIdentificationNumber** in the **piiCategories** request parameter. If **DETaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[DETaxIdentificationNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **DETaxIdentificationNumber** in the **piiCategories** request parameter. If **DETaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[DETaxIdentificationNumber]|
 
 ### Type: Germany Value Added Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Germany|To retrieve this entity type, specify **DEValueAddedNumber** in the **piiCategories** request parameter. If **DEValueAddedNumber** is detected, It appears in the **PII** response payload.|[DEValueAddedNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **DEValueAddedNumber** in the **piiCategories** request parameter. If **DEValueAddedNumber** is detected, It appears in the **PII** response payload.|[DEValueAddedNumber]|
 
 ### Type: Greece National ID Card
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Greece|To retrieve this entity type, specify **GRNationalIDCard** in the **piiCategories** request parameter. If **GRNationalIDCard** is detected, It appears in the **PII** response payload.|[GRNationalIDCard]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **GRNationalIDCard** in the **piiCategories** request parameter. If **GRNationalIDCard** is detected, It appears in the **PII** response payload.|[GRNationalIDCard]|
 
 ### Type: Greece Tax Identification Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Greece|To retrieve this entity type, specify **GRTaxIdentificationNumber** in the **piiCategories** request parameter. If **GRTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[GRTaxIdentificationNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **GRTaxIdentificationNumber** in the **piiCategories** request parameter. If **GRTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[GRTaxIdentificationNumber]|
 
 ### Type: Hong Kong SAR Identity Card Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Hong Kong SAR|To retrieve this entity type, specify **HKIdentityCardNumber** in the **piiCategories** request parameter. If **HKIdentityCardNumber** is detected, It appears in the **PII** response payload.|[HKIdentityCardNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **HKIdentityCardNumber** in the **piiCategories** request parameter. If **HKIdentityCardNumber** is detected, It appears in the **PII** response payload.|[HKIdentityCardNumber]|
 
 ### Type: Hungary Personal Identification Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Hungary|To retrieve this entity type, specify **HUPersonalIdentificationNumber** in the **piiCategories** request parameter. If **HUPersonalIdentificationNumber** is detected, It appears in the **PII** response payload.|[HUPersonalIdentificationNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **HUPersonalIdentificationNumber** in the **piiCategories** request parameter. If **HUPersonalIdentificationNumber** is detected, It appears in the **PII** response payload.|[HUPersonalIdentificationNumber]|
 
 ### Type: Hungary Tax Identification Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Hungary|To retrieve this entity type, specify **HUTaxIdentificationNumber** in the **piiCategories** request parameter. If **HUTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[HUTaxIdentificationNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **HUTaxIdentificationNumber** in the **piiCategories** request parameter. If **HUTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[HUTaxIdentificationNumber]|
 
 ### Type: Hungary Value Added Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Hungary|To retrieve this entity type, specify **HUValueAddedNumber** in the **piiCategories** request parameter. If **HUValueAddedNumber** is detected, It appears in the **PII** response payload.|[HUValueAddedNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **HUValueAddedNumber** in the **piiCategories** request parameter. If **HUValueAddedNumber** is detected, It appears in the **PII** response payload.|[HUValueAddedNumber]|
 
 ### Type: India Permanent Account
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|India|To retrieve this entity type, specify **INPermanentAccount** in the **piiCategories** request parameter. If **INPermanentAccount** is detected, It appears in the **PII** response payload.|[INPermanentAccount]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **INPermanentAccount** in the **piiCategories** request parameter. If **INPermanentAccount** is detected, It appears in the **PII** response payload.|[INPermanentAccount]|
 
 ### Type: India Unique Identification Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|India|To retrieve this entity type, specify **INUniqueIdentificationNumber** in the **piiCategories** request parameter. If **INUniqueIdentificationNumber** is detected, It appears in the **PII** response payload.|[INUniqueIdentificationNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **INUniqueIdentificationNumber** in the **piiCategories** request parameter. If **INUniqueIdentificationNumber** is detected, It appears in the **PII** response payload.|[INUniqueIdentificationNumber]|
 
 ### Type: Indonesia Identity Card Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Indonesia|To retrieve this entity type, specify **IDIdentityCardNumber** in the **piiCategories** request parameter. If **IDIdentityCardNumber** is detected, It appears in the **PII** response payload.|[IDIdentityCardNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **IDIdentityCardNumber** in the **piiCategories** request parameter. If **IDIdentityCardNumber** is detected, It appears in the **PII** response payload.|[IDIdentityCardNumber]|
 
 ### Type: Ireland Personal Public Service Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Ireland|To retrieve this entity type, specify **IEPersonalPublicServiceNumber** in the **piiCategories** request parameter. If **IEPersonalPublicServiceNumber** is detected, It appears in the **PII** response payload.|[IEPersonalPublicServiceNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **IEPersonalPublicServiceNumber** in the **piiCategories** request parameter. If **IEPersonalPublicServiceNumber** is detected, It appears in the **PII** response payload.|[IEPersonalPublicServiceNumber]|
 
 ### Type: Israel Bank Account Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Israel|To retrieve this entity type, specify **ILBankAccountNumber** in the **piiCategories** request parameter. If **ILBankAccountNumber** is detected, It appears in the **PII** response payload.|[ILBankAccountNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **ILBankAccountNumber** in the **piiCategories** request parameter. If **ILBankAccountNumber** is detected, It appears in the **PII** response payload.|[ILBankAccountNumber]|
 
 ### Type: Israel National ID
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Israel|To retrieve this entity type, specify **ILNationalID** in the **piiCategories** request parameter. If **ILNationalID** is detected, It appears in the **PII** response payload.|[ILNationalID]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **ILNationalID** in the **piiCategories** request parameter. If **ILNationalID** is detected, It appears in the **PII** response payload.|[ILNationalID]|
 
 ### Type: Italy Drivers License Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Italy|To retrieve this entity type, specify **ITDriversLicenseNumber** in the **piiCategories** request parameter. If **ITDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[ITDriversLicenseNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **ITDriversLicenseNumber** in the **piiCategories** request parameter. If **ITDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[ITDriversLicenseNumber]|
 
 ### Type: Italy Fiscal Code
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Italy|To retrieve this entity type, specify **ITFiscalCode** in the **piiCategories** request parameter. If **ITFiscalCode** is detected, It appears in the **PII** response payload.|[ITFiscalCode]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **ITFiscalCode** in the **piiCategories** request parameter. If **ITFiscalCode** is detected, It appears in the **PII** response payload.|[ITFiscalCode]|
 
 ### Type: Italy Value Added Tax Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Italy|To retrieve this entity type, specify **ITValueAddedTaxNumber** in the **piiCategories** request parameter. If **ITValueAddedTaxNumber** is detected, It appears in the **PII** response payload.|[ITValueAddedTaxNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **ITValueAddedTaxNumber** in the **piiCategories** request parameter. If **ITValueAddedTaxNumber** is detected, It appears in the **PII** response payload.|[ITValueAddedTaxNumber]|
 
 ### Type: Japan Bank Account Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Japan|To retrieve this entity type, specify **JPBankAccountNumber** in the **piiCategories** request parameter. If **JPBankAccountNumber** is detected, It appears in the **PII** response payload.|[JPBankAccountNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **JPBankAccountNumber** in the **piiCategories** request parameter. If **JPBankAccountNumber** is detected, It appears in the **PII** response payload.|[JPBankAccountNumber]|
 
 ### Type: Japan Drivers License Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Japan|To retrieve this entity type, specify **JPDriversLicenseNumber** in the **piiCategories** request parameter. If **JPDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[JPDriversLicenseNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **JPDriversLicenseNumber** in the **piiCategories** request parameter. If **JPDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[JPDriversLicenseNumber]|
 
 ### Type: Japan My Number Corporate
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Japan|To retrieve this entity type, specify **JPMyNumberCorporate** in the **piiCategories** request parameter. If **JPMyNumberCorporate** is detected, It appears in the **PII** response payload.|[JPMyNumberCorporate]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **JPMyNumberCorporate** in the **piiCategories** request parameter. If **JPMyNumberCorporate** is detected, It appears in the **PII** response payload.|[JPMyNumberCorporate]|
 
 ### Type: Japan My Number Personal
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Japan|To retrieve this entity type, specify **JPMyNumberPersonal** in the **piiCategories** request parameter. If **JPMyNumberPersonal** is detected, It appears in the **PII** response payload.|[JPMyNumberPersonal]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **JPMyNumberPersonal** in the **piiCategories** request parameter. If **JPMyNumberPersonal** is detected, It appears in the **PII** response payload.|[JPMyNumberPersonal]|
 
 ### Type: Japan Passport Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Japan|To retrieve this entity type, specify **JPPassportNumber** in the **piiCategories** request parameter. If **JPPassportNumber** is detected, It appears in the **PII** response payload.|[JPPassportNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **JPPassportNumber** in the **piiCategories** request parameter. If **JPPassportNumber** is detected, It appears in the **PII** response payload.|[JPPassportNumber]|
 
 ### Type: Japan Residence Card Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Japan|To retrieve this entity type, specify **JPResidenceCardNumber** in the **piiCategories** request parameter. If **JPResidenceCardNumber** is detected, It appears in the **PII** response payload.|[JPResidenceCardNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **JPResidenceCardNumber** in the **piiCategories** request parameter. If **JPResidenceCardNumber** is detected, It appears in the **PII** response payload.|[JPResidenceCardNumber]|
 
 ### Type: Japan Resident Registration Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Japan|To retrieve this entity type, specify **JPResidentRegistrationNumber** in the **piiCategories** request parameter. If **JPResidentRegistrationNumber** is detected, It appears in the **PII** response payload.|[JPResidentRegistrationNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **JPResidentRegistrationNumber** in the **piiCategories** request parameter. If **JPResidentRegistrationNumber** is detected, It appears in the **PII** response payload.|[JPResidentRegistrationNumber]|
 
 ### Type: Japan Social Insurance Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Japan|To retrieve this entity type, specify **JPSocialInsuranceNumber** in the **piiCategories** request parameter. If **JPSocialInsuranceNumber** is detected, It appears in the **PII** response payload.|[JPSocialInsuranceNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **JPSocialInsuranceNumber** in the **piiCategories** request parameter. If **JPSocialInsuranceNumber** is detected, It appears in the **PII** response payload.|[JPSocialInsuranceNumber]|
 
 ### Type: Latvia Personal Code
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Latvia|To retrieve this entity type, specify **LVPersonalCode** in the **piiCategories** request parameter. If **LVPersonalCode** is detected, It appears in the **PII** response payload.|[LVPersonalCode]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **LVPersonalCode** in the **piiCategories** request parameter. If **LVPersonalCode** is detected, It appears in the **PII** response payload.|[LVPersonalCode]|
 
 ### Type: Lithuania Personal Code
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Lithuania|To retrieve this entity type, specify **LTPersonalCode** in the **piiCategories** request parameter. If **LTPersonalCode** is detected, It appears in the **PII** response payload.|[LTPersonalCode]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **LTPersonalCode** in the **piiCategories** request parameter. If **LTPersonalCode** is detected, It appears in the **PII** response payload.|[LTPersonalCode]|
 
 ### Type: Luxembourg National Identification Number Natural
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Luxembourg|To retrieve this entity type, specify **LUNationalIdentificationNumberNatural** in the **piiCategories** request parameter. If **LUNationalIdentificationNumberNatural** is detected, It appears in the **PII** response payload.|[LUNationalIdentificationNumberNatural]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **LUNationalIdentificationNumberNatural** in the **piiCategories** request parameter. If **LUNationalIdentificationNumberNatural** is detected, It appears in the **PII** response payload.|[LUNationalIdentificationNumberNatural]|
 
 ### Type: Luxembourg National Identification Number Non Natural
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Luxembourg|To retrieve this entity type, specify **LUNationalIdentificationNumberNonNatural** in the **piiCategories** request parameter. If **LUNationalIdentificationNumberNonNatural** is detected, It appears in the **PII** response payload.|[LUNationalIdentificationNumberNonNatural]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **LUNationalIdentificationNumberNonNatural** in the **piiCategories** request parameter. If **LUNationalIdentificationNumberNonNatural** is detected, It appears in the **PII** response payload.|[LUNationalIdentificationNumberNonNatural]|
 
 ### Type: Malaysia Identity Card Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Malaysia|To retrieve this entity type, specify **MYIdentityCardNumber** in the **piiCategories** request parameter. If **MYIdentityCardNumber** is detected, It appears in the **PII** response payload.|[MYIdentityCardNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **MYIdentityCardNumber** in the **piiCategories** request parameter. If **MYIdentityCardNumber** is detected, It appears in the **PII** response payload.|[MYIdentityCardNumber]|
 
 
 ### Type: Malta Identity Card Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Malta|To retrieve this entity type, specify **MTIdentityCardNumber** in the **piiCategories** request parameter. If **MTIdentityCardNumber** is detected, It appears in the **PII** response payload.|[MTIdentityCardNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **MTIdentityCardNumber** in the **piiCategories** request parameter. If **MTIdentityCardNumber** is detected, It appears in the **PII** response payload.|[MTIdentityCardNumber]|
 
 ### Type: Malta Tax ID Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Malta|To retrieve this entity type, specify **MTTaxIDNumber** in the **piiCategories** request parameter. If **MTTaxIDNumber** is detected, It appears in the **PII** response payload.|[MTTaxIDNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **MTTaxIDNumber** in the **piiCategories** request parameter. If **MTTaxIDNumber** is detected, It appears in the **PII** response payload.|[MTTaxIDNumber]|
 
 ### Type: Netherlands Citizens Service Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Netherlands|To retrieve this entity type, specify **NLCitizensServiceNumber** in the **piiCategories** request parameter. If **NLCitizensServiceNumber** is detected, It appears in the **PII** response payload.|[NLCitizensServiceNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **NLCitizensServiceNumber** in the **piiCategories** request parameter. If **NLCitizensServiceNumber** is detected, It appears in the **PII** response payload.|[NLCitizensServiceNumber]|
 
 ### Type: Netherlands Tax Identification Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Netherlands|To retrieve this entity type, specify **NLTaxIdentificationNumber** in the **piiCategories** request parameter. If **NLTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[NLTaxIdentificationNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **NLTaxIdentificationNumber** in the **piiCategories** request parameter. If **NLTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[NLTaxIdentificationNumber]|
 
 ### Type: Netherlands Value Added Tax Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Netherlands|To retrieve this entity type, specify **NLValueAddedTaxNumber** in the **piiCategories** request parameter. If **NLValueAddedTaxNumber** is detected, It appears in the **PII** response payload.|[NLValueAddedTaxNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **NLValueAddedTaxNumber** in the **piiCategories** request parameter. If **NLValueAddedTaxNumber** is detected, It appears in the **PII** response payload.|[NLValueAddedTaxNumber]|
 
 ### Type: New Zealand Bank Account Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|New Zealand|To retrieve this entity type, specify **NZBankAccountNumber** in the **piiCategories** request parameter. If **NZBankAccountNumber** is detected, It appears in the **PII** response payload.|[NZBankAccountNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **NZBankAccountNumber** in the **piiCategories** request parameter. If **NZBankAccountNumber** is detected, It appears in the **PII** response payload.|[NZBankAccountNumber]|
 
 ### Type: New Zealand Drivers License Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|New Zealand|To retrieve this entity type, specify **NZDriversLicenseNumber** in the **piiCategories** request parameter. If **NZDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[NZDriversLicenseNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **NZDriversLicenseNumber** in the **piiCategories** request parameter. If **NZDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[NZDriversLicenseNumber]|
 
 ### Type: New Zealand Inland Revenue Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|New Zealand|To retrieve this entity type, specify **NZInlandRevenueNumber** in the **piiCategories** request parameter. If **NZInlandRevenueNumber** is detected, It appears in the **PII** response payload.|[NZInlandRevenueNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **NZInlandRevenueNumber** in the **piiCategories** request parameter. If **NZInlandRevenueNumber** is detected, It appears in the **PII** response payload.|[NZInlandRevenueNumber]|
 
 ### Type: New Zealand Ministry Of Health Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|New Zealand|To retrieve this entity type, specify **NZMinistryOfHealthNumber** in the **piiCategories** request parameter. If **NZMinistryOfHealthNumber** is detected, It appears in the **PII** response payload.|[NZMinistryOfHealthNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **NZMinistryOfHealthNumber** in the **piiCategories** request parameter. If **NZMinistryOfHealthNumber** is detected, It appears in the **PII** response payload.|[NZMinistryOfHealthNumber]|
 
 ### Type: New Zealand Social Welfare Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|New Zealand|To retrieve this entity type, specify **NZSocialWelfareNumber** in the **piiCategories** request parameter. If **NZSocialWelfareNumber** is detected, It appears in the **PII** response payload.|[NZSocialWelfareNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **NZSocialWelfareNumber** in the **piiCategories** request parameter. If **NZSocialWelfareNumber** is detected, It appears in the **PII** response payload.|[NZSocialWelfareNumber]|
 
 ### Type: Norway Identity Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Norway|To retrieve this entity type, specify **NOIdentityNumber** in the **piiCategories** request parameter. If **NOIdentityNumber** is detected, It appears in the **PII** response payload.|[NOIdentityNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **NOIdentityNumber** in the **piiCategories** request parameter. If **NOIdentityNumber** is detected, It appears in the **PII** response payload.|[NOIdentityNumber]|
 
 ### Type: Philippines Unified Multi Purpose ID Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Philippines|To retrieve this entity type, specify **PHUnifiedMultiPurposeIDNumber** in the **piiCategories** request parameter. If **PHUnifiedMultiPurposeIDNumber** is detected, It appears in the **PII** response payload.|[PHUnifiedMultiPurposeIDNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **PHUnifiedMultiPurposeIDNumber** in the **piiCategories** request parameter. If **PHUnifiedMultiPurposeIDNumber** is detected, It appears in the **PII** response payload.|[PHUnifiedMultiPurposeIDNumber]|
 
 ### Type: Poland Identity Card
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Poland|To retrieve this entity type, specify **PLIdentityCard** in the **piiCategories** request parameter. If **PLIdentityCard** is detected, It appears in the **PII** response payload.|[PLIdentityCard]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **PLIdentityCard** in the **piiCategories** request parameter. If **PLIdentityCard** is detected, It appears in the **PII** response payload.|[PLIdentityCard]|
 
 ### Type: Poland National ID
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Poland|To retrieve this entity type, specify **PLNationalID** in the **piiCategories** request parameter. If **PLNationalID** is detected, It appears in the **PII** response payload.|[PLNationalID]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **PLNationalID** in the **piiCategories** request parameter. If **PLNationalID** is detected, It appears in the **PII** response payload.|[PLNationalID]|
 
 ### Type: Poland Passport Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Poland|To retrieve this entity type, specify **PLPassportNumber** in the **piiCategories** request parameter. If **PLPassportNumber** is detected, It appears in the **PII** response payload.|[PLPassportNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **PLPassportNumber** in the **piiCategories** request parameter. If **PLPassportNumber** is detected, It appears in the **PII** response payload.|[PLPassportNumber]|
 
 ### Type: Poland REGON Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Poland|To retrieve this entity type, specify **PLREGONNumber** in the **piiCategories** request parameter. If **PLREGONNumber** is detected, It appears in the **PII** response payload.|[PLREGONNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **PLREGONNumber** in the **piiCategories** request parameter. If **PLREGONNumber** is detected, It appears in the **PII** response payload.|[PLREGONNumber]|
 
 ### Type: Poland Tax Identification Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Poland|To retrieve this entity type, specify **PLTaxIdentificationNumber** in the **piiCategories** request parameter. If **PLTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[PLTaxIdentificationNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **PLTaxIdentificationNumber** in the **piiCategories** request parameter. If **PLTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[PLTaxIdentificationNumber]|
 
 ### Type: Portugal Citizen Card Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Portugal|To retrieve this entity type, specify **PTCitizenCardNumber** in the **piiCategories** request parameter. If **PTCitizenCardNumber** is detected, It appears in the **PII** response payload.|[PTCitizenCardNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **PTCitizenCardNumber** in the **piiCategories** request parameter. If **PTCitizenCardNumber** is detected, It appears in the **PII** response payload.|[PTCitizenCardNumber]|
 
 ### Type: Portugal Tax Identification Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Portugal|To retrieve this entity type, specify **PTTaxIdentificationNumber** in the **piiCategories** request parameter. If **PTTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[PTTaxIdentificationNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **PTTaxIdentificationNumber** in the **piiCategories** request parameter. If **PTTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[PTTaxIdentificationNumber]|
 
 ### Type: Romania Personal Numerical Code
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Romania|To retrieve this entity type, specify **ROPersonalNumericalCode** in the **piiCategories** request parameter. If **ROPersonalNumericalCode** is detected, It appears in the **PII** response payload.|[ROPersonalNumericalCode]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **ROPersonalNumericalCode** in the **piiCategories** request parameter. If **ROPersonalNumericalCode** is detected, It appears in the **PII** response payload.|[ROPersonalNumericalCode]|
 
 ### Type: Russia Passport Number Domestic
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Russia|To retrieve this entity type, specify **RUPassportNumberDomestic** in the **piiCategories** request parameter. If **RUPassportNumberDomestic** is detected, It appears in the **PII** response payload.|[RUPassportNumberDomestic]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **RUPassportNumberDomestic** in the **piiCategories** request parameter. If **RUPassportNumberDomestic** is detected, It appears in the **PII** response payload.|[RUPassportNumberDomestic]|
 
 ### Type: Russia Passport Number International
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Russia|To retrieve this entity type, specify **RUPassportNumberInternational** in the **piiCategories** request parameter. If **RUPassportNumberInternational** is detected, It appears in the **PII** response payload.|[RUPassportNumberInternational]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **RUPassportNumberInternational** in the **piiCategories** request parameter. If **RUPassportNumberInternational** is detected, It appears in the **PII** response payload.|[RUPassportNumberInternational]|
 
 ### Type: Saudi Arabia National ID
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Saudi Arabia|To retrieve this entity type, specify **SANationalID** in the **piiCategories** request parameter. If **SANationalID** is detected, It appears in the **PII** response payload.|[SANationalID]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **SANationalID** in the **piiCategories** request parameter. If **SANationalID** is detected, It appears in the **PII** response payload.|[SANationalID]|
 
 ### Type: Singapore National Registration Identity Card Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Singapore|To retrieve this entity type, specify **SGNationalRegistrationIdentityCardNumber** in the **piiCategories** request parameter. If **SGNationalRegistrationIdentityCardNumber** is detected, It appears in the **PII** response payload.|[SGNationalRegistrationIdentityCardNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **SGNationalRegistrationIdentityCardNumber** in the **piiCategories** request parameter. If **SGNationalRegistrationIdentityCardNumber** is detected, It appears in the **PII** response payload.|[SGNationalRegistrationIdentityCardNumber]|
 
 ### Type: Slovakia Personal Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Slovakia|To retrieve this entity type, specify **SKPersonalNumber** in the **piiCategories** request parameter. If **SKPersonalNumber** is detected, It appears in the **PII** response payload.|[SKPersonalNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **SKPersonalNumber** in the **piiCategories** request parameter. If **SKPersonalNumber** is detected, It appears in the **PII** response payload.|[SKPersonalNumber]|
 
 ### Type: Slovenia Tax Identification Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Slovenia|To retrieve this entity type, specify **SITaxIdentificationNumber** in the **piiCategories** request parameter. If **SITaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[SITaxIdentificationNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **SITaxIdentificationNumber** in the **piiCategories** request parameter. If **SITaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[SITaxIdentificationNumber]|
 
 ### Type: Slovenia Unique Master Citizen Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Slovenia|To retrieve this entity type, specify **SIUniqueMasterCitizenNumber** in the **piiCategories** request parameter. If **SIUniqueMasterCitizenNumber** is detected, It appears in the **PII** response payload.|[SIUniqueMasterCitizenNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **SIUniqueMasterCitizenNumber** in the **piiCategories** request parameter. If **SIUniqueMasterCitizenNumber** is detected, It appears in the **PII** response payload.|[SIUniqueMasterCitizenNumber]|
 
 ### Type: South Africa Identification Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|South Africa|To retrieve this entity type, specify **ZAIdentificationNumber** in the **piiCategories** request parameter. If **ZAIdentificationNumber** is detected, It appears in the **PII** response payload.|[ZAIdentificationNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **ZAIdentificationNumber** in the **piiCategories** request parameter. If **ZAIdentificationNumber** is detected, It appears in the **PII** response payload.|[ZAIdentificationNumber]|
 
 ### Type: South Korea Resident Registration Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|South Korea|To retrieve this entity type, specify **KRResidentRegistrationNumber** in the **piiCategories** request parameter. If **KRResidentRegistrationNumber** is detected, It appears in the **PII** response payload.|[KRResidentRegistrationNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **KRResidentRegistrationNumber** in the **piiCategories** request parameter. If **KRResidentRegistrationNumber** is detected, It appears in the **PII** response payload.|[KRResidentRegistrationNumber]|
 
 ### Type: Spain DNI
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Spain|To retrieve this entity type, specify **ESDNI** in the **piiCategories** request parameter. If **ESDNI** is detected, It appears in the **PII** response payload.|[ESDNI]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **ESDNI** in the **piiCategories** request parameter. If **ESDNI** is detected, It appears in the **PII** response payload.|[ESDNI]|
 
 ### Type: Spain Social Security Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Spain|To retrieve this entity type, specify **ESSocialSecurityNumber** in the **piiCategories** request parameter. If **ESSocialSecurityNumber** is detected, It appears in the **PII** response payload.|[ESSocialSecurityNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **ESSocialSecurityNumber** in the **piiCategories** request parameter. If **ESSocialSecurityNumber** is detected, It appears in the **PII** response payload.|[ESSocialSecurityNumber]|
 
 ### Type: Spain Tax Identification Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Spain|To retrieve this entity type, specify **ESTaxIdentificationNumber** in the **piiCategories** request parameter. If **ESTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[ESTaxIdentificationNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **ESTaxIdentificationNumber** in the **piiCategories** request parameter. If **ESTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[ESTaxIdentificationNumber]|
 
 ### Type: Sweden National ID
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Sweden|To retrieve this entity type, specify **SENationalID** in the **piiCategories** request parameter. If **SENationalID** is detected, It appears in the **PII** response payload.|[SENationalID]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **SENationalID** in the **piiCategories** request parameter. If **SENationalID** is detected, It appears in the **PII** response payload.|[SENationalID]|
 
 ### Type: Sweden Passport Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Sweden|To retrieve this entity type, specify **SEPassportNumber** in the **piiCategories** request parameter. If **SEPassportNumber** is detected, It appears in the **PII** response payload.|[SEPassportNumber, PassportNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **SEPassportNumber** in the **piiCategories** request parameter. If **SEPassportNumber** is detected, It appears in the **PII** response payload.|[SEPassportNumber, PassportNumber]|
 
 ### Type: Sweden Tax Identification Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Sweden|To retrieve this entity type, specify **SETaxIdentificationNumber** in the **piiCategories** request parameter. If **SETaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[SETaxIdentificationNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **SETaxIdentificationNumber** in the **piiCategories** request parameter. If **SETaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[SETaxIdentificationNumber]|
 
 ### Type: Switzerland Social Security Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Switzerland|To retrieve this entity type, specify **CHSocialSecurityNumber** in the **piiCategories** request parameter. If **CHSocialSecurityNumber** is detected, It appears in the **PII** response payload.|[CHSocialSecurityNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **CHSocialSecurityNumber** in the **piiCategories** request parameter. If **CHSocialSecurityNumber** is detected, It appears in the **PII** response payload.|[CHSocialSecurityNumber]|
 
 ### Type: Taiwanese ID
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Taiwan|To retrieve this entity type, specify **TWNationalID** in the **piiCategories** request parameter. If **TWNationalID** is detected, It appears in the **PII** response payload.|[TWNationalID]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **TWNationalID** in the **piiCategories** request parameter. If **TWNationalID** is detected, It appears in the **PII** response payload.|[TWNationalID]|
 
 ### Type: Taiwan Passport Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Taiwan|To retrieve this entity type, specify **TWPassportNumber** in the **piiCategories** request parameter. If **TWPassportNumber** is detected, It appears in the **PII** response payload.|[TWPassportNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **TWPassportNumber** in the **piiCategories** request parameter. If **TWPassportNumber** is detected, It appears in the **PII** response payload.|[TWPassportNumber]|
 
 ### Type: Taiwan Resident Certificate
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Taiwan|To retrieve this entity type, specify **TWResidentCertificate** in the **piiCategories** request parameter. If **TWResidentCertificate** is detected, It appears in the **PII** response payload.|[TWResidentCertificate]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **TWResidentCertificate** in the **piiCategories** request parameter. If **TWResidentCertificate** is detected, It appears in the **PII** response payload.|[TWResidentCertificate]|
 
 ### Type: Thailand Population Identification Code
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Thailand|To retrieve this entity type, specify **THPopulationIdentificationCode** in the **piiCategories** request parameter. If **THPopulationIdentificationCode** is detected, It appears in the **PII** response payload.|[THPopulationIdentificationCode]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **THPopulationIdentificationCode** in the **piiCategories** request parameter. If **THPopulationIdentificationCode** is detected, It appears in the **PII** response payload.|[THPopulationIdentificationCode]|
 
 ### Type: Türkiye National Identification Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Türkiye|To retrieve this entity type, specify **TRNationalIdentificationNumber** in the **piiCategories** request parameter. If **TRNationalIdentificationNumber** is detected, It appears in the **PII** response payload.|[TRNationalIdentificationNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **TRNationalIdentificationNumber** in the **piiCategories** request parameter. If **TRNationalIdentificationNumber** is detected, It appears in the **PII** response payload.|[TRNationalIdentificationNumber]|
 
 ### Type: Ukraine Passport Number Domestic
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Ukraine|To retrieve this entity type, specify **UAPassportNumberDomestic** in the **piiCategories** request parameter. If **UAPassportNumberDomestic** is detected, It appears in the **PII** response payload.|[UAPassportNumberDomestic]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **UAPassportNumberDomestic** in the **piiCategories** request parameter. If **UAPassportNumberDomestic** is detected, It appears in the **PII** response payload.|[UAPassportNumberDomestic]|
 
 ### Type: Ukraine Passport Number International
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|Ukraine|To retrieve this entity type, specify **UAPassportNumberInternational** in the **piiCategories** request parameter. If **UAPassportNumberInternational** is detected, It appears in the **PII** response payload.|[UAPassportNumberInternational]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **UAPassportNumberInternational** in the **piiCategories** request parameter. If **UAPassportNumberInternational** is detected, It appears in the **PII** response payload.|[UAPassportNumberInternational]|
 
 ### Type: United Kingdom Drivers License Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|United Kingdom|To retrieve this entity type, specify **UKDriversLicenseNumber** in the **piiCategories** request parameter. If **UKDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[UKDriversLicenseNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **UKDriversLicenseNumber** in the **piiCategories** request parameter. If **UKDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[UKDriversLicenseNumber]|
 
 ### Type: United Kingdom Electoral Roll Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|United Kingdom|To retrieve this entity type, specify **UKElectoralRollNumber** in the **piiCategories** request parameter. If **UKElectoralRollNumber** is detected, It appears in the **PII** response payload.|[UKElectoralRollNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **UKElectoralRollNumber** in the **piiCategories** request parameter. If **UKElectoralRollNumber** is detected, It appears in the **PII** response payload.|[UKElectoralRollNumber]|
 
 ### Type: United Kingdom National Health Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|United Kingdom|To retrieve this entity type, specify **UKNationalHealthNumber** in the **piiCategories** request parameter. If **UKNationalHealthNumber** is detected, It appears in the **PII** response payload.|[UKNationalHealthNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **UKNationalHealthNumber** in the **piiCategories** request parameter. If **UKNationalHealthNumber** is detected, It appears in the **PII** response payload.|[UKNationalHealthNumber]|
 
 ### Type: United Kingdom National Insurance Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|United Kingdom|To retrieve this entity type, specify **UKNationalInsuranceNumber** in the **piiCategories** request parameter. If **UKNationalInsuranceNumber** is detected, It appears in the **PII** response payload.|[UKNationalInsuranceNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **UKNationalInsuranceNumber** in the **piiCategories** request parameter. If **UKNationalInsuranceNumber** is detected, It appears in the **PII** response payload.|[UKNationalInsuranceNumber]|
 
 ### Type: United Kingdom Unique Taxpayer Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|United Kingdom|To retrieve this entity type, specify **UKUniqueTaxpayerNumber** in the **piiCategories** request parameter. If **UKUniqueTaxpayerNumber** is detected, It appears in the **PII** response payload.|[UKUniqueTaxpayerNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **UKUniqueTaxpayerNumber** in the **piiCategories** request parameter. If **UKUniqueTaxpayerNumber** is detected, It appears in the **PII** response payload.|[UKUniqueTaxpayerNumber]|
 
 ### Type: United States Bank Account Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|United States|To retrieve this entity type, specify **USBankAccountNumber** in the **piiCategories** request parameter. If **USBankAccountNumber** is detected, It appears in the **PII** response payload.|[USBankAccountNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **USBankAccountNumber** in the **piiCategories** request parameter. If **USBankAccountNumber** is detected, It appears in the **PII** response payload.|[USBankAccountNumber]|
 
 ### Type: United States Drivers License Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|United States|To retrieve this entity type, specify **USDriversLicenseNumber** in the **piiCategories** request parameter. If **USDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[USDriversLicenseNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **USDriversLicenseNumber** in the **piiCategories** request parameter. If **USDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[USDriversLicenseNumber]|
 
 ### Type: United States Drug Enforcement Agency Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|United States|To retrieve this entity type, specify **"DrugEnforcementAgencyNumber** in the **piiCategories** request parameter. If **DrugEnforcementAgencyNumber** is detected, It appears in the **PII** response payload.|["DrugEnforcementAgencyNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **"DrugEnforcementAgencyNumber** in the **piiCategories** request parameter. If **DrugEnforcementAgencyNumber** is detected, It appears in the **PII** response payload.|["DrugEnforcementAgencyNumber]|
 
 ### Type: United States Individual Taxpayer Identification
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|United States|To retrieve this entity type, specify **USIndividualTaxpayerIdentification** in the **piiCategories** request parameter. If **USIndividualTaxpayerIdentification** is detected, It appears in the **PII** response payload.|[USIndividualTaxpayerIdentification]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **USIndividualTaxpayerIdentification** in the **piiCategories** request parameter. If **USIndividualTaxpayerIdentification** is detected, It appears in the **PII** response payload.|[USIndividualTaxpayerIdentification]|
 
 ### Type: United States Social Security Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|United States|To retrieve this entity type, specify **USSocialSecurityNumber** in the **piiCategories** request parameter. If **USSocialSecurityNumber** is detected, It appears in the **PII** response payload.|[USSocialSecurityNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **USSocialSecurityNumber** in the **piiCategories** request parameter. If **USSocialSecurityNumber** is detected, It appears in the **PII** response payload.|[USSocialSecurityNumber]|
 
 ### Type: United States/United Kingdom Passport Number
 
-|Issuing authority|Details|Tag|
-|---|---|---|
-|United States/United Kingdom|To retrieve this entity type, specify **USUKPassportNumber** in the **piiCategories** request parameter. If **USUKPassportNumber** is detected, It appears in the **PII** response payload.|[USUKPassportNumber]|
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **USUKPassportNumber** in the **piiCategories** request parameter. If **USUKPassportNumber** is detected, It appears in the **PII** response payload.|[USUKPassportNumber]|
 
 
 ## Related content
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンティティカテゴリの内容更新"
}
```

### Explanation
この変更では、`entity-categories.md`ファイルの内容が大幅に更新されました。全体の行数が446行追加され、446行削除されており、合計で892行の変更が行われています。主に、個人情報（PII）エンティティの各種タイプに関する情報が修正された結果です。

具体的には、テーブルのフォーマットが一貫性を持つように調整され、各エンティティのタイトルが改善されました。例えば、「ABA Routing Number」が「American Bankers Association Routing Number」に変更され、より正式な表記がなされています。さらに、テーブル内の「発行機関」や「詳細」欄が整理され、情報の明確性と可読性が向上しています。

これにより、特定のエンティティに関連する情報がよりわかりやすくなり、使用者がその情報を迅速に見つけられるように配慮されています。この更新は、特にAI言語サービスの利用に際して重要なものであり、文書全体の整合性も保たれています。

## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -27,93 +27,7 @@ items:
     displayName: configuration, fine-tuning, azure ai foundry, azure portal
 - name: Azure AI Language capabilities
   items:
-  - name: Custom text classification
-    items:
-    - name: Overview
-      href: custom-text-classification/overview.md
-      displayName: ctc, custom text classification, custom classification, text classifier
-    - name: Quickstart
-      href: custom-text-classification/quickstart.md
-      displayName: ctc setup
-    - name: Language support
-      href: custom-text-classification/language-support.md
-      displayName: ctc languages, multilingual
-    - name: FAQ
-      href: custom-text-classification/faq.md
-      displayName: ctc faq, troubleshooting
-    - name: Responsible use of AI
-      items:
-      - name: Transparency note for custom text classification
-        href: ../../ai-foundry/responsible-ai/language-service/custom-text-classification-transparency-note.md
-        displayName: Transparency note for Custom classification, Custom classification transparency, Responsible AI, Responsible use of AI
-      - name: Integration and responsible use
-        href: ../../ai-foundry/responsible-ai/language-service/custom-text-classification-guidance-integration-responsible-use.md
-        displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
-      - name: Characteristics and limitations
-        href: ../../ai-foundry/responsible-ai/language-service/custom-text-classification-characteristics-and-limitations.md
-        displayName: Custom classification characteristics, Custom classification limitations
-      - name: Data, privacy, and security
-        href: ../../ai-foundry/responsible-ai/language-service/custom-text-classification-data-privacy-security.md
-        displayName: Data privacy, logging, data retention
-    - name: How-to guides
-      items:
-      - name: Create projects
-        href: custom-text-classification/how-to/create-project.md
-        displayName: project creation, setup project
-      - name: Data selection and schema design
-        href: custom-text-classification/how-to/design-schema.md
-        displayName: best practices
-      - name: Label data
-        href: custom-text-classification/how-to/tag-data.md
-        displayName: tag data, annotate text, training data
-      - name: Auto label your data (preview)
-        href: custom-text-classification/how-to/use-autolabeling.md
-        displayName: automatic annotation, smart labeling, ai assisted labeling
-      - name: Label data with Azure Machine Learning
-        href: custom/azure-machine-learning-labeling.md
-        displayName: azure ml labeling, aml annotation
-      - name: Train a model
-        href: custom-text-classification/how-to/train-model.md
-        displayName: training, classifier, build model
-      - name: Model performance (preview)
-        href: custom-text-classification/how-to/view-model-evaluation.md
-        displayName: evaluation, performance metrics, accuracy, precision, recall
-      - name: Deploy a model
-        href: custom-text-classification/how-to/deploy-model.md
-        displayName: deployment, classifier, production deployment
-      - name: Classify text
-        href: custom-text-classification/how-to/call-api.md
-        displayName: classification, prediction
-      - name: Back up and recover your models
-        href: custom-text-classification/fail-over.md
-        displayName: backup, disaster recovery, failover
-      - name: Deploy to multiple regions
-        href: concepts/custom-features/multi-region-deployment.md
-        displayName: multi-region, global deployment, regional distribution
-    - name: Concepts
-      items:
-      - name: Evaluation metrics
-        href: custom-text-classification/concepts/evaluation-metrics.md
-        displayName: performance evaluation, accuracy, f1 score, confusion matrix
-      - name: Accepted data formats
-        href: custom-text-classification/concepts/data-formats.md
-        displayName: data representation
-      - name: Project versioning
-        href: concepts/custom-features/project-versioning.md
-        displayName: version control, model versions
-    - name: Tutorials
-      items:
-      - name: Triage incoming emails with Power Automate
-        href: custom-text-classification/tutorials/triage-email.md
-        displayName: power automate, email classification, automation
-    - name: Reference
-      items:
-      - name: Glossary
-        href: custom-text-classification/glossary.md
-        displayName: model, project, class
-      - name: Service limits
-        href: custom-text-classification/service-limits.md
-        displayName: quotas, restrictions, service boundaries
+
   - name: "Conversational language understanding (CLU)"
     items:
     - name: Overview
@@ -215,6 +129,205 @@ items:
         displayName: limits, quotas, restrictions, boundaries, clu
       - name: Glossary
         href: conversational-language-understanding/glossary.md
+
+  - name: Custom question answering
+    items:
+    - name: Overview
+      href: question-answering/overview.md
+      displayName: custom question answering, faq, knowledge base
+    - name: Quickstart
+      href: question-answering/quickstart/sdk.md
+    - name: Language support
+      href: question-answering/language-support.md
+    - name: Responsible use of AI
+      items:
+      - name: Transparency note for custom question answering
+        href: ../../ai-foundry/responsible-ai/language-service/transparency-note-question-answering.md
+        displayName: Transparency note for custom question answering, custom question answering transparency, Responsible AI, Responsible use of AI
+      - name: Integration and responsible use
+        href: ../../ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use-question-answering.md
+        displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
+      - name: Data, privacy, and security
+        href: ../../ai-foundry/responsible-ai/language-service/data-privacy-security-question-answering.md
+        displayName: Data privacy, logging, data retention
+    - name: How-to guides
+      items:
+      - name: Migrate from QnA Maker to custom question Answering
+        href: question-answering/how-to/migrate-qnamaker-to-question-answering.md
+        displayName: migration, custom question answering
+      - name: Migrate projects from QnA Maker
+        href: question-answering/how-to/migrate-qnamaker.md
+        displayName: migration, transfer
+      - name: Create, test, and deploy a knowledge base
+        href: question-answering/how-to/create-test-deploy.md
+        displayName: knowledge base, test deploy
+      - name: Deploy a CQA agent 🆕
+        href: question-answering/how-to/deploy-agent.md
+        displayName: virtual assistant, chatbot, knowledge base, deployment
+      - name: Export/import/refresh
+        href: question-answering/how-to/export-import-refresh.md
+      - name: Use smart URL refresh
+        href: question-answering/how-to/smart-url-refresh.md
+      - name: Encrypt data at rest
+        href: question-answering/how-to/encrypt-data-at-rest.md
+      - name: Move projects
+        href: question-answering/how-to/migrate-knowledge-base.md
+      - name: Add chit-chat
+        href: question-answering/how-to/chit-chat.md
+      - name: Change default answer
+        href: question-answering/how-to/change-default-answer.md
+      - name: Configure your environment and Azure resources
+        href: question-answering/how-to/configure-azure-resources.md
+        displayName: configuration, fine-tuning, azure ai foundry, azure portal
+      - name: Analytics
+        href: question-answering/how-to/analytics.md
+      - name: Manage projects
+        href: question-answering/how-to/manage-knowledge-base.md
+      - name: Network isolation and private endpoints
+        href: question-answering/how-to/network-isolation.md
+      - name: Authoring API
+        href: question-answering/how-to/authoring.md
+      - name: Prebuilt API
+        href: question-answering/how-to/prebuilt.md
+      - name: Project Best practices
+        href: question-answering/how-to/best-practices.md
+      - name: Troubleshooting
+        href: question-answering/how-to/troubleshooting.md
+      - name: Connect to Azure OpenAI
+        href: question-answering/how-to/azure-openai-integration.md
+    - name: Concepts
+      items:
+      - name: Development lifecycle
+        href: question-answering/concepts/project-development-lifecycle.md
+      - name: Resource planning
+        href: question-answering/concepts/azure-resources.md
+      - name: App planning
+        href: question-answering/concepts/plan.md
+      - name: Precise answering
+        href: question-answering/concepts/precise-answering.md
+      - name: Confidence score
+        href: question-answering/concepts/confidence-score.md
+      - name: Best practices
+        href: question-answering/concepts/best-practices.md
+      - name: Limits
+        href: question-answering/concepts/limits.md
+      - name: Choosing between conversational apps
+        href: conversational-language-understanding/concepts/app-architecture.md
+    - name: Tutorials
+      items:
+      - name: Create an FAQ Bot
+        href: question-answering/tutorials/bot-service.md
+        displayName: bot framework, chatbot
+      - name: Guided conversations
+        href: question-answering/tutorials/guided-conversations.md
+      - name: Active learning
+        href: question-answering/tutorials/active-learning.md
+      - name: Adding synonyms
+        href: question-answering/tutorials/adding-synonyms.md
+      - name: Multiple languages
+        href: question-answering/tutorials/multiple-languages.md
+      - name: Multiple domains
+        href: question-answering/tutorials/multiple-domains.md
+      - name: Add your custom question answering project to Microsoft Copilot Studios
+        href: question-answering/tutorials/power-virtual-agents.md
+        displayName: power virtual agents, pva integration, chatbot, virtual assistant
+    - name: Reference
+      items:
+      - name: General
+        items:
+        - name: Markdown format
+          href: question-answering/reference/markdown-format.md
+        - name: Format guidelines
+          href: question-answering/reference/document-format-guidelines.md
+
+  - name: Custom text classification
+    items:
+    - name: Overview
+      href: custom-text-classification/overview.md
+      displayName: ctc, custom text classification, custom classification, text classifier
+    - name: Quickstart
+      href: custom-text-classification/quickstart.md
+      displayName: ctc setup
+    - name: Language support
+      href: custom-text-classification/language-support.md
+      displayName: ctc languages, multilingual
+    - name: FAQ
+      href: custom-text-classification/faq.md
+      displayName: ctc faq, troubleshooting
+    - name: Responsible use of AI
+      items:
+      - name: Transparency note for custom text classification
+        href: ../../ai-foundry/responsible-ai/language-service/custom-text-classification-transparency-note.md
+        displayName: Transparency note for Custom classification, Custom classification transparency, Responsible AI, Responsible use of AI
+      - name: Integration and responsible use
+        href: ../../ai-foundry/responsible-ai/language-service/custom-text-classification-guidance-integration-responsible-use.md
+        displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
+      - name: Characteristics and limitations
+        href: ../../ai-foundry/responsible-ai/language-service/custom-text-classification-characteristics-and-limitations.md
+        displayName: Custom classification characteristics, Custom classification limitations
+      - name: Data, privacy, and security
+        href: ../../ai-foundry/responsible-ai/language-service/custom-text-classification-data-privacy-security.md
+        displayName: Data privacy, logging, data retention
+    - name: How-to guides
+      items:
+      - name: Create projects
+        href: custom-text-classification/how-to/create-project.md
+        displayName: project creation, setup project
+      - name: Data selection and schema design
+        href: custom-text-classification/how-to/design-schema.md
+        displayName: best practices
+      - name: Label data
+        href: custom-text-classification/how-to/tag-data.md
+        displayName: tag data, annotate text, training data
+      - name: Auto label your data (preview)
+        href: custom-text-classification/how-to/use-autolabeling.md
+        displayName: automatic annotation, smart labeling, ai assisted labeling
+      - name: Label data with Azure Machine Learning
+        href: custom/azure-machine-learning-labeling.md
+        displayName: azure ml labeling, aml annotation
+      - name: Train a model
+        href: custom-text-classification/how-to/train-model.md
+        displayName: training, classifier, build model
+      - name: Model performance (preview)
+        href: custom-text-classification/how-to/view-model-evaluation.md
+        displayName: evaluation, performance metrics, accuracy, precision, recall
+      - name: Deploy a model
+        href: custom-text-classification/how-to/deploy-model.md
+        displayName: deployment, classifier, production deployment
+      - name: Classify text
+        href: custom-text-classification/how-to/call-api.md
+        displayName: classification, prediction
+      - name: Back up and recover your models
+        href: custom-text-classification/fail-over.md
+        displayName: backup, disaster recovery, failover
+      - name: Deploy to multiple regions
+        href: concepts/custom-features/multi-region-deployment.md
+        displayName: multi-region, global deployment, regional distribution
+    - name: Concepts
+      items:
+      - name: Evaluation metrics
+        href: custom-text-classification/concepts/evaluation-metrics.md
+        displayName: performance evaluation, accuracy, f1 score, confusion matrix
+      - name: Accepted data formats
+        href: custom-text-classification/concepts/data-formats.md
+        displayName: data representation
+      - name: Project versioning
+        href: concepts/custom-features/project-versioning.md
+        displayName: version control, model versions
+    - name: Tutorials
+      items:
+      - name: Triage incoming emails with Power Automate
+        href: custom-text-classification/tutorials/triage-email.md
+        displayName: power automate, email classification, automation
+    - name: Reference
+      items:
+      - name: Glossary
+        href: custom-text-classification/glossary.md
+        displayName: model, project, class
+      - name: Service limits
+        href: custom-text-classification/service-limits.md
+        displayName: quotas, restrictions, service boundaries
+
   - name: Entity linking
     items:
     - name: Overview
@@ -273,6 +386,7 @@ items:
           href: ../containers/disconnected-containers.md
         - name: Azure AI containers overview
           href: ../cognitive-services-container-support.md
+
   - name: Key phrase extraction
     items:
     - name: Overview
@@ -314,7 +428,8 @@ items:
       - name: Integrate Power BI
         href: key-phrase-extraction/tutorials/integrate-power-bi.md
         displayName: business intelligence, data visualization
-  - name: Named Entity Recognition
+
+  - name: Named Entity Recognition (prebuilt)
     items:
     - name: Overview
       href: named-entity-recognition/overview.md
@@ -365,7 +480,8 @@ items:
       - name: Extract information in Excel using Power Automate
         href: named-entity-recognition/tutorials/extract-excel-information.md
         displayName: excel integration, power automate, ner automation, extract entities
-  - name: Custom Named Entity Recognition
+
+  - name: Named Entity Recognition (custom)
     items:
     - name: Overview
       href: custom-named-entity-recognition/overview.md
@@ -376,7 +492,7 @@ items:
     - name: FAQ
       href: custom-named-entity-recognition/faq.md
     - name: Glossary
-      href: custom-named-entity-recognition/glossary.md  
+      href: custom-named-entity-recognition/glossary.md
     - name: How-to guides
       items:
       - name: Create projects
@@ -419,6 +535,7 @@ items:
             href: concepts/custom-features/multi-region-deployment.md
           - name: Project versioning
             href: concepts/custom-features/project-versioning.md
+
   - name: Orchestration workflow
     items:
     - name: Overview
@@ -475,6 +592,7 @@ items:
         href: orchestration-workflow/service-limits.md
       - name: Glossary
         href: orchestration-workflow/glossary.md
+
   - name: Personally Identifiable Information detection
     items:
     - name: Overview
@@ -525,115 +643,7 @@ items:
         href: personally-identifiable-information/concepts/entity-categories-list.md
       - name: Recognized entity categories for conversation
         href: personally-identifiable-information/concepts/conversations-entity-categories.md
-  - name: Custom question answering
-    items:
-    - name: Overview
-      href: question-answering/overview.md
-      displayName: custom question answering, faq, knowledge base
-    - name: Quickstart
-      href: question-answering/quickstart/sdk.md
-    - name: Language support
-      href: question-answering/language-support.md
-    - name: Responsible use of AI
-      items:
-      - name: Transparency note for custom question answering
-        href: ../../ai-foundry/responsible-ai/language-service/transparency-note-question-answering.md
-        displayName: Transparency note for custom question answering, custom question answering transparency, Responsible AI, Responsible use of AI
-      - name: Integration and responsible use
-        href: ../../ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use-question-answering.md
-        displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
-      - name: Data, privacy, and security
-        href: ../../ai-foundry/responsible-ai/language-service/data-privacy-security-question-answering.md
-        displayName: Data privacy, logging, data retention
-    - name: How-to guides
-      items:
-      - name: Migrate from QnA Maker to custom question Answering
-        href: question-answering/how-to/migrate-qnamaker-to-question-answering.md
-        displayName: migration, custom question answering
-      - name: Migrate projects from QnA Maker
-        href: question-answering/how-to/migrate-qnamaker.md
-        displayName: migration, transfer
-      - name: Create, test, and deploy a knowledge base
-        href: question-answering/how-to/create-test-deploy.md
-        displayName: knowledge base, test deploy
-      - name: Deploy a CQA agent 🆕
-        href: question-answering/how-to/deploy-agent.md
-        displayName: virtual assistant, chatbot, knowledge base, deployment
-      - name: Export/import/refresh
-        href: question-answering/how-to/export-import-refresh.md
-      - name: Use smart URL refresh
-        href: question-answering/how-to/smart-url-refresh.md
-      - name: Encrypt data at rest
-        href: question-answering/how-to/encrypt-data-at-rest.md
-      - name: Move projects
-        href: question-answering/how-to/migrate-knowledge-base.md
-      - name: Add chit-chat
-        href: question-answering/how-to/chit-chat.md
-      - name: Change default answer
-        href: question-answering/how-to/change-default-answer.md
-      - name: Configure your environment and Azure resources
-        href: question-answering/how-to/configure-azure-resources.md
-        displayName: configuration, fine-tuning, azure ai foundry, azure portal
-      - name: Analytics
-        href: question-answering/how-to/analytics.md
-      - name: Manage projects
-        href: question-answering/how-to/manage-knowledge-base.md
-      - name: Network isolation and private endpoints
-        href: question-answering/how-to/network-isolation.md
-      - name: Authoring API
-        href: question-answering/how-to/authoring.md
-      - name: Prebuilt API
-        href: question-answering/how-to/prebuilt.md
-      - name: Project Best practices
-        href: question-answering/how-to/best-practices.md
-      - name: Troubleshooting
-        href: question-answering/how-to/troubleshooting.md
-      - name: Connect to Azure OpenAI
-        href: question-answering/how-to/azure-openai-integration.md
-    - name: Concepts
-      items:
-      - name: Development lifecycle
-        href: question-answering/concepts/project-development-lifecycle.md
-      - name: Resource planning
-        href: question-answering/concepts/azure-resources.md
-      - name: App planning
-        href: question-answering/concepts/plan.md
-      - name: Precise answering
-        href: question-answering/concepts/precise-answering.md
-      - name: Confidence score
-        href: question-answering/concepts/confidence-score.md
-      - name: Best practices
-        href: question-answering/concepts/best-practices.md
-      - name: Limits
-        href: question-answering/concepts/limits.md
-      - name: Choosing between conversational apps
-        href: conversational-language-understanding/concepts/app-architecture.md
-    - name: Tutorials
-      items:
-      - name: Create an FAQ Bot
-        href: question-answering/tutorials/bot-service.md
-        displayName: bot framework, chatbot
-      - name: Guided conversations
-        href: question-answering/tutorials/guided-conversations.md
-      - name: Active learning
-        href: question-answering/tutorials/active-learning.md
-      - name: Adding synonyms
-        href: question-answering/tutorials/adding-synonyms.md
-      - name: Multiple languages
-        href: question-answering/tutorials/multiple-languages.md
-      - name: Multiple domains
-        href: question-answering/tutorials/multiple-domains.md
-      - name: Add your custom question answering project to Microsoft Copilot Studios
-        href: question-answering/tutorials/power-virtual-agents.md
-        displayName: power virtual agents, pva integration, chatbot, virtual assistant
-    - name: Reference
-      items:
-      - name: General
-        items:
-        - name: Markdown format
-          href: question-answering/reference/markdown-format.md
-        - name: Format guidelines
-          href: question-answering/reference/document-format-guidelines.md
+
   - name: Sentiment analysis and opinion mining
     items:
       - name: Overview
@@ -674,50 +684,8 @@ items:
         items:
         - name: Use Flask to translate text, analyze sentiment, and synthesize speech
           href: /training/modules/python-flask-build-ai-web-app/
-  - name: Text Analytics for health
-    items:
-    - name: Overview
-      href: text-analytics-for-health/overview.md
-      displayName: text analytics for health, healthcare nlp, medical text analysis, clinical text, health entities
-    - name: Quickstart
-      href: text-analytics-for-health/quickstart.md
-    - name: Language support
-      href: text-analytics-for-health/language-support.md
-    - name: Responsible use of AI
-      items:
-      - name: Transparency note for Text Analytics for health
-        href: ../../ai-foundry/responsible-ai/language-service/transparency-note-health.md
-        displayName: Transparency note for Text Analytics health, Text Analytics for health transparency, Responsible AI, Responsible use of AI
-      - name: Integration and responsible use
-        href: ../../ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use.md
-        displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
-      - name: Data, privacy, and security
-        href: ../../ai-foundry/responsible-ai/language-service/data-privacy.md
-        displayName: Data privacy, logging, data retention
-    - name: How-to guides
-      items:
-      - name: How to call the API
-        href: text-analytics-for-health/how-to/call-api.md
-      - name: Use containers
-        items:
-        - name: Use Docker containers
-          href: text-analytics-for-health/how-to/use-containers.md
-        - name: Configure Docker containers
-          href: text-analytics-for-health/how-to/configure-containers.md
-        - name: Use container instances
-          href: ../containers/azure-container-instance-recipe.md?context=/azure/ai-services/language-service/context/context
-        - name: Azure AI containers overview
-          href: ../cognitive-services-container-support.md
-    - name: Concepts
-      items:
-      - name: Recognized entity categories
-        href: text-analytics-for-health/concepts/health-entity-categories.md
-      - name: Relation extraction
-        href: text-analytics-for-health/concepts/relation-extraction.md
-      - name: Assertion detection
-        href: text-analytics-for-health/concepts/assertion-detection.md
-      - name: Fast Healthcare Interoperability Resources structuring
-        href: text-analytics-for-health/concepts/fhir.md
+
+
   - name: Summarization
     items:
     - name: Overview
@@ -899,6 +867,51 @@ items:
           href: https://aka.ms/sdk-samples-conversation-python
         - name: Azure.AI.Language.QuestionAnswering namespace
           href: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/cognitivelanguage/azure-ai-language-questionanswering
+
+  - name: Text Analytics for health
+    items:
+    - name: Overview
+      href: text-analytics-for-health/overview.md
+      displayName: text analytics for health, healthcare nlp, medical text analysis, clinical text, health entities
+    - name: Quickstart
+      href: text-analytics-for-health/quickstart.md
+    - name: Language support
+      href: text-analytics-for-health/language-support.md
+    - name: Responsible use of AI
+      items:
+      - name: Transparency note for Text Analytics for health
+        href: ../../ai-foundry/responsible-ai/language-service/transparency-note-health.md
+        displayName: Transparency note for Text Analytics health, Text Analytics for health transparency, Responsible AI, Responsible use of AI
+      - name: Integration and responsible use
+        href: ../../ai-foundry/responsible-ai/language-service/guidance-integration-responsible-use.md
+        displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
+      - name: Data, privacy, and security
+        href: ../../ai-foundry/responsible-ai/language-service/data-privacy.md
+        displayName: Data privacy, logging, data retention
+    - name: How-to guides
+      items:
+      - name: How to call the API
+        href: text-analytics-for-health/how-to/call-api.md
+      - name: Use containers
+        items:
+        - name: Use Docker containers
+          href: text-analytics-for-health/how-to/use-containers.md
+        - name: Configure Docker containers
+          href: text-analytics-for-health/how-to/configure-containers.md
+        - name: Use container instances
+          href: ../containers/azure-container-instance-recipe.md?context=/azure/ai-services/language-service/context/context
+        - name: Azure AI containers overview
+          href: ../cognitive-services-container-support.md
+    - name: Concepts
+      items:
+      - name: Recognized entity categories
+        href: text-analytics-for-health/concepts/health-entity-categories.md
+      - name: Relation extraction
+        href: text-analytics-for-health/concepts/relation-extraction.md
+      - name: Assertion detection
+        href: text-analytics-for-health/concepts/assertion-detection.md
+      - name: Fast Healthcare Interoperability Resources structuring
+        href: text-analytics-for-health/concepts/fhir.md
 - name: Resources
   items:
     - name: Support and help options
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次ファイルの更新"
}
```

### Explanation
この変更では、`toc.yml`ファイルが大幅に更新されました。追加された行数は256行、削除された行数は243行で、合計499行の変更が行われています。変更の主な目的は、Azure AI言語サービスに関連する新しいトピックを追加し、既存のトピックの整理を行うことです。

新たに追加されたトピックには「会話型言語理解（CLU）」や「カスタム質問応答」、「感情分析と意見採掘」、および「医療向けテキスト分析」などが含まれ、これにより、利用者が幅広い機能にアクセスできるようになっています。また、不必要な情報の削除と、情報の一貫性を持たせる構造に改善されています。

特に「責任あるAIの使用」に関連する項目については、透明性のノートやデータ保護に関するガイダンスが強調され、AIの利用においての倫理的観点が考慮されています。全体として、ドキュメントはよりインタラクティブで、利用者が容易に情報にアクセスできる構造になっています。


