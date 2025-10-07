---
date: '2025-10-07'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6633d97...MicrosoftDocs:7e5f65d
summary: この一連のアップデートには、Azure AI Languageサービスの新機能導入と既存ドキュメントの最適化が含まれています。特に個人識別情報（PII）と保護された健康情報（PHI）の検出機能に大幅な改善があり、エンティティ認識の用途が広がりました。また、新しいPython
  SDKのリリースや命名エンティティ認識（NER）機能のプレイグラウンド統合も重要な更新点です。直バ破壊的変更は報告されていませんが、文書の改訂によりAPIの呼び出しに影響が出る可能性があります。このアップデートにより、Azure
  AIの言語サービスの機能が大幅に強化され、ユーザーは個人情報をより効果的に管理できるようになります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6633d97...MicrosoftDocs:7e5f65d){target="_blank"}

<format>
# ハイライト
この一連のアップデートには、Azure AI Languageサービスにおける新機能の導入と既存ドキュメントの最適化が含まれています。特に、個人識別情報（PII）と保護された健康情報（PHI）の検出機能において大幅な改善が行われ、エンティティ認識の用途が広がっています。新しいPython SDKのリリースや、命名エンティティ認識（NER）機能のプレイグラウンド統合も重要な更新点です。

## 新機能
- 個人識別情報（PII）エンティティカテゴリリストの追加
- CQAデプロイメント機能とカスタムNER機能の統合
- 新しいPython SDKのリリース

## 破壊的変更
- 直接の破壊的変更は報告されていませんが、文書の大規模な改訂が行われているため、APIや機能の呼び出し方に影響が出る可能性があります。

## その他の更新
- ドキュメントのタイトル、説明、リンクの修正
- 目次構成の改善とWhat's Newページの更新

# インサイト
このアップデートはAzure AIが提供する言語サービス機能、特にPIIやPHIの検出能力を大幅に強化するものです。これにより、ユーザーは個人情報をより効果的に管理できるようになり、さらにインテリジェントエージェントとしての機能を強化できる新しい手段が提供されています。

まず、名前付きエンティティ認識の部分で、カテゴリが一貫するように住所が「ロケーション」に、空港が「ロケーション」に変わりタグとして区別が加えられ、直感的に理解しやすく更新されています。これにより、エンティティの分類が明確になり、ユーザーの情報捜索がスムーズに。

PII関連では、PIIのみならずPHIも対象としたエンティティカテゴリの改訂が行われ、多数のエンティティタイプとその構成が整理されました。ユーザードキュメントがリフレッシュされ、これが実際の利用時の精度向上に寄与します。

また、CQAやNERの機能がFoundryプレイグラウンドと組み合わさり、エージェントのデプロイが容易に。これにより、実用的なAIソリューションの開発速度が大幅に向上します。

さらには、新しいPython SDKであるazure-ai-textanalyticsとそのオーサリング版が登場し、これによりさまざまなテキスト解析機能の統合が可能になります。これらの新機能は、競争の激しいマーケットにおけるAIの実行速度をブーストする要因となります。

