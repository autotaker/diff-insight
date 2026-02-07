---
date: '2026-02-07'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ad7cfc9...MicrosoftDocs:dfa2fda
summary: |-
  この報告は、AIサービスに関連する文書の数ファイルで行われた改訂に関するものです。主な内容として、著者情報の更新、画像のアクセシビリティ改善、PII（個人を特定可能な情報）カテゴリリストの大規模な更新、PIIテキストの赤外線処理に関する情報の追加、PII検出に関する概要の見直しが含まれています。

  新機能としては、PIIエンティティの置換機能が強調された「syntheticReplacement」という新たなポリシータイプが導入されました。また、Azure Language PII検出サービスの利用を示す動画デモも追加されています。

  一方で、いくつかの大きな変更もあり、特にPIIエンティティのカテゴリリストが更新され、情報の削除と追加が行われています。Azure Language PII検出サービスの概要もシンプル化されています。

  その他の更新として、著者情報の更新や、画像のaltテキストの改善などが行われています。全体として、これらの改訂はAzureのAIドキュメンテーションをより正確で直感的にすることを目的としています。特にデータプライバシーの規範に適応するための新しいエンティティを提供し、データセキュリティのベストプラクティスを強化することが狙いです。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ad7cfc9...MicrosoftDocs:dfa2fda){target="_blank"}

# Highlights
この差分は、AIサービスに関連するドキュメントの複数のファイルにおいて、著者情報の更新、画像のアクセシビリティ改善、大規模なカテゴリリストの更新、PIIテキストの赤外線処理に関する情報追加、およびPII検出に関する概要の見直しを含む改訂が行われました。

## New features
- `redact-text-pii.md`に新たなポリシータイプ「syntheticReplacement」が導入され、PIIエンティティの置換機能が強調されました。
- `overview.md`において、Azure Language PII検出サービスの利用を示す動画デモが追加されました。

## Breaking changes
- `entity-categories-list.md`では大規模なPIIエンティティのカテゴリリストの更新が行われ、情報の削除と追加がありました。
- `overview.md`の大幅な削除により、Azure Language PII検出サービスの概要がシンプル化されました。

## Other updates
- 著者情報が`project-share-custom-models.md`で更新されました。
- `get-keys-endpoint-azure.md`では画像のaltテキストがより適切な表現に変更されました。

# Insights
今回のコード差分による改訂では、AzureのAIドキュメンテーションがより正確で、直感的なものとなることを目指していることが見て取れます。特に、$entities-category.md$におけるPII（個人を特定可能な情報）カテゴリリストの大規模な調整により、ユーザーは最新の情報をもとに安全で効果的なデータ管理が可能になります。新しいエンティティを追加し、古い情報を削除することで、変化するデータプライバシー規範に適応する新しいエンティティの包括的なセットをユーザーに提供しています。

また、PIIテキストの赤外線処理における新機能の駆使により、ユーザーはデータセキュリティに関するベストプラクティスをさらに強化できます。特に`syntheticReplacement`ポリシーは、大量のデータを扱う際にも効率的なエンティティ置換を実現し、データのプライバシーを確保するための有用な機能といえます。