このような大幅な機能強化は、Azureの言語サービスを利用する開発者にとって、精度の向上と新しい業務フローの準備の加速をもたらすものであり、今後のAIサービスの進化において重要なマイルストーンとなるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [named-entity-categories.md](#item-a4a7f1) | minor update | エンティティカテゴリの修正 | modified | 3 | 3 | 6 | 
| [entity-categories-list.md](#item-05522d) | new feature | 個人識別情報（PII）エンティティカテゴリリストの追加 | added | 76 | 0 | 76 | 
| [entity-categories.md](#item-ba2623) | minor update | PIIおよびPHI検出のエンティティカテゴリの変更 | modified | 708 | 1111 | 1819 | 
| [overview.md](#item-8a6932) | minor update | PII検出機能の概要におけるエンティティ情報の修正 | modified | 3 | 3 | 6 | 
| [toc.yml](#item-12f1f0) | minor update | TOCにおけるエンティティカテゴリおよびリストの更新 | modified | 3 | 1 | 4 | 
| [whats-new.md](#item-69b272) | minor update | What's Newページのアップデート | modified | 18 | 0 | 18 | 


# Modified Contents
## articles/ai-services/language-service/named-entity-recognition/concepts/named-entity-categories.md{#item-a4a7f1}

<details>
<summary>Diff</summary>
````diff
@@ -48,7 +48,7 @@ The [NER language support](../language-support.md) page lists all languages avai
 |[URL](#type-url)|[Volume](#type-volume)|[Weight](#type-weight)||
 
 ### Type: Address
-##### Category: Location
+##### Category: Address
 
 |Entity|Tags|Detail|
 |---|---|---|
@@ -64,11 +64,11 @@ The [NER language support](../language-support.md) page lists all languages avai
 
 
 ### Type: Airport
-##### Category: Airport
+##### Category: Location
 
 |Entity|Tags|Detail|
 |---|---|---|
-|**Airport**|Airport|A designated location equipped with facilities for the landing, takeoff, and maintenance of aircraft.  |
+|**Airport**|Location, Airport|A designated location equipped with facilities for the landing, takeoff, and maintenance of aircraft.  |
 
 ### Type: Area
 ##### Category: Quantity
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンティティカテゴリの修正"
}
```

### Explanation
この変更では、「名前付きエンティティ認識」に関するドキュメント内のカテゴリ名に関する軽微な更新が行われています。具体的には、以下の変更が含まれます：

1. 「住所」のカテゴリ名が「ロケーション」として修正されました。
2. 「空港」のカテゴリ名も「ロケーション」に変更され、タグ欄に「空港」が追加されました。

このように、エンティティの分類に一貫性を持たせるための修正が行われており、利用者が情報をより理解しやすくすることを目的としています。全体として、3行の追加と3行の削除があり、合計6行の変更が施されています。ドキュメントの内容は、エンティティの詳細を記述するためのテーブル構造を保ったまま、カテゴリ名における表現を最適化しています。

## articles/ai-services/language-service/personally-identifiable-information/concepts/entity-categories-list.md{#item-05522d}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,76 @@
+---
+title: Entity categories list recognized by Personally Identifiable Information (PII) detection in Azure AI Language
+titleSuffix: Azure AI services
+description: View a list of entity types the PII feature can detect and identify within unstructured text.
+author: laujan
+manager: nitinme
+ms.service: azure-ai-language
+ms.topic: conceptual
+ms.date: 10/01/2025
+ms.author: lajanuar
+ms.custom:
+  - language-service-pii
+  - sfi-ropc-nochange
+---
+
+# Recognized PII entities list
+
+| Entity | Entity | Entity |
+|--|--|--|
+| [ABA Routing Number](entity-categories.md#type-aba-routing-number) | [Address](entity-categories.md#type-address) | [Age](entity-categories.md#type-age) |
+| [Argentina National Identity Number](entity-categories.md#type-argentina-national-identity-number) | [Australia Bank Account Number](entity-categories.md#type-australia-bank-account-number) | [Australia Business Number](entity-categories.md#type-australia-business-number) |
+| [Australia Company Number](entity-categories.md#type-australia-company-number) | [Australia Drivers License Number](entity-categories.md#type-australia-drivers-license-number) | [Australia Medical Account Number](entity-categories.md#type-australia-medical-account-number) |
+| [Australia Passport Number](entity-categories.md#type-australia-passport-number) | [Australia Tax File Number](entity-categories.md#type-australia-tax-file-number) | [Austria Identity Card](entity-categories.md#type-austria-identity-card) |
+| [Austria Tax Identification Number](entity-categories.md#type-austria-tax-identification-number) | [Austria Value Added Tax Number](entity-categories.md#type-austria-value-added-tax-number) | [Azure Document DB Auth Key](entity-categories.md#type-azure-document-db-auth-key) |
+| [Azure IAAS Database Connection And SQL String](entity-categories.md#type-azure-iaas-database-connection-and-sql-string) | [Azure IoT Connection String](entity-categories.md#type-azure-iot-connection-string) | [Azure Publish Setting Password](entity-categories.md#type-azure-publish-setting-password) |
+| [Azure Redis Cache String](entity-categories.md#type-azure-redis-cache-string) | [Azure SAS](entity-categories.md#type-azure-sas) | [Azure Service Bus String](entity-categories.md#type-azure-service-bus-string) |
+| [Azure Storage Account Generic](entity-categories.md#type-azure-storage-account-generic) | [Azure Storage Account Key](entity-categories.md#type-azure-storage-account-key) | [Bank Account Number 🆕](entity-categories.md#type-bank-account-number-preview) |
+| [Belgium National Number](entity-categories.md#type-belgium-national-number) | [Belgium Value Added Tax Number](entity-categories.md#type-belgium-value-added-tax-number) | [Brazil CPF Number](entity-categories.md#type-brazil-cpf-number) |
+| [Brazil Legal Entity Number](entity-categories.md#type-brazil-legal-entity-number) | [Brazil National IDRG](entity-categories.md#type-brazil-national-idrg) | [Bulgaria Uniform Civil Number](entity-categories.md#type-bulgaria-uniform-civil-number) |
+| [Canada Bank Account Number](entity-categories.md#type-canada-bank-account-number) | [Canada Drivers License Number](entity-categories.md#type-canada-drivers-license-number) | [Canada Health Service Number](entity-categories.md#type-canada-health-service-number) |
+| [Canada Passport Number](entity-categories.md#type-canada-passport-number) | [Canada Personal Health Identification](entity-categories.md#type-canada-personal-health-identification) | [Canada Social Insurance Number](entity-categories.md#type-canada-social-insurance-number) |
+| [Chile Identity Card Number](entity-categories.md#type-chile-identity-card-number) | [China Resident Identity Card Number](entity-categories.md#type-china-resident-identity-card-number) | [Credit Card Number](entity-categories.md#type-credit-card-number) |
+| [Croatia Identity Card Number](entity-categories.md#type-croatia-identity-card-number) | [Croatia National ID Number](entity-categories.md#type-croatia-national-id-number) | [Croatia Personal Identification Number](entity-categories.md#type-croatia-personal-identification-number) |
+| [Cyprus Identity Card](entity-categories.md#type-cyprus-identity-card) | [Cyprus Tax Identification Number](entity-categories.md#type-cyprus-tax-identification-number) | [Czech Republic Personal Identity Number](entity-categories.md#type-czech-republic-personal-identity-number) |
+| [Date](entity-categories.md#type-date) | [Date Of Birth 🆕](entity-categories.md#type-date-of-birth-preview) | [Denmark Personal Identification Number](entity-categories.md#type-denmark-personal-identification-number) |
+| [Drivers License Number 🆕](entity-categories.md#type-drivers-license-number-preview) | [Email](entity-categories.md#type-email) | [Estonia Personal Identification Code](entity-categories.md#type-estonia-personal-identification-code) |
+| [European Union Debit Card Number](entity-categories.md#type-european-union-debit-card-number) | [European Union Drivers License Number](entity-categories.md#type-european-union-drivers-license-number) | [European Union GPS Coordinates](entity-categories.md#type-european-union-gps-coordinates) |
+| [European Union National Identification Number](entity-categories.md#type-european-union-national-identification-number) | [European Union Passport Number](entity-categories.md#type-european-union-passport-number) | [European Union Social Security Number](entity-categories.md#type-european-union-social-security-number) |
+| [European Union Tax Identification Number](entity-categories.md#type-european-union-tax-identification-number) | [Finland European Health Number](entity-categories.md#type-finland-european-health-number) | [Finland National ID](entity-categories.md#type-finland-national-id) |
+| [Finland Passport Number](entity-categories.md#type-finland-passport-number) | [France Drivers License Number](entity-categories.md#type-france-drivers-license-number) | [France Health Insurance Number](entity-categories.md#type-france-health-insurance-number) |
+| [France National ID](entity-categories.md#type-france-national-id) | [France Passport Number](entity-categories.md#type-france-passport-number) | [France Social Security Number](entity-categories.md#type-france-social-security-number) |
+| [France Tax Identification Number](entity-categories.md#type-france-tax-identification-number) | [France Value Added Tax Number](entity-categories.md#type-france-value-added-tax-number) | [Germany Drivers License Number](entity-categories.md#type-germany-drivers-license-number) |
+| [Germany Identity Card Number](entity-categories.md#type-germany-identity-card-number) | [Germany Passport Number](entity-categories.md#type-germany-passport-number) | [Germany Tax Identification Number](entity-categories.md#type-germany-tax-identification-number) |
+| [Germany Value Added Number](entity-categories.md#type-germany-value-added-number) | [Greece National ID Card](entity-categories.md#type-greece-national-id-card) | [Greece Tax Identification Number](entity-categories.md#type-greece-tax-identification-number) |
+| [Hong Kong SAR Identity Card Number](entity-categories.md#type-hong-kong-sar-identity-card-number) | [Hungary Personal Identification Number](entity-categories.md#type-hungary-personal-identification-number) | [Hungary Tax Identification Number](entity-categories.md#type-hungary-tax-identification-number) |
+| [Hungary Value Added Number](entity-categories.md#type-hungary-value-added-number) | [India Permanent Account](entity-categories.md#type-india-permanent-account) | [India Unique Identification Number](entity-categories.md#type-india-unique-identification-number) |
+| [Indonesia Identity Card Number](entity-categories.md#type-indonesia-identity-card-number) | [International Banking Account Number](entity-categories.md#type-international-banking-account-number) | [IP Address](entity-categories.md#type-ip-address) |
+| [Ireland Personal Public Service Number](entity-categories.md#type-ireland-personal-public-service-number) | [Israel Bank Account Number](entity-categories.md#type-israel-bank-account-number) | [Israel National ID](entity-categories.md#type-israel-national-id) |
+| [Italy Drivers License Number](entity-categories.md#type-italy-drivers-license-number) | [Italy Fiscal Code](entity-categories.md#type-italy-fiscal-code) | [Italy Value Added Tax Number](entity-categories.md#type-italy-value-added-tax-number) |
+| [Japan Bank Account Number](entity-categories.md#type-japan-bank-account-number) | [Japan Drivers License Number](entity-categories.md#type-japan-drivers-license-number) | [Japan My Number Corporate](entity-categories.md#type-japan-my-number-corporate) |
+| [Japan My Number Personal](entity-categories.md#type-japan-my-number-personal) | [Japan Passport Number](entity-categories.md#type-japan-passport-number) | [Japan Residence Card Number](entity-categories.md#type-japan-residence-card-number) |
+| [Japan Resident Registration Number](entity-categories.md#type-japan-resident-registration-number) | [Japan Social Insurance Number](entity-categories.md#type-japan-social-insurance-number) | [Latvia Personal Code](entity-categories.md#type-latvia-personal-code) |
+| [License Plate 🆕](entity-categories.md#type-license-plate-preview) | [Lithuania Personal Code](entity-categories.md#type-lithuania-personal-code) | [Luxembourg National Identification Number Natural](entity-categories.md#type-luxembourg-national-identification-number-natural) |
+| [Luxembourg National Identification Number Non Natural](entity-categories.md#type-luxembourg-national-identification-number-non-natural) | [Malaysia Identity Card Number](entity-categories.md#type-malaysia-identity-card-number) | [Malta Identity Card Number](entity-categories.md#type-malta-identity-card-number) |
+| [Malta Tax ID Number](entity-categories.md#type-malta-tax-id-number) | [Netherlands Citizens Service Number](entity-categories.md#type-netherlands-citizens-service-number) | [Netherlands Tax Identification Number](entity-categories.md#type-netherlands-tax-identification-number) |
+| [Netherlands Value Added Tax Number](entity-categories.md#type-netherlands-value-added-tax-number) | [New Zealand Bank Account Number](entity-categories.md#type-new-zealand-bank-account-number) | [New Zealand Drivers License Number](entity-categories.md#type-new-zealand-drivers-license-number) |
+| [New Zealand Inland Revenue Number](entity-categories.md#type-new-zealand-inland-revenue-number) | [New Zealand Ministry Of Health Number](entity-categories.md#type-new-zealand-ministry-of-health-number) | [New Zealand Social Welfare Number](entity-categories.md#type-new-zealand-social-welfare-number) |
+| [Norway Identity Number](entity-categories.md#type-norway-identity-number) | [Organization](entity-categories.md#type-organization) | [Passport Number 🆕](entity-categories.md#type-passport-number-preview) |
+| [Person](entity-categories.md#type-person) | [Philippines Unified Multi Purpose ID Number](entity-categories.md#type-philippines-unified-multi-purpose-id-number) | [Phone Number](entity-categories.md#type-phone-number) |
+| [Poland Identity Card](entity-categories.md#type-poland-identity-card) | [Poland National ID](entity-categories.md#type-poland-national-id) | [Poland Passport Number](entity-categories.md#type-poland-passport-number) |
+| [Poland REGON Number](entity-categories.md#type-poland-regon-number) | [Poland Tax Identification Number](entity-categories.md#type-poland-tax-identification-number) | [Portugal Citizen Card Number](entity-categories.md#type-portugal-citizen-card-number) |
+| [Portugal Tax Identification Number](entity-categories.md#type-portugal-tax-identification-number) | [Romania Personal Numerical Code](entity-categories.md#type-romania-personal-numerical-code) | [Russia Passport Number Domestic](entity-categories.md#type-russia-passport-number-domestic) |
+| [Russia Passport Number International](entity-categories.md#type-russia-passport-number-international) | [Saudi Arabia National ID](entity-categories.md#type-saudi-arabia-national-id) | [Singapore National Registration Identity Card Number](entity-categories.md#type-singapore-national-registration-identity-card-number) |
+| [Slovakia Personal Number](entity-categories.md#type-slovakia-personal-number) | [Slovenia Tax Identification Number](entity-categories.md#type-slovenia-tax-identification-number) | [Slovenia Unique Master Citizen Number](entity-categories.md#type-slovenia-unique-master-citizen-number) |
+| [Sort Code 🆕](entity-categories.md#type-sort-code-preview) | [South Africa Identification Number](entity-categories.md#type-south-africa-identification-number) | [South Korea Resident Registration Number](entity-categories.md#type-south-korea-resident-registration-number) |
+| [Spain DNI](entity-categories.md#type-spain-dni) | [Spain Social Security Number](entity-categories.md#type-spain-social-security-number) | [Spain Tax Identification Number](entity-categories.md#type-spain-tax-identification-number) |
+| [SQL Server Connection String](entity-categories.md#type-sql-server-connection-string) | [Sweden National ID](entity-categories.md#type-sweden-national-id) | [Sweden Passport Number](entity-categories.md#type-sweden-passport-number) |
+| [Sweden Tax Identification Number](entity-categories.md#type-sweden-tax-identification-number) | [SWIFT Code](entity-categories.md#type-swift-code) | [Switzerland Social Security Number](entity-categories.md#type-switzerland-social-security-number) |
+| [Taiwanese ID](entity-categories.md#type-taiwanese-id) | [Taiwan Passport Number](entity-categories.md#type-taiwan-passport-number) | [Taiwan Resident Certificate](entity-categories.md#type-taiwan-resident-certificate) |
+| [Thailand Population Identification Code](entity-categories.md#type-thailand-population-identification-code) | [Türkiye National Identification Number](entity-categories.md#type-türkiye-national-identification-number) | [Ukraine Passport Number Domestic](entity-categories.md#type-ukraine-passport-number-domestic) |
+| [Ukraine Passport Number International](entity-categories.md#type-ukraine-passport-number-international) | [United Kingdom Drivers License Number](entity-categories.md#type-united-kingdom-drivers-license-number) | [United Kingdom Electoral Roll Number](entity-categories.md#type-united-kingdom-electoral-roll-number) |
+| [United Kingdom National Health Number](entity-categories.md#type-united-kingdom-national-health-number) | [United Kingdom National Insurance Number](entity-categories.md#type-united-kingdom-national-insurance-number) | [United Kingdom Unique Taxpayer Number](entity-categories.md#type-united-kingdom-unique-taxpayer-number) |
+| [United States Bank Account Number](entity-categories.md#type-united-states-bank-account-number) | [United States Drivers License Number](entity-categories.md#type-united-states-drivers-license-number) | [United States Drug Enforcement Agency Number](entity-categories.md#type-united-states-drug-enforcement-agency-number) |
+| [United States Individual Taxpayer Identification](entity-categories.md#type-united-states-individual-taxpayer-identification) | [United States Social Security Number](entity-categories.md#type-united-states-social-security-number) | [United States/United Kingdom Passport Number](entity-categories.md#type-united-statesunited-kingdom-passport-number) |
+| [URL](entity-categories.md#type-url) | [VIN 🆕](entity-categories.md#type-vin-preview) |  |
+
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "個人識別情報（PII）エンティティカテゴリリストの追加"
}
```

### Explanation
この変更では、新しい「エンティティカテゴリリスト」が追加され、Azure AI Languageの個人識別情報（PII）検出機能が認識できるエンティティタイプの詳細が提供されています。具体的には、76行の新しいコンテンツが追加されており、さまざまな国や地域における個人識別情報のエンティティタイプが表形式で並列表示されています。

追加されたコンテンツには、各エンティティ名とそれに関連するハイパーリンクが含まれており、利用者は具体的なエンティティの詳細や定義に容易にアクセスできるようになっています。例えば、「住所」「運転免許証番号」「銀行口座番号」など、さまざまな形式の個人識別情報がリストアップされ、用途や地域に応じた具体的な情報が提供されます。

この新機能は、開発者がAzure AIのPII検出能力を理解し、適切に利用するための貴重なリソースとなることを目指しています。

## articles/ai-services/language-service/personally-identifiable-information/concepts/entity-categories.md{#item-ba2623}

<details>
<summary>Diff</summary>
````diff
@@ -1,1489 +1,1086 @@
 ---
-title: Entity categories recognized by Personally Identifiable Information (detection) in Azure AI Language
+title: Entity categories recognized by Personally Identifiable Information (PII) and Protected Health Information (PHI) detection in Azure AI Language
 titleSuffix: Azure AI services
-description: Learn about the entities the PII feature can recognize from unstructured text.
+description: Learn about the types of entities the PII feature can detect and identify within unstructured text.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 08/07/2025
+ms.date: 10/01/2025
 ms.author: lajanuar
 ms.custom:
   - language-service-pii
   - sfi-ropc-nochange
 ---
 
-# Supported PII entities
-Use this article to find the entity categories that the [personally identifiable information (PII) detection feature](../how-to-call.md) returns. This feature runs a predictive model to identify, categorize, and redact sensitive information from an input document.
+# Recognized **PII** and **PHI** entities
 
-The PII feature includes the ability to detect personal (`PII`) and health (`PHI`) information.
+The Personally Identifiable Information (PII) and Protected Health Information (PHI) detection APIs are cloud-based solutions that use artificial intelligence (AI) and machine learning to help you create smart applications with advanced natural language processing. The **PII** and **PHI** APIs effectively detect and removes sensitive information from input data by categorizing personal details into specific, predefined entity types. This comprehensive approach not only safeguards sensitive data to ensure full compliance with privacy regulations, but also enables applications to process and utilize information with enhanced security, reliability, and efficiency.
 
-## Supported entities
+> [!TIP]
+> Try PII detection in text or conversations using the [Azure AI Foundry](https://ai.azure.com/explore/language) language playground.
 
-> [!NOTE]
-> * To detect protected health information (PHI), use the `domain=phi` parameter and model version `2020-04-01` or later.
-> * The `Type` and `Subtype` are new designations introduced in the `2025-05-15-preview` version.
-
-The following entity categories are returned when you're sending API requests PII feature:
-
-# [Preview API](#tab/preview-api)
-
-## Type: Person
-
-This type contains the following entity:
-
-:::row:::
-    :::column span="":::
-        **Entity**
-
-        Person
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Names of people. Returned as both PII and PHI.
-
-        To get this entity type, add `Person` to the `piiCategories` parameter. `Person` is returned in the API response if detected.
-
-    :::column-end:::
-
-    :::column span="":::
-      **Supported languages**
-
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
-
-   :::column-end:::
-:::row-end:::
-
-# [GA API](#tab/ga-api)
-
-## Category: Person
-
-This category contains the following entity:
-
-:::row:::
-    :::column span="":::
-        **Entity**
-
-        Person
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Names of people. Returned as both PII and PHI.
-
-        To get this entity category, add `Person` to the `piiCategories` parameter. `Person` is returned in the API response if detected.
-
-    :::column-end:::
-
-    :::column span="":::
-      **Supported languages**
-
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
-
-   :::column-end:::
-:::row-end:::
-
----
-
-# [Preview API](#tab/preview-api)
-
-## Type: PersonType
-
-This type contains the following entity:
-
-
-:::row:::
-    :::column span="":::
-        **Entity**
-
-        PersonType
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Job types or roles held by a person.
-
-        To get this entity category, add `PersonType` to the `piiCategories` parameter. `PersonType` is returned in the API response if detected.
-
-    :::column-end:::
-
-    :::column span="":::
-      **Supported languages**
-
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
-
-   :::column-end:::
-:::row-end:::
-
-# [GA API](#tab/ga-api)
-
-## Category: PersonType
-
-This category contains the following entity:
-
-
-:::row:::
-    :::column span="":::
-        **Entity**
-
-        PersonType
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Job types or roles held by a person.
-
-        To get this entity type, add `PersonType` to the `piiCategories` parameter. `PersonType` is returned in the API response if detected.
-
-    :::column-end:::
-
-    :::column span="":::
-      **Supported languages**
-
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
-
-   :::column-end:::
- :::row-end:::
-
----
-
-# [Preview API](#tab/preview-api)
-
-## Type: License Plate 🆕
-
-This type contains the following entity:
+## Language Support
 
+The [PII language support page](../language-support.md) lists all languages available for the PII entities in this article. Any exceptions are noted for specific named entities.
 
-:::row:::
-    :::column span="":::
-        **Entity**
+Supported API versions:
 
-        LicensePlate
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        License Plate is an alphanumeric code assigned to a vehicle by a state's Department of Licensing (or the equivalent).
-
-        To get this entity category, add `LicensePlate` to the `piiCategories` parameter. `LicensePlate` is returned in the API response if detected.
-
-    :::column-end:::
-
-    :::column span="":::
-      **Supported languages**
-
-      `en`
-
-   :::column-end:::
-:::row-end:::
-
-# [GA API](#tab/ga-api)
-
-## License Plate
-
-The **LicensePlate** entity isn't available with the current GA version.
-
----
-
-# [Preview API](#tab/preview-api)
-
-## Type: Sort Code 🆕
-
-This type contains the following entity:
-
-:::row:::
-    :::column span="":::
-            **Entity**
-
-            SortCode
-
-        :::column-end:::
-        :::column span="2":::
-            **Details**
-
-            `SortCode` entity is a 6-digit number used in the UK to identify a specific bank and branch where a bank account is held.
-
-            To get this entity category, add `SortCode` to the `piiCategories` parameter. `SortCode` is returned in the API response if detected.
-
-        :::column-end:::
-
-        :::column span="":::
-          **Supported languages**
-
-          `en`
-
-   :::column-end:::
-:::row-end:::
-
-# [GA API](#tab/ga-api)
-
-## Sort Code
-
-The **SortCode** entity isn't available with the current GA version.
-
----
-
-
-# [Preview API](#tab/preview-api)
-
-## Type: PhoneNumber
-
-This type contains the following entity:
-
-:::row:::
-    :::column span="":::
-        **Entity**
-
-        PhoneNumber
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Phone numbers (US and EU phone numbers only). Returned as both PII and PHI.
-
-        To get this entity category, add `PhoneNumber` to the `piiCategories` parameter. `PhoneNumber` is returned in the API response if detected.
-
-    :::column-end:::
-
-    :::column span="":::
-      **Supported languages**
-
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt` `pt-br`
-
-   :::column-end:::
-
-:::row-end:::
-
-# [GA API](#tab/ga-api)
-
-## Category: PhoneNumber
-
-This category contains the following entity:
-
-:::row:::
-    :::column span="":::
-        **Entity**
-
-        PhoneNumber
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Phone numbers (US and EU phone numbers only). Returned as both PII and PHI.
-
-        To get this entity type, add `PhoneNumber` to the `piiCategories` parameter. `PhoneNumber` is returned in the API response if detected.
-
-    :::column-end:::
-
-    :::column span="":::
-      **Supported languages**
-
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt` `pt-br`
-
-   :::column-end:::
-
-:::row-end:::
-
----
+* [**Stable: Generally Available (GA)**](/rest/api/language/text-analysis-runtime/analyze-text?view=rest-language-2024-11-01&preserve-view=truetabs=HTTP#entitycategory)
+* [**Preview: 2025-05-15-preview**](/rest/api/language/text-analysis-runtime/analyze-text?view=rest-language-2025-05-15-preview&preserve-view=true&tabs=HTTP#entitycategory). The following entities are currently in preview:
 
-# [Preview API](#tab/preview-api)
+  * DateOfBirth
+  * BankAccountNumber
+  * PassportNumber
+  * DriversLicenseNumber
+  * SortCode
+  * VIN (vehicle identification number)
+  * LicensePlate
 
-## Type: Organization
-
-This type contains the following entity:
-
-:::row:::
-    :::column span="":::
-        **Entity**
-
-        Organization
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Companies, political groups, musical bands, sport clubs, government bodies, and public organizations. Nationalities and religions are not included in this entity type. Returned as both PII and PHI.
-
-        To get this entity category, add `Organization` to the `piiCategories` parameter. `Organization` is returned in the API response if detected.
-
-    :::column-end:::
-
-    :::column span="":::
-      **Supported languages**
-
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
-
-   :::column-end:::
-
-:::row-end:::
-
-#### Subtype
-
-The entity in this type can have the following subcategories:
-
-:::row:::
-    :::column span="":::
-        **Entity subtype**
-
-        Medical
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Medical companies and groups.
-
-        To get this entity category, add `OrganizationMedical` to the `piiCategories` parameter. `OrganizationMedical` is returned in the API response if detected.
-
-    :::column-end:::
-
-    :::column span="":::
-      **Supported languages**
-
-      `en`
-
-   :::column-end:::
-
-:::row-end:::
-:::row:::
-    :::column span="":::
-
-        Stock exchange
-
-    :::column-end:::
-    :::column span="2":::
-
-        Stock exchange groups.
-
-        To get this entity category, add `OrganizationStockExchange` to the `piiCategories` parameter. `OrganizationStockExchange` is returned in the API response if detected.
-
-    :::column-end:::
-
-    :::column span="":::
-
-      `en`
-
-   :::column-end:::
-
-:::row-end:::
-:::row:::
-    :::column span="":::
-
-        Sports
-
-    :::column-end:::
-    :::column span="2":::
-
-        Sports-related organizations.
-
-        To get this entity category, add `OrganizationSports` to the `piiCategories` parameter. `OrganizationSports` is returned in the API response if detected.
-
-    :::column-end:::
-
-    :::column span="":::
-
-      `en`
-
-   :::column-end:::
-
-:::row-end:::
-
-# [GA API](#tab/ga-api)
-
-## Category: Organization
-
-This category contains the following entity:
-
-:::row:::
-    :::column span="":::
-        **Entity**
-
-        Organization
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Companies, political groups, musical bands, sport clubs, government bodies, and public organizations. Nationalities and religions are not included in this entity type. Returned as both PII and PHI.
-
-        To get this entity type, add `Organization` to the `piiCategories` parameter. `Organization` is returned in the API response if detected.
-
-    :::column-end:::
-
-    :::column span="":::
-      **Supported languages**
-
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
-
-   :::column-end:::
-
-:::row-end:::
-
-#### Subcategory
-
-The entity in this category can have the following subcategories:
-
-:::row:::
-    :::column span="":::
-        **Entity subcategory**
-
-        Medical
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Medical companies and groups.
-
-        To get this entity type, add `OrganizationMedical` to the `piiCategories` parameter. `OrganizationMedical` is returned in the API response if detected.
-
-    :::column-end:::
-
-    :::column span="":::
-      **Supported languages**
-
-      `en`
-
-   :::column-end:::
-
-:::row-end:::
-:::row:::
-    :::column span="":::
-
-        Stock exchange
-
-    :::column-end:::
-    :::column span="2":::
-
-        Stock exchange groups.
-
-        To get this entity type, add `OrganizationStockExchange` to the `piiCategories` parameter. `OrganizationStockExchange` is returned in the API response if detected.
-
-    :::column-end:::
-
-    :::column span="":::
-
-      `en`
-
-   :::column-end:::
-
-:::row-end:::
-:::row:::
-    :::column span="":::
-
-        Sports
-
-    :::column-end:::
-    :::column span="2":::
-
-        Sports-related organizations.
-
-        To get this entity type, add `OrganizationSports` to the `piiCategories` parameter. `OrganizationSports` is returned in the API response if detected.
-
-    :::column-end:::
-
-    :::column span="":::
-
-      `en`
-
-   :::column-end:::
-
-:::row-end:::
-
----
-
-
-# [Preview API](#tab/preview-api)
-
-## Type: Address
-
-
-This type contains the following entity:
-
-:::row:::
-    :::column span="":::
-        **Entity**
-
-        Address
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Full mailing address. Returned as both PII and PHI.
-
-        To get this entity type, add `Address` to the `piiCategories` parameter. `Address` is returned in the API response if detected.
-
-    :::column-end:::
-
-    :::column span="":::
-      **Supported languages**
-
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
-
-    :::column-end:::
-
-:::row-end:::
-
-# [GA API](#tab/ga-api)
-
-## Category: Address
-
-This type contains the following entity:
-
-:::row:::
-    :::column span="":::
-        **Entity**
-
-        Address
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Full mailing address. Returned as both PII and PHI.
+> [!NOTE]
+> Beginning with the GA API (released `2024-11-01`), the **Subtype** field is no longer supported. All entity classifications now use the **type** field.
 
-        To get this entity category, add `Address` to the `piiCategories` parameter. `Address` is returned in the API response if detected.
+### Supported PII entity list
 
-    :::column-end:::
+To examine a comprehensive list of all the types of Personally Identifiable Information (PII) entities that are currently supported, *see* the [Supported PII entity list](entity-categories-list.md)
 
-    :::column span="":::
-      **Supported languages**
+### Supported PII extraction entities
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+Personally identifiable information (PII) refers to any single piece of data or combination of data that enables the unique identification, tracking, or differentiation of an individual.
 
-    :::column-end:::
+The Azure Language PII extraction API uses Natural Language Processing (NLP) technology to detect, recognize, and extract PII entities from written text or spoken conversations. The following entities represent specific types of information that can reveal an individual's identity:
 
-:::row-end:::
+## Personal
 
----
+Any data, collected or stored, that can be used to identify or contact a specific individual is considered personal information. This may include information that identifies someone directly, such as their name or social security number. It can also refer to data that, when linked with other information, could lead to identification—for example, an address or dates of birth.).
 
-# [Preview API](#tab/preview-api)
+### Type: Address
 
-## Type: Email
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **Address** in the **piiCategories** request parameter. If **Address** is detected, It appears in the **PII** and **PHI** response payloads. |[Address]|
 
-This category contains the following entity:
+### Type: Age
 
-:::row:::
-    :::column span="":::
-        **Entity**
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **Age** in the **piiCategories** request parameter. If **Age** is detected, It appears in the **PII** response payload.|[Age]|
 
-        Email
+### Type: Date Of Birth (preview)
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **DateOfBirth** in the **piiCategories** request parameter. If **DateOfBirth** is detected, It appears in the **PII** response payload.|[DateOfBirth]|
 
-        Email addresses. Returned as both PII and PHI.
+### Type: Drivers License Number (preview)
 
-        To get this entity type, add `Email` to the `piiCategories` parameter. `Email` is returned in the API response if detected.
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **DriversLicenseNumber** in the **piiCategories** request parameter. If **DriversLicenseNumber** is detected, It appears in the **PII** response payload.|[DriversLicenseNumber]|
 
-    :::column-end:::
-    :::column span="":::
-      **Supported languages**
+### Type: Email
 
-      `en`, `es`, `fr`, `de`, `it`, `zh`, `ja`, `ko`, `pt-pt`, `pt-br`, `nl`, `sv`, `tr`, `hi`
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **Email** in the **piiCategories** request parameter. If **Email** is detected, It appears in the **PII** and **PHI** response payloads.|[Email]|
 
-    :::column-end:::
-:::row-end:::
+### Type: IP Address
 
-# [GA API](#tab/ga-api)
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **IPAddress** in the **piiCategories** request parameter. If **IPAddress** is detected, It appears in the **PII** and **PHI** response payloads.|[IPAddress]|
 
-## Category: Email
+### Type: License Plate (preview)
 
-This type contains the following entity:
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **LicensePlate** in the **piiCategories** request parameter. If **LicensePlate** is detected, It appears in the **PII** response payload.|[LicensePlate]|
 
-:::row:::
-    :::column span="":::
-        **Entity**
+### Type: Passport Number (preview)
 
-        Email
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **PassportNumber** in the **piiCategories** request parameter. If **PassportNumber** is detected, It appears in the **PII** response payload.|[PassportNumber]|
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+### Type: Person
 
-        Email addresses. Returned as both PII and PHI.
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **Person** in the **piiCategories** request parameter. If **Person** is detected, It appears in the **PII** response payloads.|[Person]|
 
-        To get this category type, add `Email` to the `piiCategories` parameter. `Email` is returned in the API response if detected.
+### Type: Phone Number
 
-    :::column-end:::
-    :::column span="":::
-      **Supported languages**
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **PhoneNumber** in the **piiCategories** request parameter. If **PhoneNumber** is detected, It appears in the **PII** and **PHI** response payloads.|[PhoneNumber]|
 
-      `en`, `es`, `fr`, `de`, `it`, `zh`, `ja`, `ko`, `pt-pt`, `pt-br`, `nl`, `sv`, `tr`, `hi`
+### Type: URL
 
-    :::column-end:::
-:::row-end:::
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **URL** in the **piiCategories** request parameter. If **URL** is detected, It appears in the **PII** and **PHI** response payloads.|[URL]|
 
----
+### Type: VIN (preview)
 
-# [Preview API](#tab/preview-api)
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **VIN** (vehicle registration number) in the **piiCategories** request parameter. If **VIN** is detected, It appears in the **PII** response payload.|[VIN]|
 
-## Type: URL
+## Financial
 
-This type contains the following entity:
+Any financial information is connected to a particular individual that can, through identifying details, be traced back to that person. 
 
-:::row:::
-    :::column span="":::
-        **Entity**
 
-        URL
+### Type: ABA Routing Number
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+|Issuing authority|Details|Tag|
+|---|---|---|
+|American Bankers Association (ABA)|To retrieve this entity type, specify **ABARoutingNumber** in the **piiCategories** request parameter. If **ABARoutingNumber** is detected, It appears in the **PII** response payload.|[ABARoutingNumber]|
 
-        URLs to websites. Returned as both PII and PHI.
+### Type: Bank Account Number (preview) 
 
-        To get this entity type, add `URL` to the `piiCategories` parameter. `URL` is returned in the API response if detected.
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **BankAccountNumber** in the **piiCategories** request parameter. If **BankAccountNumber** is detected, It appears in the **PII** response payload.|[BankAccountNumber]|
 
-    :::column-end:::
+### Type: Credit Card Number
 
-    :::column span="":::
-      **Supported languages**
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **CreditCardNumber** in the **piiCategories** request parameter. If **CreditCardNumber** is detected, It appears in the **PII** response payload.|[CreditCardNumber]|
 
-      `en`, `es`, `fr`, `de`, `it`, `zh`, `ja`, `ko`, `pt-pt`, `pt-br`, `nl`, `sv`, `tr`, `hi`
+### Type: International Banking Account Number
 
-    :::column-end:::
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **InternationalBankingAccountNumber** in the **piiCategories** request parameter. If **InternationalBankingAccountNumber** is detected, It appears in the **PII** response payload.|[InternationalBankingAccountNumber]|
 
-:::row-end:::
+### Type: Sort Code (preview)
 
-# [GA API](#tab/ga-api)
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **SortCode** in the **piiCategories** request parameter. If **SortCode** is detected, It appears in the **PII** response payload.|[SortCode]|
 
-## Category: URL
+### Type: SWIFT Code
 
-This category contains the following entity:
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **SWIFTCode** in the **piiCategories** request parameter. If **SWIFTCode** is detected, It appears in the **PII** response payload.|[SWIFTCode]|
 
-:::row:::
-    :::column span="":::
-        **Entity**
+## Organization
 
-        URL
+Any data that an organization collects, stores, or processes that can be used to identify a specific individual, either directly or indirectly. 
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+### Type: Organization
 
-        URLs to websites. Returned as both PII and PHI.
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **Organization** in the **piiCategories** request parameter. If **Organization** is detected, It appears in the **PII** and **PHI** response payloads.|[Organization]|
 
-        To get this entity category, add `URL` to the `piiCategories` parameter. `URL` is returned in the API response if detected.
+## DateTime
 
-    :::column-end:::
+ Data that can be used to identify, distinguish, or trace an individual. While a date or time on its own is often not considered PII, it can become highly sensitive when combined with other data points.
 
-    :::column span="":::
-      **Supported languages**
+### Type: Date
 
-      `en`, `es`, `fr`, `de`, `it`, `zh`, `ja`, `ko`, `pt-pt`, `pt-br`, `nl`, `sv`, `tr`, `hi`
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **Date** in the **piiCategories** request parameter. If **Date** is detected, It appears in the **PII** and **PHI** response payloads.|[Date]|
 
-    :::column-end:::
+## Azure-related
 
-:::row-end:::
+Any identifiable Azure information like authentication information and connection strings that can be used to distinguish or trace an individual's identity.
 
----
+### Type: Azure Document DB Auth Key
 
-# [Preview API](#tab/preview-api)
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Microsoft|To retrieve this entity type, specify **AzureDocumentDBAuthKey** in the **piiCategories** request parameter. If **AzureDocumentDBAuthKey** is detected, It appears in the **PII** response payload.|[AzureDocumentDBAuthKey]|
 
-## Type: IP Address
+### Type: Azure IAAS Database Connection And SQL String
 
-This category contains the following entity:
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Microsoft|To retrieve this entity type, specify **AzureIAASDatabaseConnectionAndSQLString** in the **piiCategories** request parameter. If **AzureIAASDatabaseConnectionAndSQLString** is detected, It appears in the **PII** response payload.|[AzureIAASDatabaseConnectionAndSQLString]|
 
-:::row:::
-    :::column span="":::
-        **Entity**
+### Type: Azure IoT Connection String
 
-        IPAddress
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Microsoft|To retrieve this entity type, specify **AzureIoTConnectionString** in the **piiCategories** request parameter. If **AzureIoTConnectionString** is detected, It appears in the **PII** response payload.|[AzureIoTConnectionString]|
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+### Type: Azure Publish Setting Password
 
-        Network IP addresses. Returned as both PII and PHI.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Microsoft|To retrieve this entity type, specify **AzurePublishSettingPassword** in the **piiCategories** request parameter. If **AzurePublishSettingPassword** is detected, It appears in the **PII** response payload.|[AzurePublishSettingPassword]|
 
-        To get this entity type, add `IPAddress` to the `piiCategories` parameter. `IPAddress` is returned in the API response if detected.
+### Type: Azure Redis Cache String
 
-    :::column-end:::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Microsoft|To retrieve this entity type, specify **AzureRedisCacheString** in the **piiCategories** request parameter. If **AzureRedisCacheString** is detected, It appears in the **PII** response payload.|[AzureRedisCacheString]|
 
-    :::column span="":::
-      **Supported languages**
+### Type: Azure SAS
 
-      `en`, `es`, `fr`, `de`, `it`, `zh`, `ja`, `ko`, `pt-pt`, `pt-br`, `nl`, `sv`, `tr`, `hi`
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Microsoft|To retrieve this entity type, specify **AzureSAS** in the **piiCategories** request parameter. If **AzureSAS** is detected, It appears in the **PII** response payload.|[AzureSAS]|
 
-    :::column-end:::
-:::row-end:::
+### Type: Azure Service Bus String
 
-# [GA API](#tab/ga-api)
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Microsoft|To retrieve this entity type, specify **AzureServiceBusString** in the **piiCategories** request parameter. If **AzureServiceBusString** is detected, It appears in the **PII** response payload.|[AzureServiceBusString]|
 
-## Category: IP Address
+### Type: Azure Storage Account Generic
 
-This category contains the following entity:
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Microsoft|To retrieve this entity type, specify **AzureStorageAccountGeneric** in the **piiCategories** request parameter. If **AzureStorageAccountGeneric** is detected, It appears in the **PII** response payload.|[AzureStorageAccountGeneric]|
 
-:::row:::
-    :::column span="":::
-        **Entity**
+### Type: Azure Storage Account Key
 
-        IPAddress
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Microsoft|To retrieve this entity type, specify **AzureStorageAccountKey** in the **piiCategories** request parameter. If **AzureStorageAccountKey** is detected, It appears in the **PII** response payload.|[AzureStorageAccountKey]|
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+### Type: SQL Server Connection String
 
-        Network IP addresses. Returned as both PII and PHI.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Microsoft|To retrieve this entity type, specify **SQLServerConnectionString** in the **piiCategories** request parameter. If **SQLServerConnectionString** is detected, It appears in the **PII** response payload.|[AzureStorageAccountKey]|
 
-        To get this entity category, add `IPAddress` to the `piiCategories` parameter. `IPAddress` is returned in the API response if detected.
 
-    :::column-end:::
+## Government
 
-    :::column span="":::
-      **Supported languages**
+Any government-issued identification that can be used along or combined with other data to trace and reveal a specific person's identity.
 
-      `en`, `es`, `fr`, `de`, `it`, `zh`, `ja`, `ko`, `pt-pt`, `pt-br`, `nl`, `sv`, `tr`, `hi`
+### Type: Argentina National Identity Number
 
-    :::column-end:::
-:::row-end:::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Argentina|To retrieve this entity type, specify **ARNationalIdentityNumber** in the **piiCategories** request parameter. If **ARNationalIdentityNumber** is detected, It appears in the **PII** response payload.|[ARNationalIdentityNumber]|
 
+### Type: Australia Bank Account Number
 
----
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Australia|To retrieve this entity type, specify **AUBankAccountNumber** in the **piiCategories** request parameter. If **AUBankAccountNumber** is detected, It appears in the **PII** response payload.|[AUBankAccountNumber]|
 
-# [Preview API](#tab/preview-api)
+### Type: Australia Business Number
 
-## Type: DateTime
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Australia|To retrieve this entity type, specify **AUBusinessNumber** in the **piiCategories** request parameter. If **AUBusinessNumber** is detected, It appears in the **PII** response payload.|[AUBusinessNumber]|
 
-This type contains the following entities:
+### Type: Australia Company Number
 
-:::row:::
-    :::column span="":::
-        **Entity**
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Australia|To retrieve this entity type, specify **AUCompanyNumber** in the **piiCategories** request parameter. If **AUCompanyNumber** is detected, It appears in the **PII** response payload.|[AUCompanyNumber]|
 
-        DateTime
+### Type: Australia Drivers License Number
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Australia|To retrieve this entity type, specify **AUDriversLicenseNumber** in the **piiCategories** request parameter. If **AUDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[AUDriversLicenseNumber]|
 
-        Dates and times of day.
+### Type: Australia Medical Account Number
 
-        To get this entity type, add `DateTime` to the `piiCategories` parameter. `DateTime` is returned in the API response if detected.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Australia|To retrieve this entity type, specify **AUMedicalAccountNumber** in the **piiCategories** request parameter. If **AUMedicalAccountNumber** is detected, It appears in the **PII** response payload.|[AUMedicalAccountNumber]|
 
-    :::column-end:::
-:::column span="":::
-      **Supported languages**
+### Type: Australia Passport Number
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Australia|To retrieve this entity type, specify **AUPassportNumber** in the **piiCategories** request parameter. If **AUPassportNumber** is detected, It appears in the **PII** response payload.|[AUPassportNumber]|
 
-   :::column-end:::
-:::row-end:::
+### Type: Australia Tax File Number
 
-### Subtypes
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Australia|To retrieve this entity type, specify **AUTaxFileNumber** in the **piiCategories** request parameter. If **AUTaxFileNumber** is detected, It appears in the **PII** response payload.|[AUTaxFileNumber]|
 
-The entity in this type can have the following subtypes:
+### Type: Austria Identity Card
 
-:::row:::
-    :::column span="":::
-        **Entity subtypes**
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Austria|To retrieve this entity type, specify **ATIdentityCard** in the **piiCategories** request parameter. If **ATIdentityCard** is detected, It appears in the **PII** response payload.|[ATIdentityCard]|
 
-        Date
+### Type: Austria Tax Identification Number
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Austria|To retrieve this entity type, specify **ATTaxIdentificationNumber** in the **piiCategories** request parameter. If **ATTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[ATTaxIdentificationNumber]|
 
-        Calendar dates. Returned as both PII and PHI.
+### Type: Austria Value Added Tax Number
 
-        To get this entity type, add `Date` to the `piiCategories` parameter. `Date` is returned in the API response if detected.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Austria|To retrieve this entity type, specify **ATValueAddedTaxNumber** in the **piiCategories** request parameter. If **ATValueAddedTaxNumber** is detected, It appears in the **PII** response payload.|[ATValueAddedTaxNumber]|
 
-    :::column-end:::
-    :::column span="2":::
-      **Supported languages**
+### Type: Belgium National Number
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Belgium|To retrieve this entity type, specify **BENationalNumber** in the **piiCategories** request parameter. If **BENationalNumber** is detected, It appears in the **PII** response payload.|[BENationalNumber]|
 
-    :::column-end:::
-:::row-end:::
+### Type: Belgium Value Added Tax Number
 
-:::row:::
-    :::column span="":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Belgium|To retrieve this entity type, specify **BEValueAddedTaxNumber** in the **piiCategories** request parameter. If **BEValueAddedTaxNumber** is detected, It appears in the **PII** response payload.|[BEValueAddedTaxNumber]|
 
-        DateAndTime
 
+### Type: Brazil CPF Number
 
-    :::column-end:::
-    :::column span="2":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Brazil|To retrieve this entity type, specify **BRCPFNumber** in the **piiCategories** request parameter. If **BRCPFNumber** is detected, It appears in the **PII** response payload.|[BRCPFNumber]|
 
-        Dates and times of day.
+### Type: Brazil Legal Entity Number
 
-        To get this entity category, add `DateAndTime` to the `piiCategories` parameter. `DateAndTime` is returned in the API response if detected.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Brazil|To retrieve this entity type, specify **BRLegalEntityNumber** in the **piiCategories** request parameter. If **BRLegalEntityNumber** is detected, It appears in the **PII** response payload.|[BRLegalEntityNumber]|
 
+### Type: Brazil National IDRG
 
-    :::column-end:::
-    :::column span="2":::
-      **Supported languages**
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Brazil|To retrieve this entity type, specify **BRNationalIDRG** in the **piiCategories** request parameter. If **BRNationalIDRG** is detected, It appears in the **PII** response payload.|[BRNationalIDRG]|
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
-      :::column-end:::
-:::row-end:::
+### Type: Bulgaria Uniform Civil Number
 
-#### Subtype: Age
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Bulgaria|To retrieve this entity type, specify **BGUniformCivilNumber** in the **piiCategories** request parameter. If **BGUniformCivilNumber** is detected, It appears in the **PII** response payload.|[BGUniformCivilNumber]|
 
-The PII service supports the Age subtype within the broader Quantity type (since Age is the personally identifiable piece of information).
+### Type: Canada Bank Account Number
 
-:::row:::
-    :::column span="":::
-        **Entity subtype**
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Canada|To retrieve this entity type, specify **CABankAccountNumber** in the **piiCategories** request parameter. If **CABankAccountNumber** is detected, It appears in the **PII** response payload.|[CABankAccountNumber]|
 
-        Age
+### Type: Canada Drivers License Number
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Canada|To retrieve this entity type, specify **CADriversLicenseNumber** in the **piiCategories** request parameter. If **CADriversLicenseNumber** is detected, It appears in the **PII** response payload.|[CADriversLicenseNumber]|
 
-        Ages.
+### Type: Canada Health Service Number
 
-    :::column-end:::
-    :::column span="2":::
-      **Supported languages**
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Canada|To retrieve this entity type, specify **CAHealthServiceNumber** in the **piiCategories** request parameter. If **CAHealthServiceNumber** is detected, It appears in the **PII** response payload.|[CAHealthServiceNumber]|
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+### Type: Canada Passport Number
 
-   :::column-end:::
-:::row-end:::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Canada|To retrieve this entity type, specify **CAPassportNumber** in the **piiCategories** request parameter. If **CAPassportNumber** is detected, It appears in the **PII** response payload.|[CAPassportNumber]|
 
-#### Subtype: DateOfBirth 🆕
+### Type: Canada Personal Health Identification
 
-:::row:::
-    :::column span="":::
-        **Entity subtype**
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Canada|To retrieve this entity type, specify **CAPersonalHealthIdentification** in the **piiCategories** request parameter. If **CAPersonalHealthIdentification** is detected, It appears in the **PII** and **PHI** response payload.|[CAPersonalHealthIdentification]|
 
-        Date of birth.
+### Type: Canada Social Insurance Number
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Canada|To retrieve this entity type, specify **CASocialInsuranceNumber** in the **piiCategories** request parameter. If **CASocialInsuranceNumber** is detected, It appears in the **PII** response payload.|[CASocialInsuranceNumber]|
 
-      Date
+### Type: Chile Identity Card Number
 
-      To get this entity type, add `DateOfBirth` to the `piiCategories` parameter. `DateOfBirth` is returned in the API response if detected.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Chile|To retrieve this entity type, specify **CLIdentityCardNumber** in the **piiCategories** request parameter. If **CLIdentityCardNumber** is detected, It appears in the **PII** response payload.|[CLIdentityCardNumber]|
 
-    :::column-end:::
-    :::column span="2":::
-      **Supported languages**
+### Type: China Resident Identity Card Number
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `nl`
+|Issuing authority|Details|Tag|
+|---|---|---|
+|China|To retrieve this entity type, specify **CNResidentIdentityCardNumber** in the **piiCategories** request parameter. If **CNResidentIdentityCardNumber** is detected, It appears in the **PII** response payload.|[CNResidentIdentityCardNumber]|
 
-   :::column-end:::
-:::row-end:::
+### Type: Croatia Identity Card Number
 
-# [GA API](#tab/ga-api)
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Croatia|To retrieve this entity type, specify **HRIdentityCardNumber** in the **piiCategories** request parameter. If **HRIdentityCardNumber** is detected, It appears in the **PII** response payload.|[HRIdentityCardNumber]|
 
-## Category: DateTime
+### Type: Croatia National ID Number
 
-This category contains the following entities:
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Croatia|To retrieve this entity type, specify **HRNationalIDNumber** in the **piiCategories** request parameter. If **HRNationalIDNumber** is detected, It appears in the **PII** response payload.|[HRNationalIDNumber]|
 
-:::row:::
-    :::column span="":::
-        **Entity**
+### Type: Croatia Personal Identification Number
 
-        DateTime
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Croatia|To retrieve this entity type, specify **HRPersonalIdentificationNumber** in the **piiCategories** request parameter. If **HRPersonalIdentificationNumber** is detected, It appears in the **PII** response payload.|[HRPersonalIdentificationNumber]|
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+### Type: Cyprus Identity Card
 
-        Dates and times of day.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Cyprus|To retrieve this entity type, specify **CYIdentityCard** in the **piiCategories** request parameter. If **CYIdentityCard** is detected, It appears in the **PII** response payload.|[CYIdentityCard]|
 
-        To get this entity category, add `DateTime` to the `piiCategories` parameter. `DateTime` is returned in the API response if detected.
+### Type: Cyprus Tax Identification Number
 
-    :::column-end:::
-:::column span="":::
-      **Supported languages**
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Cyprus|To retrieve this entity type, specify **CYTaxIdentificationNumber** in the **piiCategories** request parameter. If **CYTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[CYTaxIdentificationNumber]|
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+### Type: Czech Republic Personal Identity Number
 
-   :::column-end:::
-:::row-end:::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Czech Republic|To retrieve this entity type, specify **CZPersonalIdentityNumber** in the **piiCategories** request parameter. If **CZPersonalIdentityNumber** is detected, It appears in the **PII** response payload.|[CZPersonalIdentityNumber]|
 
-### Subtypes
+### Type: Denmark Personal Identification Number
 
-The subtype `DateOFBirth` isn't available in the current GA version.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Denmark|To retrieve this entity type, specify **DKPersonalIdentificationNumber** in the **piiCategories** request parameter. If **DKPersonalIdentificationNumber** is detected, It appears in the **PII** response payload.|[DKPersonalIdentificationNumber]|
 
-### Subcategories
+### Type: Estonia Personal Identification Code
 
-The entity in this category can have the following subcategory:
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Estonia|To retrieve this entity type, specify **EEPersonalIdentificationCode** in the **piiCategories** request parameter. If **EEPersonalIdentificationCode** is detected, It appears in the **PII** response payload.|[EEPersonalIdentificationCode]|
 
-:::row:::
-    :::column span="":::
-        **Entity subcategory**
+### Type: European Union Debit Card Number
 
-        Date
+|Issuing authority|Details|Tag|
+|---|---|---|
+|European Union|To retrieve this entity type, specify **EUDebitCardNumber** in the **piiCategories** request parameter. If **EUDebitCardNumber** is detected, It appears in the **PII** response payload.|[EUDebitCardNumber]|
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+### Type: European Union Drivers License Number
 
-        Calender dates. Returned as both PII and PHI.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|European Union|To retrieve this entity type, specify **EUDriversLicenseNumber** in the **piiCategories** request parameter. If **EUDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[EUDriversLicenseNumber]|
 
-        To get this entity category, add `Date` to the `piiCategories` parameter. `Date` is returned in the API response if detected.
+### Type: European Union GPS Coordinates
 
-    :::column-end:::
-    :::column span="2":::
-      **Supported languages**
+|Issuing authority|Details|Tag|
+|---|---|---|
+|European Union|To retrieve this entity type, specify **EUGPSCoordinates** in the **piiCategories** request parameter. If **EUGPSCoordinates** is detected, It appears in the **PII** response payload.|[EUGPSCoordinates]|
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+### Type: European Union National Identification Number
 
-    :::column-end:::
-:::row-end:::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|European Union|To retrieve this entity type, specify **EUNationalIdentificationNumber** in the **piiCategories** request parameter. If **EUNationalIdentificationNumber** is detected, It appears in the **PII** response payload.|[EUNationalIdentificationNumber]|
 
-:::row:::
-    :::column span="":::
+### Type: European Union Passport Number
 
-        DateAndTime
+|Issuing authority|Details|Tag|
+|---|---|---|
+|European Union|To retrieve this entity type, specify **EUPassportNumber** in the **piiCategories** request parameter. If **EUPassportNumber** is detected, It appears in the **PII** response payload.|[EUPassportNumber]|
 
+### Type: European Union Social Security Number
 
-    :::column-end:::
-    :::column span="2":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|European Union|To retrieve this entity type, specify **EUSocialSecurityNumber** in the **piiCategories** request parameter. If **EUSocialSecurityNumber** is detected, It appears in the **PII** response payload.|[EUSocialSecurityNumber]|
 
-        Dates and times of day.
+### Type: European Union Tax Identification Number
 
-        To get this entity category, add `DateAndTime` to the `piiCategories` parameter. `DateAndTime` is returned in the API response if detected.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|European Union|To retrieve this entity type, specify **EUTaxIdentificationNumber** in the **piiCategories** request parameter. If **EUTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[EUTaxIdentificationNumber]|
 
+### Type: Finland European Health Number
 
-    :::column-end:::
-    :::column span="2":::
-      **Supported languages**
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Finland|To retrieve this entity type, specify **FIEuropeanHealthNumber** in the **piiCategories** request parameter. If **FIEuropeanHealthNumber** is detected, It appears in the **PII** response payload.|[FIEuropeanHealthNumber]|
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
-      :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
-        **Entity**
+### Type: Finland National ID
 
-    :::column-end:::
-    :::column span="2":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Finland|To retrieve this entity type, specify **FINationalID** in the **piiCategories** request parameter. If **FINationalID** is detected, It appears in the **PII** response payload.|[FINationalID]|
 
-        Calendar dates in diverse formats and years associated with date of birth of an individual. Examples include "born in 1994", "born in 990101", "birth date: February 14th, 1995", "date: 1992/06/30", "DATE: 05-12-1988", "04.10.1999"
+### Type: Finland Passport Number
 
-    :::column-end:::
-    :::column span="":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Finland|To retrieve this entity type, specify **FIPassportNumber** in the **piiCategories** request parameter. If **FIPassportNumber** is detected, It appears in the **PII** response payload.|[FIPassportNumber]|
 
-      `en`, `fr`, `de`, `it`, `es`, `pt-pt`, `pt-br`, `nl`, `zh-Hans`, `ja`, `ko`, `zh-Hant`
+### Type: France Drivers License Number
 
-    :::column-end:::
-:::row-end:::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|France|To retrieve this entity type, specify **FRDriversLicenseNumber** in the **piiCategories** request parameter. If **FRDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[FRDriversLicenseNumber]|
 
-#### Subcategory: Age
+### Type: France Health Insurance Number
 
-The PII service supports the Age subcategory within the broader Quantity type (since Age is the personally identifiable piece of information).
+|Issuing authority|Details|Tag|
+|---|---|---|
+|France|To retrieve this entity type, specify **FRHealthInsuranceNumber** in the **piiCategories** request parameter. If **FRHealthInsuranceNumber** is detected, It appears in the **PII** response payload.|[FRHealthInsuranceNumber]|
 
-:::row:::
-    :::column span="":::
-        **Entity subcategory**
+### Type: France National ID
 
-        Age
+|Issuing authority|Details|Tag|
+|---|---|---|
+|France|To retrieve this entity type, specify **FRNationalID** in the **piiCategories** request parameter. If **FRNationalID** is detected, It appears in the **PII** response payload.|[FRNationalID]|
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+### Type: France Passport Number
 
-        Numeric age.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|France|To retrieve this entity type, specify **FRPassportNumber** in the **piiCategories** request parameter. If **FRPassportNumber** is detected, It appears in the **PII** response payload.|[FRPassportNumber]|
 
-    :::column-end:::
-    :::column span="2":::
-      **Supported languages**
+### Type: France Social Security Number
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+|Issuing authority|Details|Tag|
+|---|---|---|
+|France|To retrieve this entity type, specify **FRSocialSecurityNumber** in the **piiCategories** request parameter. If **FRSocialSecurityNumber** is detected, It appears in the **PII** response payload.|[FRSocialSecurityNumber]|
 
-   :::column-end:::
-:::row-end:::
+### Type: France Tax Identification Number
 
----
+|Issuing authority|Details|Tag|
+|---|---|---|
+|France|To retrieve this entity type, specify **FRTaxIdentificationNumber** in the **piiCategories** request parameter. If **FRTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[FRTaxIdentificationNumber]|
 
-# [Preview API](#tab/preview-api)
+### Type: France Value Added Tax Number
 
-### Identification
+|Issuing authority|Details|Tag|
+|---|---|---|
+|France|To retrieve this entity type, specify **FRValueAddedTaxNumber** in the **piiCategories** request parameter. If **FRValueAddedTaxNumber** is detected, It appears in the **PII** response payload.|[FRValueAddedTaxNumber]|
 
-## Type: BankAccountNumber
+### Type: Germany Drivers License Number
 
-:::row:::
-    :::column span="":::
-        **Entity**
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Germany|To retrieve this entity type, specify **DEDriversLicenseNumber** in the **piiCategories** request parameter. If **DEDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[DEDriversLicenseNumber]|
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+### Type: Germany Identity Card Number
 
-        To get this entity type, add `BankAccountNumber` to the `piiCategories` parameter. `BankAccountNumber` is returned in the API response if detected.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Germany|To retrieve this entity type, specify **DEIdentityCardNumber** in the **piiCategories** request parameter. If **DEIdentityCardNumber** is detected, It appears in the **PII** response payload.|[DEIdentityCardNumber]|
 
-    :::column-end:::
-    :::column span="":::
-      **Supported languages**
+### Type: Germany Passport Number
 
-     `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `af`, `ca`, `da`, `el`, `ga`, `gl`, `ku`, `nl`, `no`, `ss`, `ro`, `sq`, `ur`, `ar`, `bg`, `bs`, `cy`, `fa`, `hr`, `id`, `mg`, `mk`, `ms`, `ps`, `ru`, `sl`, `so`, `sr`, `sw`, `am`, `as`, `cs`, `et`, `eu`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `mr`, `my`, `ne`, `or`, `pa`, `pl`, `sk`, `th`, `uk`, `az`, `bn`, `gu`, `hy`, `ka`, `kk`, `kn`, `ky`, `ml`, `mn`, `ta`, `te`, `ug`, `uz`, `vi`
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Germany|To retrieve this entity type, specify **DEPassportNumber** in the **piiCategories** request parameter. If **DEPassportNumber** is detected, It appears in the **PII** response payload.|[DEPassportNumber]|
 
-    :::column-end:::
-:::row-end:::
+### Type: Germany Tax Identification Number
 
-## Type: DriversLicenseNumber
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Germany|To retrieve this entity type, specify **DETaxIdentificationNumber** in the **piiCategories** request parameter. If **DETaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[DETaxIdentificationNumber]|
 
-:::row:::
-    :::column span="":::
-        **Entity**
+### Type: Germany Value Added Number
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Germany|To retrieve this entity type, specify **DEValueAddedNumber** in the **piiCategories** request parameter. If **DEValueAddedNumber** is detected, It appears in the **PII** response payload.|[DEValueAddedNumber]|
 
-        To get this entity type, add `DriversLicenseNumber` to the `piiCategories` parameter. `DriversLicenseNumber` is returned in the API response if detected.
+### Type: Greece National ID Card
 
-    :::column-end:::
-    :::column span="":::
-      **Supported languages**
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Greece|To retrieve this entity type, specify **GRNationalIDCard** in the **piiCategories** request parameter. If **GRNationalIDCard** is detected, It appears in the **PII** response payload.|[GRNationalIDCard]|
 
-     `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `sk`, `th`, `uk`
+### Type: Greece Tax Identification Number
 
-    :::column-end:::
-:::row-end:::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Greece|To retrieve this entity type, specify **GRTaxIdentificationNumber** in the **piiCategories** request parameter. If **GRTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[GRTaxIdentificationNumber]|
 
-## Type: PassportNumber
+### Type: Hong Kong SAR Identity Card Number
 
-:::row:::
-    :::column span="":::
-        **Entity**
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Hong Kong SAR|To retrieve this entity type, specify **HKIdentityCardNumber** in the **piiCategories** request parameter. If **HKIdentityCardNumber** is detected, It appears in the **PII** response payload.|[HKIdentityCardNumber]|
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+### Type: Hungary Personal Identification Number
 
-        To get this entity type, add `PassportNumber` to the `piiCategories` parameter. `PassportNumber` is returned in the API response if detected.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Hungary|To retrieve this entity type, specify **HUPersonalIdentificationNumber** in the **piiCategories** request parameter. If **HUPersonalIdentificationNumber** is detected, It appears in the **PII** response payload.|[HUPersonalIdentificationNumber]|
 
-    :::column-end:::
-    :::column span="":::
-      **Supported languages**
+### Type: Hungary Tax Identification Number
 
-     `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `km`, `lo`, `lt`, `lv`, `sk`, `th`, `uk`
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Hungary|To retrieve this entity type, specify **HUTaxIdentificationNumber** in the **piiCategories** request parameter. If **HUTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[HUTaxIdentificationNumber]|
 
-    :::column-end:::
-:::row-end:::
+### Type: Hungary Value Added Number
 
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Hungary|To retrieve this entity type, specify **HUValueAddedNumber** in the **piiCategories** request parameter. If **HUValueAddedNumber** is detected, It appears in the **PII** response payload.|[HUValueAddedNumber]|
 
-# [GA API](#tab/ga-api)
+### Type: India Permanent Account
 
-[!INCLUDE [supported identification entities](../includes/identification-entities.md)]
+|Issuing authority|Details|Tag|
+|---|---|---|
+|India|To retrieve this entity type, specify **INPermanentAccount** in the **piiCategories** request parameter. If **INPermanentAccount** is detected, It appears in the **PII** response payload.|[INPermanentAccount]|
 
----
+### Type: India Unique Identification Number
 
-# [Preview API](#tab/preview-api)
+|Issuing authority|Details|Tag|
+|---|---|---|
+|India|To retrieve this entity type, specify **INUniqueIdentificationNumber** in the **piiCategories** request parameter. If **INUniqueIdentificationNumber** is detected, It appears in the **PII** response payload.|[INUniqueIdentificationNumber]|
 
-## Azure information
+### Type: Indonesia Identity Card Number
 
-These entity types include identifiable Azure information like authentication information and connection strings. Not returned as PHI.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Indonesia|To retrieve this entity type, specify **IDIdentityCardNumber** in the **piiCategories** request parameter. If **IDIdentityCardNumber** is detected, It appears in the **PII** response payload.|[IDIdentityCardNumber]|
 
-:::row:::
-    :::column span="":::
-        **Entity**
+### Type: Ireland Personal Public Service Number
 
-        Azure DocumentDB Auth Key
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Ireland|To retrieve this entity type, specify **IEPersonalPublicServiceNumber** in the **piiCategories** request parameter. If **IEPersonalPublicServiceNumber** is detected, It appears in the **PII** response payload.|[IEPersonalPublicServiceNumber]|
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+### Type: Israel Bank Account Number
 
-        Authorization key for an Azure Cosmos DB server.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Israel|To retrieve this entity type, specify **ILBankAccountNumber** in the **piiCategories** request parameter. If **ILBankAccountNumber** is detected, It appears in the **PII** response payload.|[ILBankAccountNumber]|
 
-        To get this entity type, add `AzureDocumentDBAuthKey` to the `piiCategories` parameter. `AzureDocumentDBAuthKey` is returned in the API response if detected.
+### Type: Israel National ID
 
-    :::column-end:::
-    :::column span="":::
-      **Supported languages**
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Israel|To retrieve this entity type, specify **ILNationalID** in the **piiCategories** request parameter. If **ILNationalID** is detected, It appears in the **PII** response payload.|[ILNationalID]|
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+### Type: Italy Drivers License Number
 
-    :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Italy|To retrieve this entity type, specify **ITDriversLicenseNumber** in the **piiCategories** request parameter. If **ITDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[ITDriversLicenseNumber]|
 
-        Azure IAAS Database Connection String and Azure SQL Connection String.
+### Type: Italy Fiscal Code
 
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Italy|To retrieve this entity type, specify **ITFiscalCode** in the **piiCategories** request parameter. If **ITFiscalCode** is detected, It appears in the **PII** response payload.|[ITFiscalCode]|
 
-    :::column-end:::
-    :::column span="2":::
+### Type: Italy Value Added Tax Number
 
-        Connection string for an Azure infrastructure as a service (IaaS) database, and SQL connection string.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Italy|To retrieve this entity type, specify **ITValueAddedTaxNumber** in the **piiCategories** request parameter. If **ITValueAddedTaxNumber** is detected, It appears in the **PII** response payload.|[ITValueAddedTaxNumber]|
 
-        To get this entity type, add `AzureIAASDatabaseConnectionAndSQLString` to the `piiCategories` parameter. `AzureIAASDatabaseConnectionAndSQLString` is returned in the API response if detected.
+### Type: Japan Bank Account Number
 
-    :::column-end:::
-    :::column span="":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Japan|To retrieve this entity type, specify **JPBankAccountNumber** in the **piiCategories** request parameter. If **JPBankAccountNumber** is detected, It appears in the **PII** response payload.|[JPBankAccountNumber]|
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+### Type: Japan Drivers License Number
 
-    :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Japan|To retrieve this entity type, specify **JPDriversLicenseNumber** in the **piiCategories** request parameter. If **JPDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[JPDriversLicenseNumber]|
 
-        Azure IoT Connection String
+### Type: Japan My Number Corporate
 
-    :::column-end:::
-    :::column span="2":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Japan|To retrieve this entity type, specify **JPMyNumberCorporate** in the **piiCategories** request parameter. If **JPMyNumberCorporate** is detected, It appears in the **PII** response payload.|[JPMyNumberCorporate]|
 
-        Connection string for Azure IoT.
+### Type: Japan My Number Personal
 
-        To get this entity type, add `AzureIoTConnectionString` to the `piiCategories` parameter. `AzureIoTConnectionString` is returned in the API response if detected.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Japan|To retrieve this entity type, specify **JPMyNumberPersonal** in the **piiCategories** request parameter. If **JPMyNumberPersonal** is detected, It appears in the **PII** response payload.|[JPMyNumberPersonal]|
 
-    :::column-end:::
-    :::column span="":::
+### Type: Japan Passport Number
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Japan|To retrieve this entity type, specify **JPPassportNumber** in the **piiCategories** request parameter. If **JPPassportNumber** is detected, It appears in the **PII** response payload.|[JPPassportNumber]|
 
-    :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
+### Type: Japan Residence Card Number
 
-        Azure Publish Setting Password
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Japan|To retrieve this entity type, specify **JPResidenceCardNumber** in the **piiCategories** request parameter. If **JPResidenceCardNumber** is detected, It appears in the **PII** response payload.|[JPResidenceCardNumber]|
 
-    :::column-end:::
-    :::column span="2":::
+### Type: Japan Resident Registration Number
 
-        Password for Azure publish settings.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Japan|To retrieve this entity type, specify **JPResidentRegistrationNumber** in the **piiCategories** request parameter. If **JPResidentRegistrationNumber** is detected, It appears in the **PII** response payload.|[JPResidentRegistrationNumber]|
 
-        To get this entity type, add `AzurePublishSettingPassword` to the `piiCategories` parameter. `AzurePublishSettingPassword` is returned in the API response if detected.
+### Type: Japan Social Insurance Number
 
-    :::column-end:::
-    :::column span="":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Japan|To retrieve this entity type, specify **JPSocialInsuranceNumber** in the **piiCategories** request parameter. If **JPSocialInsuranceNumber** is detected, It appears in the **PII** response payload.|[JPSocialInsuranceNumber]|
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+### Type: Latvia Personal Code
 
-    :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Latvia|To retrieve this entity type, specify **LVPersonalCode** in the **piiCategories** request parameter. If **LVPersonalCode** is detected, It appears in the **PII** response payload.|[LVPersonalCode]|
 
-        Azure Redis Cache Connection String
+### Type: Lithuania Personal Code
 
-    :::column-end:::
-    :::column span="2":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Lithuania|To retrieve this entity type, specify **LTPersonalCode** in the **piiCategories** request parameter. If **LTPersonalCode** is detected, It appears in the **PII** response payload.|[LTPersonalCode]|
 
-        Connection string for a Redis cache.
+### Type: Luxembourg National Identification Number Natural
 
-        To get this entity type, add `AzureRedisCacheString` to the `piiCategories` parameter. `AzureRedisCacheString` is returned in the API response if detected.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Luxembourg|To retrieve this entity type, specify **LUNationalIdentificationNumberNatural** in the **piiCategories** request parameter. If **LUNationalIdentificationNumberNatural** is detected, It appears in the **PII** response payload.|[LUNationalIdentificationNumberNatural]|
 
-    :::column-end:::
-    :::column span="":::
+### Type: Luxembourg National Identification Number Non Natural
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Luxembourg|To retrieve this entity type, specify **LUNationalIdentificationNumberNonNatural** in the **piiCategories** request parameter. If **LUNationalIdentificationNumberNonNatural** is detected, It appears in the **PII** response payload.|[LUNationalIdentificationNumberNonNatural]|
 
-    :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
+### Type: Malaysia Identity Card Number
 
-        Azure SAS
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Malaysia|To retrieve this entity type, specify **MYIdentityCardNumber** in the **piiCategories** request parameter. If **MYIdentityCardNumber** is detected, It appears in the **PII** response payload.|[MYIdentityCardNumber]|
 
-    :::column-end:::
-    :::column span="2":::
 
-        Connection string for Azure software as a service (SaaS).
+### Type: Malta Identity Card Number
 
-        To get this entity type, add `AzureSAS` to the `piiCategories` parameter. `AzureSAS` is returned in the API response if detected.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Malta|To retrieve this entity type, specify **MTIdentityCardNumber** in the **piiCategories** request parameter. If **MTIdentityCardNumber** is detected, It appears in the **PII** response payload.|[MTIdentityCardNumber]|
 
-    :::column-end:::
-    :::column span="":::
+### Type: Malta Tax ID Number
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Malta|To retrieve this entity type, specify **MTTaxIDNumber** in the **piiCategories** request parameter. If **MTTaxIDNumber** is detected, It appears in the **PII** response payload.|[MTTaxIDNumber]|
 
-    :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
+### Type: Netherlands Citizens Service Number
 
-        Azure Service Bus Connection String
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Netherlands|To retrieve this entity type, specify **NLCitizensServiceNumber** in the **piiCategories** request parameter. If **NLCitizensServiceNumber** is detected, It appears in the **PII** response payload.|[NLCitizensServiceNumber]|
 
-    :::column-end:::
-    :::column span="2":::
+### Type: Netherlands Tax Identification Number
 
-        Connection string for an Azure service bus.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Netherlands|To retrieve this entity type, specify **NLTaxIdentificationNumber** in the **piiCategories** request parameter. If **NLTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[NLTaxIdentificationNumber]|
 
-        To get this entity type, add `AzureServiceBusString` to the `piiCategories` parameter. `AzureServiceBusString` is returned in the API response if detected.
+### Type: Netherlands Value Added Tax Number
 
-    :::column-end:::
-    :::column span="":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Netherlands|To retrieve this entity type, specify **NLValueAddedTaxNumber** in the **piiCategories** request parameter. If **NLValueAddedTaxNumber** is detected, It appears in the **PII** response payload.|[NLValueAddedTaxNumber]|
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+### Type: New Zealand Bank Account Number
 
-    :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|New Zealand|To retrieve this entity type, specify **NZBankAccountNumber** in the **piiCategories** request parameter. If **NZBankAccountNumber** is detected, It appears in the **PII** response payload.|[NZBankAccountNumber]|
 
-        Azure Storage Account Key
+### Type: New Zealand Drivers License Number
 
-    :::column-end:::
-    :::column span="2":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|New Zealand|To retrieve this entity type, specify **NZDriversLicenseNumber** in the **piiCategories** request parameter. If **NZDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[NZDriversLicenseNumber]|
 
-        Account key for an Azure storage account.
+### Type: New Zealand Inland Revenue Number
 
-        To get this entity type, add `AzureStorageAccountKey` to the `piiCategories` parameter. `AzureStorageAccountKey` is returned in the API response if detected.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|New Zealand|To retrieve this entity type, specify **NZInlandRevenueNumber** in the **piiCategories** request parameter. If **NZInlandRevenueNumber** is detected, It appears in the **PII** response payload.|[NZInlandRevenueNumber]|
 
-    :::column-end:::
-    :::column span="":::
+### Type: New Zealand Ministry Of Health Number
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+|Issuing authority|Details|Tag|
+|---|---|---|
+|New Zealand|To retrieve this entity type, specify **NZMinistryOfHealthNumber** in the **piiCategories** request parameter. If **NZMinistryOfHealthNumber** is detected, It appears in the **PII** response payload.|[NZMinistryOfHealthNumber]|
 
-    :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
+### Type: New Zealand Social Welfare Number
 
-        Azure Storage Account Key (Generic)
+|Issuing authority|Details|Tag|
+|---|---|---|
+|New Zealand|To retrieve this entity type, specify **NZSocialWelfareNumber** in the **piiCategories** request parameter. If **NZSocialWelfareNumber** is detected, It appears in the **PII** response payload.|[NZSocialWelfareNumber]|
 
-    :::column-end:::
-    :::column span="2":::
+### Type: Norway Identity Number
 
-        Generic account key for an Azure storage account.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Norway|To retrieve this entity type, specify **NOIdentityNumber** in the **piiCategories** request parameter. If **NOIdentityNumber** is detected, It appears in the **PII** response payload.|[NOIdentityNumber]|
 
-        To get this entity type, add `AzureStorageAccountGeneric` to the `piiCategories` parameter. `AzureStorageAccountGeneric` is returned in the API response if detected.
+### Type: Philippines Unified Multi Purpose ID Number
 
-    :::column-end:::
-    :::column span="":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Philippines|To retrieve this entity type, specify **PHUnifiedMultiPurposeIDNumber** in the **piiCategories** request parameter. If **PHUnifiedMultiPurposeIDNumber** is detected, It appears in the **PII** response payload.|[PHUnifiedMultiPurposeIDNumber]|
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+### Type: Poland Identity Card
 
-    :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Poland|To retrieve this entity type, specify **PLIdentityCard** in the **piiCategories** request parameter. If **PLIdentityCard** is detected, It appears in the **PII** response payload.|[PLIdentityCard]|
 
-        SQL Server Connection String
+### Type: Poland National ID
 
-    :::column-end:::
-    :::column span="2":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Poland|To retrieve this entity type, specify **PLNationalID** in the **piiCategories** request parameter. If **PLNationalID** is detected, It appears in the **PII** response payload.|[PLNationalID]|
 
-        Connection string for a computer running SQL Server.
+### Type: Poland Passport Number
 
-        To get this entity type, add `SQLServerConnectionString` to the `piiCategories` parameter. `SQLServerConnectionString` is returned in the API response if detected.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Poland|To retrieve this entity type, specify **PLPassportNumber** in the **piiCategories** request parameter. If **PLPassportNumber** is detected, It appears in the **PII** response payload.|[PLPassportNumber]|
 
-    :::column-end:::
-    :::column span="":::
+### Type: Poland REGON Number
 
-      `en`
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Poland|To retrieve this entity type, specify **PLREGONNumber** in the **piiCategories** request parameter. If **PLREGONNumber** is detected, It appears in the **PII** response payload.|[PLREGONNumber]|
 
-    :::column-end:::
-:::row-end:::
+### Type: Poland Tax Identification Number
 
-# [GA API](#tab/ga-api)
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Poland|To retrieve this entity type, specify **PLTaxIdentificationNumber** in the **piiCategories** request parameter. If **PLTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[PLTaxIdentificationNumber]|
 
-## Azure information
+### Type: Portugal Citizen Card Number
 
-These entity categories include identifiable Azure information like authentication information and connection strings. Not returned as PHI.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Portugal|To retrieve this entity type, specify **PTCitizenCardNumber** in the **piiCategories** request parameter. If **PTCitizenCardNumber** is detected, It appears in the **PII** response payload.|[PTCitizenCardNumber]|
 
-:::row:::
-    :::column span="":::
-        **Entity**
+### Type: Portugal Tax Identification Number
 
-        Azure DocumentDB Auth Key
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Portugal|To retrieve this entity type, specify **PTTaxIdentificationNumber** in the **piiCategories** request parameter. If **PTTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[PTTaxIdentificationNumber]|
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+### Type: Romania Personal Numerical Code
 
-        Authorization key for an Azure Cosmos DB server.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Romania|To retrieve this entity type, specify **ROPersonalNumericalCode** in the **piiCategories** request parameter. If **ROPersonalNumericalCode** is detected, It appears in the **PII** response payload.|[ROPersonalNumericalCode]|
 
-        To get this entity category, add `AzureDocumentDBAuthKey` to the `piiCategories` parameter. `AzureDocumentDBAuthKey` is returned in the API response if detected.
+### Type: Russia Passport Number Domestic
 
-    :::column-end:::
-    :::column span="":::
-      **Supported languages**
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Russia|To retrieve this entity type, specify **RUPassportNumberDomestic** in the **piiCategories** request parameter. If **RUPassportNumberDomestic** is detected, It appears in the **PII** response payload.|[RUPassportNumberDomestic]|
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+### Type: Russia Passport Number International
 
-    :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Russia|To retrieve this entity type, specify **RUPassportNumberInternational** in the **piiCategories** request parameter. If **RUPassportNumberInternational** is detected, It appears in the **PII** response payload.|[RUPassportNumberInternational]|
 
-        Azure IAAS Database Connection String and Azure SQL Connection String.
+### Type: Saudi Arabia National ID
 
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Saudi Arabia|To retrieve this entity type, specify **SANationalID** in the **piiCategories** request parameter. If **SANationalID** is detected, It appears in the **PII** response payload.|[SANationalID]|
 
-    :::column-end:::
-    :::column span="2":::
+### Type: Singapore National Registration Identity Card Number
 
-        Connection string for an Azure infrastructure as a service (IaaS) database, and SQL connection string.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Singapore|To retrieve this entity type, specify **SGNationalRegistrationIdentityCardNumber** in the **piiCategories** request parameter. If **SGNationalRegistrationIdentityCardNumber** is detected, It appears in the **PII** response payload.|[SGNationalRegistrationIdentityCardNumber]|
 
-        To get this entity category, add `AzureIAASDatabaseConnectionAndSQLString` to the `piiCategories` parameter. `AzureIAASDatabaseConnectionAndSQLString` is returned in the API response if detected.
+### Type: Slovakia Personal Number
 
-    :::column-end:::
-    :::column span="":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Slovakia|To retrieve this entity type, specify **SKPersonalNumber** in the **piiCategories** request parameter. If **SKPersonalNumber** is detected, It appears in the **PII** response payload.|[SKPersonalNumber]|
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+### Type: Slovenia Tax Identification Number
 
-    :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Slovenia|To retrieve this entity type, specify **SITaxIdentificationNumber** in the **piiCategories** request parameter. If **SITaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[SITaxIdentificationNumber]|
 
-        Azure IoT Connection String
+### Type: Slovenia Unique Master Citizen Number
 
-    :::column-end:::
-    :::column span="2":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Slovenia|To retrieve this entity type, specify **SIUniqueMasterCitizenNumber** in the **piiCategories** request parameter. If **SIUniqueMasterCitizenNumber** is detected, It appears in the **PII** response payload.|[SIUniqueMasterCitizenNumber]|
 
-        Connection string for Azure IoT.
+### Type: South Africa Identification Number
 
-        To get this entity category, add `AzureIoTConnectionString` to the `piiCategories` parameter. `AzureIoTConnectionString` is returned in the API response if detected.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|South Africa|To retrieve this entity type, specify **ZAIdentificationNumber** in the **piiCategories** request parameter. If **ZAIdentificationNumber** is detected, It appears in the **PII** response payload.|[ZAIdentificationNumber]|
 
-    :::column-end:::
-    :::column span="":::
+### Type: South Korea Resident Registration Number
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+|Issuing authority|Details|Tag|
+|---|---|---|
+|South Korea|To retrieve this entity type, specify **KRResidentRegistrationNumber** in the **piiCategories** request parameter. If **KRResidentRegistrationNumber** is detected, It appears in the **PII** response payload.|[KRResidentRegistrationNumber]|
 
-    :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
+### Type: Spain DNI
 
-        Azure Publish Setting Password
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Spain|To retrieve this entity type, specify **ESDNI** in the **piiCategories** request parameter. If **ESDNI** is detected, It appears in the **PII** response payload.|[ESDNI]|
 
-    :::column-end:::
-    :::column span="2":::
+### Type: Spain Social Security Number
 
-        Password for Azure publish settings.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Spain|To retrieve this entity type, specify **ESSocialSecurityNumber** in the **piiCategories** request parameter. If **ESSocialSecurityNumber** is detected, It appears in the **PII** response payload.|[ESSocialSecurityNumber]|
 
-        To get this entity category, add `AzurePublishSettingPassword` to the `piiCategories` parameter. `AzurePublishSettingPassword` is returned in the API response if detected.
+### Type: Spain Tax Identification Number
 
-    :::column-end:::
-    :::column span="":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Spain|To retrieve this entity type, specify **ESTaxIdentificationNumber** in the **piiCategories** request parameter. If **ESTaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[ESTaxIdentificationNumber]|
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+### Type: Sweden National ID
 
-    :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Sweden|To retrieve this entity type, specify **SENationalID** in the **piiCategories** request parameter. If **SENationalID** is detected, It appears in the **PII** response payload.|[SENationalID]|
 
-        Azure Redis Cache Connection String
+### Type: Sweden Passport Number
 
-    :::column-end:::
-    :::column span="2":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Sweden|To retrieve this entity type, specify **SEPassportNumber** in the **piiCategories** request parameter. If **SEPassportNumber** is detected, It appears in the **PII** response payload.|[SEPassportNumber, PassportNumber]|
 
-        Connection string for a Redis cache.
+### Type: Sweden Tax Identification Number
 
-        To get this entity category, add `AzureRedisCacheString` to the `piiCategories` parameter. `AzureRedisCacheString` is returned in the API response if detected.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Sweden|To retrieve this entity type, specify **SETaxIdentificationNumber** in the **piiCategories** request parameter. If **SETaxIdentificationNumber** is detected, It appears in the **PII** response payload.|[SETaxIdentificationNumber]|
 
-    :::column-end:::
-    :::column span="":::
+### Type: Switzerland Social Security Number
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Switzerland|To retrieve this entity type, specify **CHSocialSecurityNumber** in the **piiCategories** request parameter. If **CHSocialSecurityNumber** is detected, It appears in the **PII** response payload.|[CHSocialSecurityNumber]|
 
-    :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
+### Type: Taiwanese ID
 
-        Azure SAS
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Taiwan|To retrieve this entity type, specify **TWNationalID** in the **piiCategories** request parameter. If **TWNationalID** is detected, It appears in the **PII** response payload.|[TWNationalID]|
 
-    :::column-end:::
-    :::column span="2":::
+### Type: Taiwan Passport Number
 
-        Connection string for Azure software as a service (SaaS).
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Taiwan|To retrieve this entity type, specify **TWPassportNumber** in the **piiCategories** request parameter. If **TWPassportNumber** is detected, It appears in the **PII** response payload.|[TWPassportNumber]|
 
-        To get this entity category, add `AzureSAS` to the `piiCategories` parameter. `AzureSAS` is returned in the API response if detected.
+### Type: Taiwan Resident Certificate
 
-    :::column-end:::
-    :::column span="":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Taiwan|To retrieve this entity type, specify **TWResidentCertificate** in the **piiCategories** request parameter. If **TWResidentCertificate** is detected, It appears in the **PII** response payload.|[TWResidentCertificate]|
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+### Type: Thailand Population Identification Code
 
-    :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Thailand|To retrieve this entity type, specify **THPopulationIdentificationCode** in the **piiCategories** request parameter. If **THPopulationIdentificationCode** is detected, It appears in the **PII** response payload.|[THPopulationIdentificationCode]|
 
-        Azure Service Bus Connection String
+### Type: Türkiye National Identification Number
 
-    :::column-end:::
-    :::column span="2":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Türkiye|To retrieve this entity type, specify **TRNationalIdentificationNumber** in the **piiCategories** request parameter. If **TRNationalIdentificationNumber** is detected, It appears in the **PII** response payload.|[TRNationalIdentificationNumber]|
 
-        Connection string for an Azure service bus.
+### Type: Ukraine Passport Number Domestic
 
-        To get this entity category, add `AzureServiceBusString` to the `piiCategories` parameter. `AzureServiceBusString` is returned in the API response if detected.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Ukraine|To retrieve this entity type, specify **UAPassportNumberDomestic** in the **piiCategories** request parameter. If **UAPassportNumberDomestic** is detected, It appears in the **PII** response payload.|[UAPassportNumberDomestic]|
 
-    :::column-end:::
-    :::column span="":::
+### Type: Ukraine Passport Number International
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+|Issuing authority|Details|Tag|
+|---|---|---|
+|Ukraine|To retrieve this entity type, specify **UAPassportNumberInternational** in the **piiCategories** request parameter. If **UAPassportNumberInternational** is detected, It appears in the **PII** response payload.|[UAPassportNumberInternational]|
 
-    :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
+### Type: United Kingdom Drivers License Number
 
-        Azure Storage Account Key
+|Issuing authority|Details|Tag|
+|---|---|---|
+|United Kingdom|To retrieve this entity type, specify **UKDriversLicenseNumber** in the **piiCategories** request parameter. If **UKDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[UKDriversLicenseNumber]|
 
-    :::column-end:::
-    :::column span="2":::
+### Type: United Kingdom Electoral Roll Number
 
-        Account key for an Azure storage account.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|United Kingdom|To retrieve this entity type, specify **UKElectoralRollNumber** in the **piiCategories** request parameter. If **UKElectoralRollNumber** is detected, It appears in the **PII** response payload.|[UKElectoralRollNumber]|
 
-        To get this entity category, add `AzureStorageAccountKey` to the `piiCategories` parameter. `AzureStorageAccountKey` is returned in the API response if detected.
+### Type: United Kingdom National Health Number
 
-    :::column-end:::
-    :::column span="":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|United Kingdom|To retrieve this entity type, specify **UKNationalHealthNumber** in the **piiCategories** request parameter. If **UKNationalHealthNumber** is detected, It appears in the **PII** response payload.|[UKNationalHealthNumber]|
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+### Type: United Kingdom National Insurance Number
 
-    :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|United Kingdom|To retrieve this entity type, specify **UKNationalInsuranceNumber** in the **piiCategories** request parameter. If **UKNationalInsuranceNumber** is detected, It appears in the **PII** response payload.|[UKNationalInsuranceNumber]|
 
-        Azure Storage Account Key (Generic)
+### Type: United Kingdom Unique Taxpayer Number
 
-    :::column-end:::
-    :::column span="2":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|United Kingdom|To retrieve this entity type, specify **UKUniqueTaxpayerNumber** in the **piiCategories** request parameter. If **UKUniqueTaxpayerNumber** is detected, It appears in the **PII** response payload.|[UKUniqueTaxpayerNumber]|
 
-        Generic account key for an Azure storage account.
+### Type: United States Bank Account Number
 
-        To get this entity category, add `AzureStorageAccountGeneric` to the `piiCategories` parameter. `AzureStorageAccountGeneric` is returned in the API response if detected.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|United States|To retrieve this entity type, specify **USBankAccountNumber** in the **piiCategories** request parameter. If **USBankAccountNumber** is detected, It appears in the **PII** response payload.|[USBankAccountNumber]|
 
-    :::column-end:::
-    :::column span="":::
+### Type: United States Drivers License Number
 
-      `en`, `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br`, `zh`, `ja`, `ko`, `nl`, `sv`, `tr`, `hi`, `da`, `nl`, `no`, `ro`, `ar`, `bg`, `hr`, `ms`, `ru`, `sl`, `cs`, `et`, `fi`, `he`, `hu`, `lv`, `sk`, `th`, `uk`
+|Issuing authority|Details|Tag|
+|---|---|---|
+|United States|To retrieve this entity type, specify **USDriversLicenseNumber** in the **piiCategories** request parameter. If **USDriversLicenseNumber** is detected, It appears in the **PII** response payload.|[USDriversLicenseNumber]|
 
-    :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
+### Type: United States Drug Enforcement Agency Number
 
-        SQL Server Connection String
+|Issuing authority|Details|Tag|
+|---|---|---|
+|United States|To retrieve this entity type, specify **"DrugEnforcementAgencyNumber** in the **piiCategories** request parameter. If **DrugEnforcementAgencyNumber** is detected, It appears in the **PII** response payload.|["DrugEnforcementAgencyNumber]|
 
-    :::column-end:::
-    :::column span="2":::
+### Type: United States Individual Taxpayer Identification
 
-        Connection string for a computer running SQL Server.
+|Issuing authority|Details|Tag|
+|---|---|---|
+|United States|To retrieve this entity type, specify **USIndividualTaxpayerIdentification** in the **piiCategories** request parameter. If **USIndividualTaxpayerIdentification** is detected, It appears in the **PII** response payload.|[USIndividualTaxpayerIdentification]|
 
-        To get this entity category, add `SQLServerConnectionString` to the `piiCategories` parameter. `SQLServerConnectionString` is returned in the API response if detected.
+### Type: United States Social Security Number
 
-    :::column-end:::
-    :::column span="":::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|United States|To retrieve this entity type, specify **USSocialSecurityNumber** in the **piiCategories** request parameter. If **USSocialSecurityNumber** is detected, It appears in the **PII** response payload.|[USSocialSecurityNumber]|
 
-      `en`
+### Type: United States/United Kingdom Passport Number
 
-    :::column-end:::
-:::row-end:::
+|Issuing authority|Details|Tag|
+|---|---|---|
+|United States/United Kingdom|To retrieve this entity type, specify **USUKPassportNumber** in the **piiCategories** request parameter. If **USUKPassportNumber** is detected, It appears in the **PII** response payload.|[USUKPassportNumber]|
 
----
 
-## Next steps
+## Related content
 
-* [PII overview](../overview.md)
+[PII entity categories list](entity-categories-list.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PIIおよびPHI検出のエンティティカテゴリの変更"
}
```

### Explanation
この変更では、Azure AI Languageにおける個人識別情報（PII）および保護された健康情報（PHI）の検出に関連するエンティティカテゴリに関する文書が更新され、大幅な修正が施されています。具体的には、708行が追加され、1111行が削除され、合計1819行の変更が含まれています。

主な変更点は以下の通りです：

1. **タイトルと説明の更新**:
   - ドキュメントのタイトルが「PII検出によって認識されるエンティティカテゴリ」から、「PIIおよびPHI検出によって認識されるエンティティカテゴリ」へ変更されました。
   - 説明文も改訂され、PIIおよびPHI APIの機能について、より具体的に説明されています。

2. **新しいエンティティタイプの追加**:
   - 新たなエンティティタイプやその詳細情報が追加され、AIや機械学習を活用したPII・PHI検出機能が強調されています。

3. **構造の再編成**:
   - エンティティに関する情報がより明確に整理され、特定のエンティティを取得するためのパラメータやそれらを検出する方法を示した表が用意されています。

4. **メモやヒントの追加**:
   - PII検出を試すためのリンクや、保護された健康情報を検出する際の特定のモデルバージョンに関する注意事項も追加されています。

これにより、ユーザーがより効率的にPIIおよびPHIエンティティを利用できるように、ドキュメントが一貫性を持たせて強化されました。

## articles/ai-services/language-service/personally-identifiable-information/overview.md{#item-8a6932}

<details>
<summary>Diff</summary>
````diff
@@ -22,9 +22,9 @@ Azure AI Language Personally Identifiable Information (PII) detection is a featu
 
 The 2025-08-01-preview introduces several new entities:
 
-* [**DateOfBirth**](concepts/entity-categories.md#category-datetime) with English, French, German, Italian, Spanish, Portuguese, Brazilian Portuguese, and Dutch language support.
-* [**LicensePlate**](concepts/entity-categories.md#type-license-plate-) with English language support.
-* [**SortCode**](concepts/entity-categories.md#type-sort-code-) with English language support.
+* [**DateOfBirth**](concepts/entity-categories.md#type-date-of-birth-preview) with English, French, German, Italian, Spanish, Portuguese, Brazilian Portuguese, and Dutch language support.
+* [**LicensePlate**](concepts/entity-categories.md#type-license-plate-preview) with English language support.
+* [**SortCode**](concepts/entity-categories.md#type-sort-code-preview) with English language support.
 
 
 The Text PII and Conversational PII detection preview API (version `2024-11-15-preview`) now supports the option to mask detected sensitive entities with a label beyond just redaction characters. Customers can specify if personal data content such as names and phone numbers, that is, `"John Doe received a call from 424-878-9192"`, are masked with a redaction character, that is, `"******** received a call from ************"`, or masked with an entity label, that is, `"[PERSON_1] received a call from [PHONENUMBER_1]"`. More on how to specify the redaction policy style for your outputs can be found in our [how-to guides](how-to-call.md). 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PII検出機能の概要におけるエンティティ情報の修正"
}
```

### Explanation
この変更では、Azure AI Languageのパーソナル識別情報（PII）検出機能に関する概要ドキュメントに小さな修正が加えられています。斜体のある新しいエンティティの記述において、3行が追加され、3行が削除され、合計6行の変更が行われました。

具体的な変更点は以下の通りです：

1. **エンティティタイプのリンク修正**:
   - 「DateOfBirth」、「LicensePlate」、「SortCode」の各エンティティのリンクが、関連するカテゴリに合わせて更新されました。具体的には、これらのリンクがリファレンスの構造を反映して「category-」から「type-」へ変更されています。

2. **機能の追加の明確化**:
   - 新しい機能として、検出された敏感エンティティを単に削除するだけでなく、ラベルでマスキングするオプションが追加されています。これにより、顧客は個人データの内容をどのように管理するかをより柔軟に指定できるようになります。

これにより、ドキュメントがより正確で使いやすくなり、新しい機能の利用方法が明確に示されています。ユーザーは、PII検出機能をより効果的に活用できるようになります。

## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -519,8 +519,10 @@ items:
             href: ../cognitive-services-container-support.md
     - name: Concepts
       items:
-      - name: Recognized entity categories
+      - name: Recognized entity types 🆕
         href: personally-identifiable-information/concepts/entity-categories.md
+      - name: Recognized entities list 🆕
+        href: personally-identifiable-information/concepts/entity-categories-list.md
       - name: Recognized entity categories for conversation
         href: personally-identifiable-information/concepts/conversations-entity-categories.md
   - name: Custom question answering
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCにおけるエンティティカテゴリおよびリストの更新"
}
```

### Explanation
この変更では、Azure AI Languageサービスの目次ファイル（toc.yml）に若干の修正が施され、新しいエンティティタイプに関する情報が追加されています。具体的には、3行が追加され、1行が削除され、合計4行の変更が記録されています。

主な変更点は以下の通りです：

1. **エンティティカテゴリの名称変更**:
   - 「Recognized entity categories」という名称が「Recognized entity types」に変更され、エンティティの種類に関する理解が深まるようになりました。

2. **新しいエンティティリストの追加**:
   - 追加された新しい項目「Recognized entities list」が、PIIに関連するエンティティの詳細なリストへリンクしています。これにより、ユーザーは特定の認識可能なエンティティの一覧を直接参照できるようになっています。

これらの変更によって、目次がより充実し、ユーザーが必要な情報に迅速にアクセスできるような構成となりました。

## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -14,6 +14,24 @@ ms.author: lajanuar
 
 Azure AI Language is updated on an ongoing basis. Bookmark this page to stay up to date with release notes, feature enhancements, and our newest documentation.
 
+## September 2025
+
+**Introducing CQA deploy-to-agent**. Custom Question Answering (CQA) projects can now be [deployed as intelligent agents](question-answering/how-to/deploy-agent.md) directly within the Azure AI Foundry playground through a streamlined deployment experience. 
+  * This feature enables users to transform fine-tuned CQA knowledge bases into production-ready agents with minimal configuration steps. 
+  * The deployment process provides parity with CLU workflows and accelerates the agent development timeline within the unified Foundry environment.
+
+**Custom Named Entity Recognition (NER) capabilities integrated into Language Playground**. Users can now access a testing playground for custom Named Entity Recognition (NER) within Azure AI Foundry. 
+  * This interactive interface allows training, deployment, testing, and fine-tuning for custom models while experimenting with custom NER capabilities in real-time.
+  * The playground accelerates the onboarding process and provides enhanced debugging capabilities for custom NER implementations. For more information, *see* [Quickstart: Custom named entity recognition](custom-named-entity-recognition/quickstart.md).
+
+**New Python SDKs**. The new Python SDKs [**azure-ai-textanalytics 6.0.0b1**](https://pypi.org/project/azure-ai-textanalytics/6.0.0b1/) and [**azure-ai-textanalytics-authoring 1.0.0b1**](https://pypi.org/project/azure-ai-textanalytics-authoring/1.0.0b1/) are now available:
+
+   * **azure-ai-textanalytics 6.0.0b1** offers runtime APIs that enable users to utilize various prebuilt features within Azure AI Language, such as sentiment analysis, named entity recognition (NER), language detection, key phrase extraction, text PII detection, Text Analytics for health, and document summarization.<br><br>Additionally, the SDK can be used to access inference APIs for custom NER and text classification models. This release supports the latest `2025-05-15-preview` API, and previous versions. The `2025-05-15-preview` API introduces several new capabilities:
+
+      * Added support for new entity types in [Named Entity Recognition (NER)](named-entity-recognition/concepts/named-entity-categories.md) and [Text PII detection](personally-identifiable-information/concepts/entity-categories.md): **DateOfBirth**, **BankAccountNumber**, **PassportNumber**, and **DriversLicenseNumber**.
+
+      * Enhanced functionality allows users to define values to be excluded from the results produced by Text PII detection.
+
 ## August 2025
 
 **Release of new Text PII and NER model (2025-08-01-preview)**. This new preview model version introduces broader functionality and expanded capabilities for Text personal information identification (PII) and named entity recognition (NER) services:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "What's Newページのアップデート"
}
```

### Explanation
この変更では、Azure AI Languageサービスの「What's New」ページに関して、2025年9月に追加された新機能や更新内容が詳細に記述されました。合計で18行の変更が加えられ、すべての行が新たに追加されています。

主な更新内容は以下の通りです：

1. **CQAデプロイメント機能の導入**:
   - カスタム質問応答（CQA）プロジェクトが、Azure AI Foundryプレイグラウンド内でインテリジェントエージェントとして直接デプロイできる新機能が紹介されました。この機能により、ユーザーは微調整されたCQA知識ベースを最小限の設定ステップで本番環境のエージェントに変換できます。

2. **カスタム命名エンティティ認識（NER）機能の統合**:
   - Azure AI Foundry内のテストプレイグラウンドにカスタムNERのインターフェースが追加され、ユーザーはリアルタイムでカスタムモデルのトレーニング、デプロイメント、テスト、および微調整を行うことができるようになりました。

3. **新しいPython SDKのリリース**:
   - 新しいPython SDK「azure-ai-textanalytics 6.0.0b1」と「azure-ai-textanalytics-authoring 1.0.0b1」が導入され、Azure AI Language内での感情分析、名寄せ認識（NER）、言語判定などの様々な事前構築機能の利用が可能になりました。また、最新のAPI「2025-05-15-preview」には新しいエンティティタイプやテキストPII検出の除外機能が追加されています。

これらのアップデートにより、ユーザーは最新の機能を活用しやすくなり、AI言語サービスの利用がさらにスムーズになります。