最後に、Azure Language PII検出サービスのガイドが簡潔化された背景には、情報過多を避けつつ、ユーザーにサービスの本質を理解しやすくする狙いがあるでしょう。リアルタイムでの利用例を示す動画の追加により、視覚的に戦略的なインサイトが得られるようになっています。これにより、概念理解だけではなく、より具体的なアクションに移す際の手助けとなるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [project-share-custom-models.md](#item-acd5dd) | minor update | プロジェクト共有カスタムモデルの著者情報の更新 | modified | 1 | 1 | 2 | 
| [get-keys-endpoint-azure.md](#item-bbdf8d) | minor update | Azureポータルのキーとエンドポイントページの画像説明の変更 | modified | 1 | 1 | 2 | 
| [entity-categories-list.md](#item-05522d) | breaking change | PIIエンティティのカテゴリリストの大幅な更新 | modified | 60 | 60 | 120 | 
| [redact-text-pii.md](#item-9e48af) | minor update | PIIテキストの赤外線処理に関する情報の追加 | modified | 7 | 2 | 9 | 
| [overview.md](#item-8a6932) | breaking change | PII検出に関する概要の大幅な更新 | modified | 9 | 45 | 54 | 


# Modified Contents
## articles/ai-services/document-intelligence/how-to-guides/project-share-custom-models.md{#item-acd5dd}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: how-to
 ms.date: 11/18/2025
-ms.author: jppark
+ms.author: lajanuar
 monikerRange: '>=doc-intel-3.0.0'
 ms.custom: sfi-image-nochange
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロジェクト共有カスタムモデルの著者情報の更新"
}
```

### Explanation
この変更は、`project-share-custom-models.md`ファイルの著者情報を更新することを目的としています。具体的には、ファイル内の`ms.author`フィールドが`jppark`から`lajanuar`に変更されました。変更は全体で2つの行で構成されており、1行が削除され、1行が追加されています。この修正は情報の更新を反映するものであり、文書の管理やメンテナンスに役立ちます。

## articles/ai-services/language-service/custom-text-classification/includes/get-keys-endpoint-azure.md{#item-bbdf8d}

<details>
<summary>Diff</summary>
````diff
@@ -10,4 +10,4 @@ ms.author: lajanuar
 
 * From the menu on the left side, select **Keys and Endpoint**. The endpoint and key are used for API requests.
 
-:::image type="content" source="../media/get-endpoint-azure.png" alt-text="A screenshot showing the key and endpoint page in the Azure portal." lightbox="../media/get-endpoint-azure.png":::
+:::image type="content" source="../media/get-endpoint-azure.png" alt-text="Screenshot that shows the key and endpoint page in the Azure portal." lightbox="../media/get-endpoint-azure.png":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azureポータルのキーとエンドポイントページの画像説明の変更"
}
```

### Explanation
この変更は、`get-keys-endpoint-azure.md`ファイル内の画像の説明を更新することを目的としています。具体的には、画像に関するaltテキストが改訂され、より適切な表現に修正されています。変更は2つの行から成り、1行が削除され、1行が新たに追加されています。この修正により、視覚的な情報がより明確に伝わり、アクセシビリティの向上が期待できます。また、著者情報として`ms.author`が`lajanuar`のまま維持されています。

## articles/ai-services/language-service/personally-identifiable-information/concepts/entity-categories-list.md{#item-05522d}

<details>
<summary>Diff</summary>
````diff
@@ -14,64 +14,64 @@ ms.custom:
 ---
 # Recognized PII entities list
 
-| Entity | Entity | Entity|
-|--|--|--|
-|[Address](entity-categories.md#type-address)| [Age](entity-categories.md#type-age) | [American Bankers Association Routing Number](entity-categories.md#type-american-bankers-association-routing-number) |
+| Entity | Entity | Entity |
+| -- | -- | -- |
+| [Address](entity-categories.md#type-address) | [Age](entity-categories.md#type-age) | [American Bankers Association Routing Number](entity-categories.md#type-american-bankers-association-routing-number) |
 | [Airport 🆕](entity-categories.md#type-airport-preview) | [Argentina National Identity Number](entity-categories.md#type-argentina-national-identity-number) | [Australia Bank Account Number](entity-categories.md#type-australia-bank-account-number) |
-| [Australia Business Number](entity-categories.md#type-australia-business-number) |
-| [Australia Company Number](entity-categories.md#type-australia-company-number) | [Australia Drivers License Number](entity-categories.md#type-australia-drivers-license-number) | [Australia Medical Account Number](entity-categories.md#type-australia-medical-account-number) |
-| [Australia Passport Number](entity-categories.md#type-australia-passport-number) | [Australia Tax File Number](entity-categories.md#type-australia-tax-file-number) | [Austria Identity Card](entity-categories.md#type-austria-identity-card) |
-| [Austria Tax Identification Number](entity-categories.md#type-austria-tax-identification-number) | [Austria Value Added Tax Number](entity-categories.md#type-austria-value-added-tax-number) | [Azure Document DB Auth Key](entity-categories.md#type-azure-document-db-auth-key) |
-| [Azure IAAS Database Connection And SQL String](entity-categories.md#type-azure-iaas-database-connection-and-sql-string) | [Azure IoT Connection String](entity-categories.md#type-azure-iot-connection-string) | [Azure Publish Setting Password](entity-categories.md#type-azure-publish-setting-password) |
-| [Azure Redis Cache String](entity-categories.md#type-azure-redis-cache-string) | [Azure SAS](entity-categories.md#type-azure-sas) | [Azure Service Bus String](entity-categories.md#type-azure-service-bus-string) |
-| [Azure Storage Account Generic](entity-categories.md#type-azure-storage-account-generic) | [Azure Storage Account Key](entity-categories.md#type-azure-storage-account-key) | [Bank Account Number 🆕](entity-categories.md#type-bank-account-number-preview) |
-| [Belgium National Number](entity-categories.md#type-belgium-national-number) | [Belgium Value Added Tax Number](entity-categories.md#type-belgium-value-added-tax-number) | [Brazil CPF Number](entity-categories.md#type-brazil-cpf-number) |
-| [Brazil Legal Entity Number](entity-categories.md#type-brazil-legal-entity-number) | [Brazil National IDRG](entity-categories.md#type-brazil-national-idrg) | [Bulgaria Uniform Civil Number](entity-categories.md#type-bulgaria-uniform-civil-number) |
-| [Canada Bank Account Number](entity-categories.md#type-canada-bank-account-number) | [Canada Drivers License Number](entity-categories.md#type-canada-drivers-license-number) | [Canada Health Service Number](entity-categories.md#type-canada-health-service-number) |
-| [Canada Passport Number](entity-categories.md#type-canada-passport-number) | [Canada Personal Health Identification](entity-categories.md#type-canada-personal-health-identification) | [Canada Social Insurance Number](entity-categories.md#type-canada-social-insurance-number) |
-| [Canada Social Identification Number 🆕](entity-categories.md#type-canada-social-identification-number-preview) | [Chile Identity Card Number](entity-categories.md#type-chile-identity-card-number) | [China Resident Identity Card Number](entity-categories.md#type-china-resident-identity-card-number) |
-| [City 🆕](entity-categories.md#type-city-preview) | [Credit Card Number](entity-categories.md#type-credit-card-number) | [Croatia Identity Card Number](entity-categories.md#type-croatia-identity-card-number) | [Croatia National ID Number](entity-categories.md#type-croatia-national-id-number) | [Croatia Personal Identification Number](entity-categories.md#type-croatia-personal-identification-number) |
-| [CVV 🆕](entity-categories.md#type-card-verification-value-cvv-preview) | [Cyprus Identity Card](entity-categories.md#type-cyprus-identity-card) | [Cyprus Tax Identification Number](entity-categories.md#type-cyprus-tax-identification-number) |
-| [Date](entity-categories.md#type-date) | [Date Of Birth 🆕](entity-categories.md#type-date-of-birth-preview) | [Denmark Personal Identification Number](entity-categories.md#type-denmark-personal-identification-number) |
-| [Drivers License Number 🆕](entity-categories.md#type-drivers-license-number-preview) | [Email](entity-categories.md#type-email) | [Estonia Personal Identification Code](entity-categories.md#type-estonia-personal-identification-code) |
-| [European Union Debit Card Number](entity-categories.md#type-european-union-debit-card-number) | [European Union Drivers License Number](entity-categories.md#type-european-union-drivers-license-number) | [European Union GPS Coordinates](entity-categories.md#type-european-union-gps-coordinates) |
-| [European Union National Identification Number](entity-categories.md#type-european-union-national-identification-number) | [European Union Passport Number](entity-categories.md#type-european-union-passport-number) | [European Union Social Security Number](entity-categories.md#type-european-union-social-security-number) |
-| [European Union Tax Identification Number](entity-categories.md#type-european-union-tax-identification-number) | [Expiration Date 🆕](entity-categories.md#type-expiration-date-preview) | [Finland European Health Number](entity-categories.md#type-finland-european-health-number) |
-| [Finland National ID](entity-categories.md#type-finland-national-id) | [Finland Passport Number](entity-categories.md#type-finland-passport-number) | [France Drivers License Number](entity-categories.md#type-france-drivers-license-number) |
-| [France National ID](entity-categories.md#type-france-national-id) | [France Passport Number](entity-categories.md#type-france-passport-number) | [France Social Security Number](entity-categories.md#type-france-social-security-number) |
-| [France Tax Identification Number](entity-categories.md#type-france-tax-identification-number) | [France Value Added Tax Number](entity-categories.md#type-france-value-added-tax-number) | [Germany Drivers License Number](entity-categories.md#type-germany-drivers-license-number) |
-| [Germany Identity Card Number](entity-categories.md#type-germany-identity-card-number) | [Germany Passport Number](entity-categories.md#type-germany-passport-number) | [Germany Tax Identification Number](entity-categories.md#type-germany-tax-identification-number) |
-| [Germany Value Added Number](entity-categories.md#type-germany-value-added-number) | [GPE 🆕](entity-categories.md#type-geopolitical-entity-gpe-preview) | [Greece National ID Card](entity-categories.md#type-greece-national-id-card) |
-| [Greece Tax Identification Number](entity-categories.md#type-greece-tax-identification-number) | [Hong Kong SAR Identity Card Number](entity-categories.md#type-hong-kong-sar-identity-card-number) | [Hungary Personal Identification Number](entity-categories.md#type-hungary-personal-identification-number) |
-| [Hungary Value Added Number](entity-categories.md#type-hungary-value-added-number) | [India Permanent Account](entity-categories.md#type-india-permanent-account) | [India Unique Identification Number](entity-categories.md#type-india-unique-identification-number) |
-| [Indonesia Identity Card Number](entity-categories.md#type-indonesia-identity-card-number) | [International Banking Account Number](entity-categories.md#type-international-banking-account-number) | [IP Address](entity-categories.md#type-ip-address) |
-| [Ireland Personal Public Service Number](entity-categories.md#type-ireland-personal-public-service-number) | [Israel Bank Account Number](entity-categories.md#type-israel-bank-account-number) | [Israel National ID](entity-categories.md#type-israel-national-id) |
-| [Italy Drivers License Number](entity-categories.md#type-italy-drivers-license-number) | [Italy Fiscal Code](entity-categories.md#type-italy-fiscal-code) | [Italy Value Added Tax Number](entity-categories.md#type-italy-value-added-tax-number) |
-| [Japan Bank Account Number](entity-categories.md#type-japan-bank-account-number) | [Japan Drivers License Number](entity-categories.md#type-japan-drivers-license-number) | [Japan My Number Corporate](entity-categories.md#type-japan-my-number-corporate) |
-| [Japan My Number Personal](entity-categories.md#type-japan-my-number-personal) | [Japan Passport Number](entity-categories.md#type-japan-passport-number) | [Japan Residence Card Number](entity-categories.md#type-japan-residence-card-number) |
-| [Japan Resident Registration Number](entity-categories.md#type-japan-resident-registration-number) | [Japan Social Insurance Number](entity-categories.md#type-japan-social-insurance-number) | [Latvia Personal Code](entity-categories.md#type-latvia-personal-code) |
-| [License Plate 🆕](entity-categories.md#type-license-plate-preview) | [Lithuania Personal Code](entity-categories.md#type-lithuania-personal-code) | [Location 🆕](entity-categories.md#type-location-preview) |
-| [Luxembourg National Identification Number Natural](entity-categories.md#type-luxembourg-national-identification-number-natural) | [Luxembourg National Identification Number Non Natural](entity-categories.md#type-luxembourg-national-identification-number-non-natural) | [Malaysia Identity Card Number](entity-categories.md#type-malaysia-identity-card-number) | [Malta Identity Card Number](entity-categories.md#type-malta-identity-card-number) |
-| [Malta Tax ID Number](entity-categories.md#type-malta-tax-id-number) | [Netherlands Citizens Service Number](entity-categories.md#type-netherlands-citizens-service-number) | [Netherlands Tax Identification Number](entity-categories.md#type-netherlands-tax-identification-number) |
-| [Netherlands Value Added Tax Number](entity-categories.md#type-netherlands-value-added-tax-number) | [New Zealand Bank Account Number](entity-categories.md#type-new-zealand-bank-account-number) | [New Zealand Drivers License Number](entity-categories.md#type-new-zealand-drivers-license-number) |
-| [New Zealand Inland Revenue Number](entity-categories.md#type-new-zealand-inland-revenue-number) | [New Zealand Ministry Of Health Number](entity-categories.md#type-new-zealand-ministry-of-health-number) | [New Zealand Social Welfare Number](entity-categories.md#type-new-zealand-social-welfare-number) |
-| [Norway Identity Number](entity-categories.md#type-norway-identity-number) | [Organization](entity-categories.md#type-organization) | [Passport Number 🆕](entity-categories.md#type-passport-number-preview) |
-| [Password 🆕](entity-categories.md#type-password-preview) | [Person](entity-categories.md#type-person) | [Philippines Unified Multi Purpose ID Number](entity-categories.md#type-philippines-unified-multi-purpose-id-number) |
-| [Phone Number](entity-categories.md#type-phone-number) | [Poland Identity Card](entity-categories.md#type-poland-identity-card) | [Poland National ID](entity-categories.md#type-poland-national-id) |
-| [Poland Passport Number](entity-categories.md#type-poland-passport-number) | [Poland REGON Number](entity-categories.md#type-poland-regon-number) | [Poland Tax Identification Number](entity-categories.md#type-poland-tax-identification-number) |
-| [Portugal Tax Identification Number](entity-categories.md#type-portugal-tax-identification-number) | [Romania Personal Numerical Code](entity-categories.md#type-romania-personal-numerical-code) | [Russia Passport Number Domestic](entity-categories.md#type-russia-passport-number-domestic) |
-| [Russia Passport Number International](entity-categories.md#type-russia-passport-number-international) | [Saudi Arabia National ID](entity-categories.md#type-saudi-arabia-national-id) | [Singapore National Registration Identity Card Number](entity-categories.md#type-singapore-national-registration-identity-card-number) |
-| [Slovakia Personal Number](entity-categories.md#type-slovakia-personal-number) | [Slovenia Tax Identification Number](entity-categories.md#type-slovenia-tax-identification-number) | [Slovenia Unique Master Citizen Number](entity-categories.md#type-slovenia-unique-master-citizen-number) |
-| [Sort Code 🆕](entity-categories.md#type-sort-code-preview) | [South Africa Identification Number](entity-categories.md#type-south-africa-identification-number) | [South Korea Drivers License Number 🆕](entity-categories.md#type-south-korea-drivers-license-number-preview) |
-| [South Korea Passport Number 🆕](entity-categories.md#type-south-korea-passport-number-preview) | [South Korea Resident Registration Number](entity-categories.md#type-south-korea-resident-registration-number) | [South Korea Social Security Number 🆕](entity-categories.md#type-south-korea-social-security-number-preview) |
-| [Spain DNI](entity-categories.md#type-spain-dni) | [Spain Social Security Number](entity-categories.md#type-spain-social-security-number) | [Spain Tax Identification Number](entity-categories.md#type-spain-tax-identification-number) |
-| [SQL Server Connection String](entity-categories.md#type-sql-server-connection-string) | [State 🆕](entity-categories.md#type-state-preview) | [Sweden National ID](entity-categories.md#type-sweden-national-id) |
-| [Sweden Passport Number](entity-categories.md#type-sweden-passport-number) | [Sweden Tax Identification Number](entity-categories.md#type-sweden-tax-identification-number) | [SWIFT Code](entity-categories.md#type-swift-code) |
-| [Taiwanese ID](entity-categories.md#type-taiwanese-id) | [Taiwan Passport Number](entity-categories.md#type-taiwan-passport-number) | [Taiwan Resident Certificate](entity-categories.md#type-taiwan-resident-certificate) |
-| [Thailand Population Identification Code](entity-categories.md#type-thailand-population-identification-code) | [Türkiye National Identification Number](entity-categories.md#type-türkiye-national-identification-number) | [Ukraine Passport Number Domestic](entity-categories.md#type-ukraine-passport-number-domestic) |
-| [Ukraine Passport Number International](entity-categories.md#type-ukraine-passport-number-international) | [United Kingdom Drivers License Number](entity-categories.md#type-united-kingdom-drivers-license-number) | [United Kingdom Electoral Roll Number](entity-categories.md#type-united-kingdom-electoral-roll-number) |
-| [United Kingdom National Health Number](entity-categories.md#type-united-kingdom-national-health-number) | [United Kingdom National Insurance Number](entity-categories.md#type-united-kingdom-national-insurance-number) | [United Kingdom Unique Taxpayer Number](entity-categories.md#type-united-kingdom-unique-taxpayer-number) |
-| [United States Bank Account Number](entity-categories.md#type-united-states-bank-account-number) | [United States Drivers License Number](entity-categories.md#type-united-states-drivers-license-number) | [United States Drug Enforcement Agency Number](entity-categories.md#type-united-states-drug-enforcement-agency-number) |
-| [United States Individual Taxpayer Identification](entity-categories.md#type-united-states-individual-taxpayer-identification) | [United States Medicare Beneficiary Id 🆕](entity-categories.md#type-united-states-medicare-beneficiary-identification-preview) | [United States Social Security Number](entity-categories.md#type-united-states-social-security-number) |
-| [United States/United Kingdom Passport Number](entity-categories.md#type-united-statesunited-kingdom-passport-number) | [URL](entity-categories.md#type-url) | [VIN 🆕](entity-categories.md#type-vin-preview) |
-| [ZipCode 🆕](entity-categories.md#type-zipcode-preview) |
+| [Australia Business Number](entity-categories.md#type-australia-business-number) | [Australia Company Number](entity-categories.md#type-australia-company-number) | [Australia Drivers License Number](entity-categories.md#type-australia-drivers-license-number) |
+| [Australia Medical Account Number](entity-categories.md#type-australia-medical-account-number) | [Australia Passport Number](entity-categories.md#type-australia-passport-number) | [Australia Tax File Number](entity-categories.md#type-australia-tax-file-number) |
+| [Austria Identity Card](entity-categories.md#type-austria-identity-card) | [Austria Tax Identification Number](entity-categories.md#type-austria-tax-identification-number) | [Austria Value Added Tax Number](entity-categories.md#type-austria-value-added-tax-number) |
+| [Azure Document DB Auth Key](entity-categories.md#type-azure-document-db-auth-key) | [Azure IAAS Database Connection And SQL String](entity-categories.md#type-azure-iaas-database-connection-and-sql-string) | [Azure IoT Connection String](entity-categories.md#type-azure-iot-connection-string) |
+| [Azure Publish Setting Password](entity-categories.md#type-azure-publish-setting-password) | [Azure Redis Cache String](entity-categories.md#type-azure-redis-cache-string) | [Azure SAS](entity-categories.md#type-azure-sas) |
+| [Azure Service Bus String](entity-categories.md#type-azure-service-bus-string) | [Azure Storage Account Generic](entity-categories.md#type-azure-storage-account-generic) | [Azure Storage Account Key](entity-categories.md#type-azure-storage-account-key) |
+| [Bank Account Number 🆕](entity-categories.md#type-bank-account-number-preview) | [Belgium National Number](entity-categories.md#type-belgium-national-number) | [Belgium Value Added Tax Number](entity-categories.md#type-belgium-value-added-tax-number) |
+| [Brazil CPF Number](entity-categories.md#type-brazil-cpf-number) | [Brazil Legal Entity Number](entity-categories.md#type-brazil-legal-entity-number) | [Brazil National IDRG](entity-categories.md#type-brazil-national-idrg) |
+| [Bulgaria Uniform Civil Number](entity-categories.md#type-bulgaria-uniform-civil-number) | [Canada Bank Account Number](entity-categories.md#type-canada-bank-account-number) | [Canada Drivers License Number](entity-categories.md#type-canada-drivers-license-number) |
+| [Canada Health Service Number](entity-categories.md#type-canada-health-service-number) | [Canada Passport Number](entity-categories.md#type-canada-passport-number) | [Canada Personal Health Identification](entity-categories.md#type-canada-personal-health-identification) |
+| [Canada Social Insurance Number](entity-categories.md#type-canada-social-insurance-number) | [Canada Social Identification Number 🆕](entity-categories.md#type-canada-social-identification-number-preview) | [Chile Identity Card Number](entity-categories.md#type-chile-identity-card-number) |
+| [China Resident Identity Card Number](entity-categories.md#type-china-resident-identity-card-number) | [City 🆕](entity-categories.md#type-city-preview) | [Credit Card Number](entity-categories.md#type-credit-card-number) |
+| [Croatia Identity Card Number](entity-categories.md#type-croatia-identity-card-number) | [City 🆕](entity-categories.md#type-city-preview) |[Croatia National ID Number](entity-categories.md#type-croatia-national-id-number) |
+| [Croatia Personal Identification Number](entity-categories.md#type-croatia-personal-identification-number) | [CVV 🆕](entity-categories.md#type-card-verification-value-cvv-preview) | [Cyprus Identity Card](entity-categories.md#type-cyprus-identity-card) |
+| [Cyprus Tax Identification Number](entity-categories.md#type-cyprus-tax-identification-number) | [Date](entity-categories.md#type-date) | [Date Of Birth 🆕](entity-categories.md#type-date-of-birth-preview) |
+| [Denmark Personal Identification Number](entity-categories.md#type-denmark-personal-identification-number) | [Drivers License Number 🆕](entity-categories.md#type-drivers-license-number-preview) | [Email](entity-categories.md#type-email) | 
+| [Estonia Personal Identification Code](entity-categories.md#type-estonia-personal-identification-code) | [European Union Debit Card Number](entity-categories.md#type-european-union-debit-card-number) | [European Union Drivers License Number](entity-categories.md#type-european-union-drivers-license-number) |
+| [European Union GPS Coordinates](entity-categories.md#type-european-union-gps-coordinates) | [European Union National Identification Number](entity-categories.md#type-european-union-national-identification-number) | [European Union Passport Number](entity-categories.md#type-european-union-passport-number) |
+| [European Union Social Security Number](entity-categories.md#type-european-union-social-security-number) | [European Union Tax Identification Number](entity-categories.md#type-european-union-tax-identification-number) | [Expiration Date 🆕](entity-categories.md#type-expiration-date-preview) |
+| [Finland European Health Number](entity-categories.md#type-finland-european-health-number) | [Finland National ID](entity-categories.md#type-finland-national-id) | [Finland Passport Number](entity-categories.md#type-finland-passport-number) |
+| [France Drivers License Number](entity-categories.md#type-france-drivers-license-number) | [France National ID](entity-categories.md#type-france-national-id) | [France Passport Number](entity-categories.md#type-france-passport-number) |
+| [France Social Security Number](entity-categories.md#type-france-social-security-number) | [France Tax Identification Number](entity-categories.md#type-france-tax-identification-number) | [France Value Added Tax Number](entity-categories.md#type-france-value-added-tax-number) |
+| [Germany Drivers License Number](entity-categories.md#type-germany-drivers-license-number) | [Germany Identity Card Number](entity-categories.md#type-germany-identity-card-number) | [Germany Passport Number](entity-categories.md#type-germany-passport-number) |
+| [Germany Tax Identification Number](entity-categories.md#type-germany-tax-identification-number) | [Germany Value Added Number](entity-categories.md#type-germany-value-added-number) | [GPE 🆕](entity-categories.md#type-geopolitical-entity-gpe-preview) |
+| [Greece National ID Card](entity-categories.md#type-greece-national-id-card) | [Greece Tax Identification Number](entity-categories.md#type-greece-tax-identification-number) | [Hong Kong SAR Identity Card Number](entity-categories.md#type-hong-kong-sar-identity-card-number) |
+| [Hungary Personal Identification Number](entity-categories.md#type-hungary-personal-identification-number) | [Hungary Value Added Number](entity-categories.md#type-hungary-value-added-number) | [India Permanent Account](entity-categories.md#type-india-permanent-account) |
+| [India Unique Identification Number](entity-categories.md#type-india-unique-identification-number) | [Indonesia Identity Card Number](entity-categories.md#type-indonesia-identity-card-number) | [International Banking Account Number](entity-categories.md#type-international-banking-account-number) |
+| [IP Address](entity-categories.md#type-ip-address) | [Ireland Personal Public Service Number](entity-categories.md#type-ireland-personal-public-service-number) | [Israel Bank Account Number](entity-categories.md#type-israel-bank-account-number) |
+| [Israel National ID](entity-categories.md#type-israel-national-id) | [Italy Drivers License Number](entity-categories.md#type-italy-drivers-license-number) | [Italy Fiscal Code](entity-categories.md#type-italy-fiscal-code) |
+| [Italy Value Added Tax Number](entity-categories.md#type-italy-value-added-tax-number) | [Japan Bank Account Number](entity-categories.md#type-japan-bank-account-number) | [Japan Drivers License Number](entity-categories.md#type-japan-drivers-license-number) |
+| [Japan My Number Corporate](entity-categories.md#type-japan-my-number-corporate) | [Japan My Number Personal](entity-categories.md#type-japan-my-number-personal) | [Japan Passport Number](entity-categories.md#type-japan-passport-number) |
+| [Japan Residence Card Number](entity-categories.md#type-japan-residence-card-number) | [Japan Resident Registration Number](entity-categories.md#type-japan-resident-registration-number) | [Japan Social Insurance Number](entity-categories.md#type-japan-social-insurance-number) |
+| [Latvia Personal Code](entity-categories.md#type-latvia-personal-code) | [License Plate 🆕](entity-categories.md#type-license-plate-preview) | [Lithuania Personal Code](entity-categories.md#type-lithuania-personal-code) |
+| [Location 🆕](entity-categories.md#type-location-preview) | [Luxembourg National Identification Number Natural](entity-categories.md#type-luxembourg-national-identification-number-natural) | [Luxembourg National Identification Number Non Natural](entity-categories.md#type-luxembourg-national-identification-number-non-natural) |
+| [Malaysia Identity Card Number](entity-categories.md#type-malaysia-identity-card-number) | [Malta Identity Card Number](entity-categories.md#type-malta-identity-card-number) | [Malta Tax ID Number](entity-categories.md#type-malta-tax-id-number) |
+| [Netherlands Citizens Service Number](entity-categories.md#type-netherlands-citizens-service-number) | [Netherlands Tax Identification Number](entity-categories.md#type-netherlands-tax-identification-number) | [Netherlands Value Added Tax Number](entity-categories.md#type-netherlands-value-added-tax-number) |
+| [New Zealand Bank Account Number](entity-categories.md#type-new-zealand-bank-account-number) | [New Zealand Drivers License Number](entity-categories.md#type-new-zealand-drivers-license-number) | [New Zealand Inland Revenue Number](entity-categories.md#type-new-zealand-inland-revenue-number) |
+| [New Zealand Ministry Of Health Number](entity-categories.md#type-new-zealand-ministry-of-health-number) | [New Zealand Social Welfare Number](entity-categories.md#type-new-zealand-social-welfare-number) | [Norway Identity Number](entity-categories.md#type-norway-identity-number) |
+| [Organization](entity-categories.md#type-organization) | [Passport Number 🆕](entity-categories.md#type-passport-number-preview) | [Password 🆕](entity-categories.md#type-password-preview) |
+| [Person](entity-categories.md#type-person) | [Philippines Unified Multi Purpose ID Number](entity-categories.md#type-philippines-unified-multi-purpose-id-number) | [Phone Number](entity-categories.md#type-phone-number) |
+| [Poland Identity Card](entity-categories.md#type-poland-identity-card) | [Poland National ID](entity-categories.md#type-poland-national-id) | [Poland Passport Number](entity-categories.md#type-poland-passport-number) |
+| [Poland REGON Number](entity-categories.md#type-poland-regon-number) | [Poland Tax Identification Number](entity-categories.md#type-poland-tax-identification-number) | [Portugal Tax Identification Number](entity-categories.md#type-portugal-tax-identification-number) |
+| [Romania Personal Numerical Code](entity-categories.md#type-romania-personal-numerical-code) | [Russia Passport Number Domestic](entity-categories.md#type-russia-passport-number-domestic) | [Russia Passport Number International](entity-categories.md#type-russia-passport-number-international) |
+| [Saudi Arabia National ID](entity-categories.md#type-saudi-arabia-national-id) | [Singapore National Registration Identity Card Number](entity-categories.md#type-singapore-national-registration-identity-card-number) | [Slovakia Personal Number](entity-categories.md#type-slovakia-personal-number) |
+| [Slovenia Tax Identification Number](entity-categories.md#type-slovenia-tax-identification-number) | [Slovenia Unique Master Citizen Number](entity-categories.md#type-slovenia-unique-master-citizen-number) | [Sort Code 🆕](entity-categories.md#type-sort-code-preview) |
+| [South Africa Identification Number](entity-categories.md#type-south-africa-identification-number) | [South Korea Drivers License Number 🆕](entity-categories.md#type-south-korea-drivers-license-number-preview) | [South Korea Passport Number 🆕](entity-categories.md#type-south-korea-passport-number-preview) |
+| [South Korea Resident Registration Number](entity-categories.md#type-south-korea-resident-registration-number) | [South Korea Social Security Number 🆕](entity-categories.md#type-south-korea-social-security-number-preview) | [Spain DNI](entity-categories.md#type-spain-dni) |
+|[Spain Social Security Number](entity-categories.md#type-spain-social-security-number) | [Spain Tax Identification Number](entity-categories.md#type-spain-tax-identification-number) | [SQL Server Connection String](entity-categories.md#type-sql-server-connection-string) |
+| [State 🆕](entity-categories.md#type-state-preview) | [Sweden National ID](entity-categories.md#type-sweden-national-id) | [Sweden Passport Number](entity-categories.md#type-sweden-passport-number) |
+|[Sweden Tax Identification Number](entity-categories.md#type-sweden-tax-identification-number) | [SWIFT Code](entity-categories.md#type-swift-code) | [Taiwanese ID](entity-categories.md#type-taiwanese-id) |
+| [Taiwan Passport Number](entity-categories.md#type-taiwan-passport-number) | [Taiwan Resident Certificate](entity-categories.md#type-taiwan-resident-certificate) | [Thailand Population Identification Code](entity-categories.md#type-thailand-population-identification-code) |
+| [Türkiye National Identification Number](entity-categories.md#type-türkiye-national-identification-number) | [Ukraine Passport Number Domestic](entity-categories.md#type-ukraine-passport-number-domestic) | [Ukraine Passport Number International](entity-categories.md#type-ukraine-passport-number-international) |
+| [United Kingdom Drivers License Number](entity-categories.md#type-united-kingdom-drivers-license-number) | [United Kingdom Electoral Roll Number](entity-categories.md#type-united-kingdom-electoral-roll-number) | [United Kingdom National Health Number](entity-categories.md#type-united-kingdom-national-health-number) |
+| [United Kingdom National Insurance Number](entity-categories.md#type-united-kingdom-national-insurance-number) | [United Kingdom Unique Taxpayer Number](entity-categories.md#type-united-kingdom-unique-taxpayer-number) | [United States Bank Account Number](entity-categories.md#type-united-states-bank-account-number) |
+| [United States Drivers License Number](entity-categories.md#type-united-states-drivers-license-number) | [United States Drug Enforcement Agency Number](entity-categories.md#type-united-states-drug-enforcement-agency-number) |[United States Individual Taxpayer Identification](entity-categories.md#type-united-states-individual-taxpayer-identification) |
+| [United States Medicare Beneficiary Id 🆕](entity-categories.md#type-united-states-medicare-beneficiary-identification-preview) | [United States Social Security Number](entity-categories.md#type-united-states-social-security-number) | [United States/United Kingdom Passport Number](entity-categories.md#type-united-statesunited-kingdom-passport-number) |
+| [URL](entity-categories.md#type-url) | [VIN 🆕](entity-categories.md#type-vin-preview) | [ZipCode 🆕](entity-categories.md#type-zipcode-preview) |
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "PIIエンティティのカテゴリリストの大幅な更新"
}
```

### Explanation
この変更は、`entity-categories-list.md`ファイルにおける個人を特定可能な情報（PII）エンティティのカテゴリリストの大規模な更新を反映しています。具体的には、60行が削除され、60行が新たに追加されるという形で、合計で120行の変更が行われました。この変更により、各エンティティの説明やリンクが修正されており、新しいエンティティの追加や古い情報の削除が行われています。この更新は、PIIエンティティの情報提供をより正確かつ包括的にすることを目的としており、ユーザーにとっての利便性を向上させる重要な変更となっています。

## articles/ai-services/language-service/personally-identifiable-information/how-to/redact-text-pii.md{#item-9e48af}

<details>
<summary>Diff</summary>
````diff
@@ -10,11 +10,11 @@ ms.date: 11/18/2025
 ms.author: lajanuar
 ms.custom: language-service-pii
 ---
+<!-- markdownlint-disable MD025 -->
 # Detect and redact Personally Identifying Information in text
 
 Azure Language in Foundry Tools is a cloud-based service that applies Natural Language Processing (NLP) features to text-based data. The PII feature can evaluate unstructured text, extract, and redact sensitive information (PII) and health information (PHI) in text across several [predefined categories](../concepts/entity-categories.md).
 
-
 ## Development options
 
 [!INCLUDE [development options](../includes/development-options.md)]
@@ -42,16 +42,21 @@ Starting with version `2025-11-15-preview` and onward, you can specify the `reda
 The policy field accepts four policy types:
 
 > [!div class="checklist"]
+>
 > * [`SyntheticReplacement 🆕`](#syntheticreplacement-policy-type-)
 > * [`CharacterMask` (default)](#charactermask-policy-type)
 > * [`NoMask`](#nomask-policy-type)
 > * [`EntityMask`](#entitymask-policy-type)
 
 For more information, *see* [REST API PII task parameters](/rest/api/language/analyze-text/analyze-text/analyze-text?view=rest-language-analyze-text-2025-11-15-preview&preserve-view=true&tabs=HTTP#piitaskparameters).
 
+<!-- markdownlint-disable MD001 -->
 ##### syntheticReplacement policy type 🆕
 
-The **syntheticReplacement** policy type** replaces a detected PII entity with a replacement value. For instance, an input like "John Doe received a call from 424-878-9193." can be transformed into "Sam Johnson received a call from 401-255-6901." These substitutes are randomly selected from a predefined set of alternative values.
+> [!IMPORTANT]
+> The Azure Language in Foundry Tools Text Personally Identifiable Information (PII) detection **anonymization feature** (synthetic replacement) is currently available in `preview` and licensed to you as part of your Azure subscription. Your use of this feature is subject to the terms applicable to **Previews** as described in the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms) and the [Microsoft Products and Services Data Protection Addendum (DPA)](https://www.microsoft.com/licensing/docs/view/microsoft-products-and-services-data-protection-addendum-dpa).
+
+The **syntheticReplacement** policy type replaces a detected PII entity with a replacement value. For instance, an input like "John Doe received a call from 424-878-9193." can be transformed into "Sam Johnson received a call from 401-255-6901." These substitutes are randomly selected from a predefined set of alternative values.
 
    ```bash
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PIIテキストの赤外線処理に関する情報の追加"
}
```

### Explanation
この変更は、`redact-text-pii.md`ファイルにおける個人を特定可能な情報（PII）の赤外線処理に関する内容の更新を反映しています。具体的には、7行が新たに追加され、2行が削除され、合計9行の変更が行われました。主な改訂には、新たなポリシータイプ「syntheticReplacement」の重要性が強調されています。このポリシーは、検出されたPIIエンティティを代替値で置き換える機能を持っており、使用に関する条件が明示されています。また、マークダウンLintに関するコメントが追加され、文書の整形が改善されています。この更新により、ユーザーは新たな機能とその利用条件をより明確に理解できるようになります。

## articles/ai-services/language-service/personally-identifiable-information/overview.md{#item-8a6932}

<details>
<summary>Diff</summary>
````diff
@@ -11,61 +11,25 @@ ms.author: lajanuar
 ms.custom: language-service-pii
 ---
 
+<!-- markdownlint-disable MD025 -->
 # What is Azure Language PII detection?
 
-> [!IMPORTANT]
-> The Azure Language in Foundry Tools Text Personally Identifiable Information (PII) detection **anonymization feature** (synthetic replacement) is currently available in `preview` and licensed to you as part of your Azure subscription. Your use of this feature is subject to the terms applicable to **Previews** as described in the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms) and the [Microsoft Products and Services Data Protection Addendum (DPA)](https://www.microsoft.com/licensing/docs/view/microsoft-products-and-services-data-protection-addendum-dpa).
-
 Azure Language in Foundry Tools Personally Identifiable Information (PII) detection is a feature offered by [Azure Language](../overview.md). The PII detection service is a cloud-based API that utilizes machine learning and AI algorithms to help you develop intelligent applications with advanced natural language understanding. Azure Language PII detection uses Named Entity Recognition (NER) to **identify and redact** sensitive information from input data. The service classifies sensitive personal data into predefined categories. These categories include phone numbers, email addresses, and identification documents. This classification helps to efficiently detect and eliminate such information.
 
 > [!TIP]
 > Try PII detection [in Microsoft Foundry portal](https://ai.azure.com/). There you can [utilize a currently existing Language Studio resource or create a new Foundry resource](../../../ai-services/connect-services-foundry-portal.md).
 
-## What's new
-
-**The 2025-11-15-preview version introduces the following new PII task parameters**:
-
-* [**Multiple redaction policies**](how-to/redact-text-pii.md#redaction-policies) offer the ability to apply various redaction approaches within a single request:
-
-    * [SyntheticReplacementPolicyType 🆕](how-to/redact-text-pii.md#syntheticreplacement-policy-type-)
-    * [CharacterMaskPolicyType (default)](how-to/redact-text-pii.md#charactermask-policy-type)
-    * [NoMaskPolicyType](how-to/redact-text-pii.md#nomask-policy-type)
-    * [EntityMaskPolicyType](how-to/redact-text-pii.md#entitymask-policy-type)
+## Video demonstration
 
-* [**Configurable confidence threshold**](how-to/redact-text-pii.md#confidencescorethreshold-) enables you to set a minimum confidence score. Entities are only included in the output if their confidence score meets or exceeds the specified threshold.
+In this video, we introduce the PII detection service and show you how it detects and redacts sensitive data across text, documents, and conversational transcripts. We cover:
 
-* [**Disable type validation enforcement**](how-to/redact-text-pii.md#disableentityvalidation) enables you to bypass the entity type validation. By default, the service enforces validation across multiple entity types to ensure data integrity and minimize false positives. Disabling this enforcement can enhance operational efficiency in cases where strict validation isn't required.
+* How to try the service in the Azure Foundry portal playground
+* Key customization options for entity types, masking styles, and exclusions
+* Why PII protection matters and the business impact of data breaches
 
-* The following entities are available in preview:
+> [!VIDEO https://learn-video.azurefd.net/vod/player?id=17262a01-0c8c-40fa-98e3-826b766d5db4]
 
-    * [Airport](concepts/entity-categories.md#type-airport-preview)
-    * [DateOfBirth](concepts/entity-categories.md#type-date-of-birth-preview)
-    * [BankAccountNumber](concepts/entity-categories.md#type-bank-account-number-preview)
-    * [CASocialIdentificationNumber](concepts/entity-categories.md#type-canada-social-identification-number-preview)
-    * [CVV (Card Verification Value )](concepts/entity-categories.md#type-card-verification-value-cvv-preview)
-    * [City](concepts/entity-categories.md#type-city-preview)
-    * [PassportNumber](concepts/entity-categories.md#type-passport-number-preview)
-    * [DriversLicenseNumber](concepts/entity-categories.md#type-drivers-license-number-preview)
-    * [ExpirationDate](concepts/entity-categories.md#type-expiration-date-preview)
-    * [Geopolitical Entity](concepts/entity-categories.md#type-geopolitical-entity-gpe-preview)
-    * [KRDriversLicenseNumber](concepts/entity-categories.md#type-south-korea-drivers-license-number-preview)
-    * [KRPassportNumber ](concepts/entity-categories.md#type-south-korea-passport-number-preview)
-    * [KRSocialSecurityNumber ](concepts/entity-categories.md#type-south-korea-social-security-number-preview)
-    * [LicensePlate](concepts/entity-categories.md#type-license-plate-preview)
-    * [Location](concepts/entity-categories.md#type-location-preview)
-    * [Password](concepts/entity-categories.md#type-password-preview)
-    * [SortCode](concepts/entity-categories.md#type-sort-code-preview)
-    * [State](concepts/entity-categories.md#type-state-preview)
-    * [USMedicareBeneficiaryId](concepts/entity-categories.md#type-united-states-medicare-beneficiary-identification-preview)
-    * [VIN (vehicle identification number)](concepts/entity-categories.md#type-vin-preview)
-    * [ZipCode](concepts/entity-categories.md#type-zipcode-preview)
-
-* **Conversational PII detection models (both version `2024-11-01-preview` and `GA`)** are updated to provide enhanced AI quality and accuracy. The numeric identifier entity type now also includes Drivers License and Medicare Beneficiary Identifier.
-
-   > [!div class="checklist"]
-   > * As of June 2024, we now provide General Availability support for the Conversational PII service (English-language only).
-   > * Customers can now redact transcripts, chats, and other text written in a conversational style.
-   > * These capabilities provide better confidence in AI quality. They also offer Azure SLA support, production environment support, and enterprise-grade security.
+Closed captions are available for this video.
 
 ## Capabilities
 
@@ -75,7 +39,6 @@ Azure Language in Foundry Tools Personally Identifiable Information (PII) detect
 * [Conversation PII detection](how-to/redact-conversation-pii.md), a specialized model designed to handle speech transcriptions and the informal, conversational tone found in meeting and call transcripts.
 * [Native Document PII detection](how-to/redact-document-pii.md) for processing structured document files.
 
-
 ### [Text PII](#tab/text-pii)
 
 Language is a cloud-based service that applies Natural Language Processing (NLP) features to detect categories of personal information (PII) in text-based data. This documentation contains the following types:
@@ -167,5 +130,6 @@ An AI system includes not only the technology, but also the people who use it, t
 ## Next steps
 
 There are two ways to get started using the entity linking feature:
+
 * [Foundry](../../../ai-foundry/what-is-foundry.md) is a web-based platform that lets you use several Language features without needing to write code.
 * The [quickstart article](quickstart.md) for instructions on making requests to the service using the REST API and client library SDK.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "PII検出に関する概要の大幅な更新"
}
```

### Explanation
この変更は、`overview.md`ファイルにおける個人を特定可能な情報（PII）検出に関する情報の大規模な見直しを反映しています。9行が追加され、45行が削除され、合計54行の変更が行われました。主な内容としては、Azure Language PII検出サービスの概要が簡潔に再構成され、主に動画デモが追加されています。この動画では、PII検出サービスの利用方法やその機能について詳細に解説されています。

歌手のバランスを向上させ、重要な情報をシンプルに整理したことで、ユーザーがこのサービスの利点をより理解しやすくなっています。従来の情報やセクションが大幅に削除され、関連性を保ちながら情報量が減少し、更新の意図がより明確に伝わるようになっています。また、過去のバージョンでの新機能に関する詳細も削除され、現行の機能とその利用方法に焦点を当てた形となっています。


