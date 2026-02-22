---
date: '2026-02-22'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4c55324...MicrosoftDocs:6789bf3
summary: 今回の変更では、Azure Languageサービスにおいて会話型個人情報（PII）の検出機能と関連ドキュメントが改善されました。新たに「会話エンティティカテゴリリスト」が追加され、検出可能な個人情報の種類が一覧で示されることで、開発者やユーザーの理解が深まります。また、既存のドキュメントが見直され、情報の明確さと利用しやすさが向上しています。大きな破壊的変更はなく、エンティティタイプの表示形式や目次構成の改善が行われ、全体的な可読性とナビゲーションも向上しています。このアップデートにより、個人情報の管理リスクが軽減され、AIサービスの開発が効率化されることが期待されます。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:4c55324...MicrosoftDocs:6789bf3){target="_blank"}

# Highlights
今回の変更点では、Azure Languageサービス内での会話型個人情報（PII）検出に関する機能とドキュメントの改善が中心となっています。新しい機能としては、「会話エンティティカテゴリリスト」が追加され、一覧形式で提供されることで、開発者やユーザーがどのような個人情報が検出可能なのかを容易に理解できるようになっています。また、各ドキュメントの内容が見直されることで、情報の明確さと利用しやすさが向上しています。

## New features
- 「会話エンティティカテゴリリスト」の追加により、会話型の個人情報検出におけるエンティティタイプをリスト化し、詳細な情報へのリンクを提供。このリストには、銀行口座番号や健康カード番号などの多様なカテゴリが含まれる。
- エンティティごとにプレビュー版かどうかを示す注釈を追加。

## Breaking changes
特に大きな破壊的変更は報告されていませんが、全体として既存の情報が整理され、ユーザーにとってより明確になっている。

## Other updates
- 既存のドキュメントに対して、エンティティタイプの表示形式の改善や、目次構成の調整が行われ、可読性とナビゲーション性能が向上。
- 各エンティティの説明を保持しつつ、視覚的に強調される形式に統一。

# Insights
このリリースは、AzureのAIサービスにおける会話型データ処理の精度を高めることを狙った戦略的なアップデートといえます。最近の傾向として、デジタルプラットフォーム上でのデータ保護の需要が高まる中で、PII検出の能力向上は重要です。新エンティティカテゴリリストの追加により、開発者は特定の会話エンティティがどのように検出されるかを前もって知った上で、AIサービスを構築できるようになります。

この変更によって、手動で個人情報を管理するリスクが軽減され、自動化されたプロセスで処理されるデータのコンプライアンスが向上します。また、多様なエンティティタイプとその管理に関する明確な指針は、監査や法令遵守を含むさまざまなビジネスニーズにも応えるものです。

全体として、ユーザーエクスペリエンスの向上を意識した改良が随所に施されており、情報のアクセス効率が良くなるだけでなく、サービス自体の信頼性と競争力をも向上させるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [conversations-entities-list.md](#item-656953) | new feature | 会話型個人情報検出におけるエンティティカテゴリリストの追加 | added | 26 | 0 | 26 | 
| [conversations-entity-categories.md](#item-c268ff) | minor update | 会話型個人情報エンティティカテゴリに関する内容の改善 | modified | 197 | 137 | 334 | 
| [entity-categories-list.md](#item-05522d) | minor update | PIIエンティティカテゴリリストの更新 | modified | 63 | 62 | 125 | 
| [entity-categories.md](#item-ba2623) | minor update | エンティティカテゴリの表示形式の改善 | modified | 180 | 180 | 360 | 
| [toc.yml](#item-12f1f0) | minor update | エンティティカテゴリの構成の改善 | modified | 14 | 9 | 23 | 


# Modified Contents
## articles/ai-services/language-service/personally-identifiable-information/concepts/conversations-entities-list.md{#item-656953}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,26 @@
+---
+title: Entity categories list recognized by Conversational Personally Identifiable Information (PII) detection in Azure Language in Foundry Tools
+titleSuffix: Foundry Tools
+description: View a list of entity types the conversational PII feature can detect and identify within conversation inputs.
+author: laujan
+manager: nitinme
+ms.service: azure-ai-language
+ms.topic: concept-article
+ms.date: 02/17/2026
+ms.author: lajanuar
+---
+<!-- markdownlint-disable MD025 -->
+# Recognized conversational PII entities list
+
+| &nbsp; | Entities | &nbsp; |
+| :--: | :--: | :--: |
+| &#8226; [ABA Routing Number (**preview**)](conversations-entity-categories.md#type-aba-routing-number-preview) | &#8226; [Address](conversations-entity-categories.md#type-address) | &#8226; [Age (**preview**)](conversations-entity-categories.md#type-age-preview) |
+| &#8226; [Bank Account Number (**preview**)](conversations-entity-categories.md#type-bank-account-number-preview) | &#8226; [Canada Social Insurance Number (**preview**)](conversations-entity-categories.md#type-canada-social-insurance-number-preview) | &#8226; [Credit Card](conversations-entity-categories.md#type-credit-card) |
+| &#8226; [CVV (**preview**)](conversations-entity-categories.md#type-card-verification-value-cvv-preview) | &#8226; [Date (**preview**)](conversations-entity-categories.md#type-date-preview) | &#8226; [Date Of Birth (**preview**)](conversations-entity-categories.md#type-date-of-birth-preview) |
+| &#8226; [Drivers License Number (**preview**)](conversations-entity-categories.md#type-drivers-license-number-preview) | &#8226; [Email](conversations-entity-categories.md#type-email) | &#8226; [GitHub Account (**preview**)](conversations-entity-categories.md#type-github-account-preview) |
+| &#8226; [Government Issued ID (**preview**)](conversations-entity-categories.md#type-government-issued-id-preview) | &#8226; [GPE (**preview**)](conversations-entity-categories.md#type-geopolitical-entity-gpe-preview) | &#8226; [Health Card Number (**preview**)](conversations-entity-categories.md#type-health-card-number-preview) |
+| &#8226; [International Banking Account Number (**preview**)](conversations-entity-categories.md#type-international-banking-account-number-preview) | &#8226; [Location (**preview**)](conversations-entity-categories.md#type-location-preview) | &#8226; [Numeric Identifier](conversations-entity-categories.md#type-numeric-identifier) |
+| &#8226; [Organization (**preview**)](conversations-entity-categories.md#type-organization-preview) | &#8226; [Passport Number (**preview**)](conversations-entity-categories.md#type-passport-number-preview) | &#8226; [Person](conversations-entity-categories.md#type-person) |
+| &#8226; [Person Type (**preview**)](conversations-entity-categories.md#type-person-type-preview) | &#8226; [Phone Number](conversations-entity-categories.md#type-phone-number) | &#8226; [SWIFT Code (**preview**)](conversations-entity-categories.md#type-swift-code-preview) |
+| &#8226; [United States Medicare Beneficiary ID (**preview**)](conversations-entity-categories.md#type-united-states-medicare-beneficiary-id-preview) | &#8226; [United States Social Security Number](conversations-entity-categories.md#type-united-states-social-security-number) | &#8226; [Vehicle Identification Number (**preview**)](conversations-entity-categories.md#type-vehicle-identification-number-preview) |
+| &#8226; [ZipCode (**preview**)](conversations-entity-categories.md#type-zipcode-preview) | | |
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "会話型個人情報検出におけるエンティティカテゴリリストの追加"
}
```

### Explanation
この変更は、Azure Languageサービス内の会話型個人情報（PII）検出機能に関する新しいコンテンツを追加します。具体的には、「会話エンティティカテゴリリスト」として知られるマークダウンファイルが新たに作成されました。このファイルは、会話の入力から認識されるエンティティタイプを一覧表示しており、各エンティティについての詳細リンクも含まれています。

新しいセクションには、エンティティの名前と、これらがプレビュー版かどうかを示す注釈があり、様々な個人情報のカテゴリーが示されています。これにより、開発者やユーザーがどのようなデータが検出されるかを理解しやすくなることで、より効果的にサービスを使用できるようになります。

新しいエンティティリストには、以下の情報が含まれています：
- 銀行口座番号やクレジットカード、運転免許証番号などの個人データ
- 地理的エンティティや健康カード番号も含む幅広いエンティティカテゴリ

この変更は、利用者が会話型プラットフォームでのデータ管理に関して、有用なガイダンスを得られることを目的としています。

## articles/ai-services/language-service/personally-identifiable-information/concepts/conversations-entity-categories.md{#item-c268ff}

<details>
<summary>Diff</summary>
````diff
@@ -1,204 +1,264 @@
 ---
-title: Entity categories recognized by Conversational Personally Identifiable Information (detection) in Azure Language in Foundry Tools
+title: Entity categories recognized by Conversational Personally Identifiable Information (PII) detection in Azure Language in Foundry Tools
 titleSuffix: Foundry Tools
-description: Learn about the entities the Conversational PII feature can recognize from conversation inputs.
+description: Learn about the types of entities the conversational PII feature can detect and identify within conversation inputs.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: concept-article
-ms.date: 11/18/2025
+ms.date: 02/17/2026
 ms.author: lajanuar
-ms.custom: language-service-pii, build-2024
 ---
-# Supported customer content (PII) entity categories in conversations
 
-Use this article to find the entity categories that can be returned by the [conversational PII detection feature](../how-to-call-for-conversations.md). This feature runs a predictive model to identify, categorize, and redact sensitive information from an input conversation.
+<!-- markdownlint-disable MD025 -->
+# Recognized conversational **PII** entities
 
-## Entity categories
+The conversational Personally Identifiable Information (PII) detection API uses AI and machine learning to detect and redact sensitive information in conversation inputs.
 
-The following entity categories are returned when you're sending API requests PII feature.
+The API categorizes personal details into predefined entity types for precise identification and removal. Detecting and redacting PII helps ensure compliance with privacy regulations and enables your applications to handle data securely.
 
-## Category: Person
+> [!TIP]
+> Try PII detection in text or conversations using the [Microsoft Foundry](https://ai.azure.com/explore/language) language playground.
 
-This category contains the following entity:
+### Language Support
 
-:::row:::
-    :::column span="":::
-        **Entity**
+The [PII language support page](../language-support.md) lists all languages available for the PII entities in this article. Any exceptions are noted for specific named entities.
 
-        Name
+Supported API versions:
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+* [**Stable 2024-11-01: Generally Available (GA)**](/rest/api/language/analyze-conversations/operation-groups?view=rest-language-analyze-conversations-2024-11-01&preserve-view=true)
+* [**Preview: 2025-11-15-preview**](/rest/api/language/analyze-conversations/operation-groups?view=rest-language-analyze-conversations-2025-11-15-preview&preserve-view=true)
 
-        All first, middle, last or full name is considered PII regardless of whether it is the speaker’s name, the agent’s name, someone else’s name or a different version of the speaker’s full name (Chris vs. Christopher). 
+The following entities are currently in preview:
 
-        To get this entity category, add `Person` to the `pii-categories` parameter. `Person` will be returned in the API response if detected. 
-        > [!NOTE]
-        > As of the 2023-04-15-preview API onwards, this category is 'Person' instead of 'Name'.
-      
-    :::column-end:::
-    
-    :::column span="":::
-      **Supported document languages**
+* [ABARoutingNumber](#type-aba-routing-number-preview)
+* [Age](#type-age-preview)
+* [BankAccountNumber](#type-bank-account-number-preview)
+* [CASocialInsuranceNumber](#type-canada-social-insurance-number-preview)
+* [CVV (Card Verification Value)](#type-card-verification-value-cvv-preview)
+* [Date](#type-date-preview)
+* [DateOfBirth](#type-date-of-birth-preview)
+* [DriversLicenseNumber](#type-drivers-license-number-preview)
+* [GithubAccount](#type-github-account-preview)
+* [GovernmentIssuedId](#type-government-issued-id-preview)
+* [GPE (Geopolitical Entity)](#type-geopolitical-entity-gpe-preview)
+* [HealthCardNumber](#type-health-card-number-preview)
+* [InternationalBankingAccountNumber](#type-international-banking-account-number-preview)
+* [Location](#type-location-preview)
+* [Organization](#type-organization-preview)
+* [PassportNumber](#type-passport-number-preview)
+* [PersonType](#type-person-type-preview)
+* [SWIFTCode](#type-swift-code-preview)
+* [USMedicareBeneficiaryId](#type-united-states-medicare-beneficiary-id-preview)
+* [VehicleIdentificationNumber](#type-vehicle-identification-number-preview)
+* [ZipCode](#type-zipcode-preview)
 
-      `en`  
-   :::column-end:::
-:::row-end:::
+### Supported conversational PII entity list
 
-## Category: Phone
+To examine a comprehensive list of all the types of conversational PII entities that are currently supported, *see* the [Supported conversational PII entity list](conversations-entities-list.md) article.
 
-This category contains the following entity:
+### Supported conversational PII extraction entities
 
-:::row:::
-    :::column span="":::
-        **Entity**
+Personally identifiable information (PII) refers to any single piece of data or combination of data that enables the unique identification, tracking, or differentiation of an individual.
 
-        Phone
+The Azure Language in Foundry Tools conversational PII extraction API uses Natural Language Processing (NLP) technology to detect, recognize, and extract PII entities from conversations. The following entities represent specific types of information that can reveal an individual's identity:
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+## Geolocation
 
-        All telephone numbers (including toll-free numbers or numbers that may be easily found or considered public knowledge) are considered PII
+Geolocation data identifies an individual's physical position or movement patterns. This data qualifies as PII when it can be associated with a specific person.
 
-        To get this entity category, add `Phone` to the `pii-categories` parameter. `Phone` will be returned in the API response if detected.
-      
-    :::column-end:::
+### Type: Geopolitical Entity GPE (preview)
 
-    :::column span="":::
-      **Supported document languages**
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **GPE** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payloads.|[**GPE**]|
 
-      `en`
-      
-   :::column-end:::
+### Type: Location (preview)
 
-:::row-end:::
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **Location** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payloads.|[**Location**]|
 
-## Category: Address
+### Type: ZipCode (preview)
 
-This category contains the following entity:
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **ZipCode** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payloads.|[**ZipCode**]|
 
-:::row:::
-    :::column span="":::
-        **Entity**
+## Personal
 
-        Address
+Any data, collected or stored, that can be used to identify or contact a specific individual is considered personal information. This data may include information that identifies someone directly, such as their name or social security number. It can also refer to data that, when linked with other information, could lead to identification---for example, an address or dates of birth.
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+### Type: Address
 
-        Complete or partial addresses are considered PII. All addresses regardless of what residence or institution the address belongs to (such as: personal residence, business, medical center, government agency, etc.) are covered under this category.        
-        Note:  
-            * If information is limited to City & State only, it will not be considered PII.  
-            * If information contains street, zip code or house number, all information is considered as Address PII , including the city and state
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **Address** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payloads.|[**Address**]|
 
-        To get this entity category, add `Address` to the `pii-categories` parameter. `Address` will be returned in the API response if detected.
+### Type: Age (preview)
 
-    :::column-end:::
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **Age** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payload.|[**Age**]|
 
-    :::column span="":::
-      **Supported document languages**
+### Type: Date Of Birth (preview)
 
-      `en`
-      
-    :::column-end:::
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **DateOfBirth** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payload.|[**DateOfBirth**]|
 
-:::row-end:::
+### Type: Drivers License Number (preview)
 
-## Category: Email
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **DriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payload.|[**DriversLicenseNumber**]|
 
-This category contains the following entity:
+### Type: Email
 
-:::row:::
-    :::column span="":::
-        **Entity**
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **Email** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payloads.|[**Email**]|
 
-        Email
+### Type: Passport Number (preview)
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **PassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payload.|[**PassportNumber**]|
 
-        All email addresses are considered PII.
-      
-        To get this entity category, add `Email` to the `pii-categories` parameter. `Email` will be returned in the API response if detected.
+### Type: Person
 
-    :::column-end:::
-    :::column span="":::
-      **Supported document languages**
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **Person** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payloads.|[**Person**]|
 
-      `en`
-      
-    :::column-end:::
-:::row-end:::
+### Type: Person Type (preview)
 
-## Category: NumericIdentifier
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **PersonType** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payload.|[**PersonType**]|
 
-This category contains the following entities:
+### Type: Phone Number
 
-:::row:::
-    :::column span="":::
-        **Entity**
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **Phone** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payloads.|[**Phone**]|
 
-        NumericIdentifier 
+### Type: Vehicle Identification Number (preview)
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **VehicleIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payload.|[**VehicleIdentificationNumber**]|
 
-        Any numeric or alphanumeric identifier that could contain any PII information. 
-        Examples:   
-            * Case Number 
-            * Member Number 
-            * Ticket number 
-            * Bank account number 
-            * Installation ID 
-            * IP Addresses 
-            * Product Keys 
-            * Serial Numbers (1:1 relationship with a specific item/product) 
-            * Shipping tracking numbers, etc.
+## Financial
 
-        To get this entity category, add `NumericIdentifier` to the `pii-categories` parameter. `NumericIdentifier` will be returned in the API response if detected.
-      
-    :::column-end:::
-    :::column span="2":::
-      **Supported document languages**
+Any financial information is connected to a particular individual that can, through identifying details, be traced back to that person.
 
-      `en`
-      
-    :::column-end:::
-:::row-end:::
+### Type: ABA Routing Number (preview)
 
-## Category: Credit card
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **ABARoutingNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payload.|[**ABARoutingNumber**]|
 
-This category contains the following entity:
+### Type: Bank Account Number (preview)
 
-:::row:::
-    :::column span="":::
-        **Entity**
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **BankAccountNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payload.|[**BankAccountNumber**]|
 
-        Credit card
+### Type: Card Verification Value CVV (preview)
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **CVV** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payload.|[**CVV**]|
 
-        Any credit card number, any security code on the back, or the expiration date is considered as PII.
+### Type: Credit Card
 
-        To get this entity category, add `CreditCard` to the `pii-categories` parameter. `CreditCard` will be returned in the API response if detected.
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **CreditCard** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payload.|[**CreditCard**]|
 
-    :::column-end:::
-    :::column span="2":::
-      **Supported document languages**
+### Type: International Banking Account Number (preview)
 
-      `en`
-      
-   :::column-end:::
-:::row-end:::
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **InternationalBankingAccountNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payload.|[**InternationalBankingAccountNumber**]|
 
-## Next steps
+### Type: SWIFT Code (preview)
 
-[How to detect PII in conversations](../how-to-call-for-conversations.md)
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **SWIFTCode** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payload.|[**SWIFTCode**]|
+
+## Organizational
+
+Any data that an organization collects, stores, or processes that can be used to identify a specific individual, either directly or indirectly.
+
+### Type: Organization (preview)
+
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **Organization** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payloads.|[**Organization**]|
+
+## DateTime
+
+Data that can be used to identify, distinguish, or trace an individual. While a date or time on its own is often not considered PII, it can become highly sensitive when combined with other data points.
+
+### Type: Date (preview)
+
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **Date** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payloads.|[**Date**]|
+
+## Digital
+
+Any identifiable digital information that can be used to distinguish or trace an individual's identity.
+
+### Type: GitHub Account (preview)
+
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **GithubAccount** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payload.|[**GithubAccount**]|
+
+### Type: Numeric Identifier
+
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **NumericIdentifier** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payload. Covers numeric or alphanumeric identifiers such as case numbers, member numbers, ticket numbers, bank account numbers, IP addresses, product keys, serial numbers, and shipping tracking numbers.|[**NumericIdentifier**]|
+
+## Government
+
+Any government-issued identification that can be used alone or combined with other data to trace and reveal a specific person's identity.
+
+### Type: Canada Social Insurance Number (preview)
+
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **CASocialInsuranceNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payload.|[**CASocialInsuranceNumber**]|
+
+### Type: Government Issued ID (preview)
+
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **GovernmentIssuedId** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payload.|[**GovernmentIssuedId**]|
+
+### Type: Health Card Number (preview)
+
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **HealthCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payload.|[**HealthCardNumber**]|
+
+### Type: United States Medicare Beneficiary ID (preview)
+
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **USMedicareBeneficiaryId** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payload.|[**USMedicareBeneficiaryId**]|
+
+### Type: United States Social Security Number
+
+|Details|Tag|
+|---|---|
+|To retrieve this entity type, specify **USSocialSecurityNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **conversational PII** response payload.|[**USSocialSecurityNumber**]|
+
+## Related content
+
+[Conversational PII entity categories list](conversations-entities-list.md) - A comprehensive list of all the types of conversational PII entities that are currently supported.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "会話型個人情報エンティティカテゴリに関する内容の改善"
}
```

### Explanation
この変更は、Azureの会話型個人情報（PII）エンティティカテゴリに関するドキュメントの内容を更新および改善するものです。具体的には、エンティティの定義や説明、カテゴリーの構造を見直し、情報をより明確に伝えることを目的としています。

主な変更点は以下の通りです：
- タイトルには「PII」の省略形を明確にし、内容説明を微調整して、より具体的にエンティティの種類を認識すると説明するようにしました。
- PII検出APIの機能について、より詳細な情報を追加し、AIと機械学習がどのようにしてセンシティブな情報を検出、分類、非表示化するかを説明するセクションを強化しました。
- 各エンティティのカテゴリーについて具体的な実装情報を提供し、APIリクエストに含める際のパラメータに関する情報を追加しました。
- 新たにいくつかのPIIエンティティの種類をリスト化し、それぞれにアクセス方法を示すための詳細なタグ付けを行いました。

これらの変更は、利用者がドキュメントを参照する際に、情報を容易に理解できるようにするとともに、新たにサポートされているエンティティのリストを詳細に提供し、APIを効果的に利用する手助けをすることを目的としています。

## articles/ai-services/language-service/personally-identifiable-information/concepts/entity-categories-list.md{#item-05522d}

<details>
<summary>Diff</summary>
````diff
@@ -12,66 +12,67 @@ ms.custom:
   - language-service-pii
   - sfi-ropc-nochange
 ---
-# Recognized PII entities list
+<!-- markdownlint-disable MD025 -->
+# Recognized text PII entities list
 
-| Entity | Entity | Entity |
-| -- | -- | -- |
-| [Address](entity-categories.md#type-address) | [Age](entity-categories.md#type-age) | [American Bankers Association Routing Number](entity-categories.md#type-american-bankers-association-routing-number) |
-| [Airport 🆕](entity-categories.md#type-airport-preview) | [Argentina National Identity Number](entity-categories.md#type-argentina-national-identity-number) | [Australia Bank Account Number](entity-categories.md#type-australia-bank-account-number) |
-| [Australia Business Number](entity-categories.md#type-australia-business-number) | [Australia Company Number](entity-categories.md#type-australia-company-number) | [Australia Drivers License Number](entity-categories.md#type-australia-drivers-license-number) |
-| [Australia Medical Account Number](entity-categories.md#type-australia-medical-account-number) | [Australia Passport Number](entity-categories.md#type-australia-passport-number) | [Australia Tax File Number](entity-categories.md#type-australia-tax-file-number) |
-| [Austria Identity Card](entity-categories.md#type-austria-identity-card) | [Austria Tax Identification Number](entity-categories.md#type-austria-tax-identification-number) | [Austria Value Added Tax Number](entity-categories.md#type-austria-value-added-tax-number) |
-| [Azure Document DB Auth Key](entity-categories.md#type-azure-document-db-auth-key) | [Azure IAAS Database Connection And SQL String](entity-categories.md#type-azure-iaas-database-connection-and-sql-string) | [Azure IoT Connection String](entity-categories.md#type-azure-iot-connection-string) |
-| [Azure Publish Setting Password](entity-categories.md#type-azure-publish-setting-password) | [Azure Redis Cache String](entity-categories.md#type-azure-redis-cache-string) | [Azure SAS](entity-categories.md#type-azure-sas) |
-| [Azure Service Bus String](entity-categories.md#type-azure-service-bus-string) | [Azure Storage Account Generic](entity-categories.md#type-azure-storage-account-generic) | [Azure Storage Account Key](entity-categories.md#type-azure-storage-account-key) |
-| [Bank Account Number 🆕](entity-categories.md#type-bank-account-number-preview) | [Belgium National Number](entity-categories.md#type-belgium-national-number) | [Belgium Value Added Tax Number](entity-categories.md#type-belgium-value-added-tax-number) |
-| [Brazil CPF Number](entity-categories.md#type-brazil-cpf-number) | [Brazil Legal Entity Number](entity-categories.md#type-brazil-legal-entity-number) | [Brazil National IDRG](entity-categories.md#type-brazil-national-idrg) |
-| [Bulgaria Uniform Civil Number](entity-categories.md#type-bulgaria-uniform-civil-number) | [Canada Bank Account Number](entity-categories.md#type-canada-bank-account-number) | [Canada Drivers License Number](entity-categories.md#type-canada-drivers-license-number) |
-| [Canada Health Service Number](entity-categories.md#type-canada-health-service-number) | [Canada Passport Number](entity-categories.md#type-canada-passport-number) | [Canada Personal Health Identification](entity-categories.md#type-canada-personal-health-identification) |
-| [Canada Social Insurance Number](entity-categories.md#type-canada-social-insurance-number) | [Canada Social Identification Number 🆕](entity-categories.md#type-canada-social-identification-number-preview) | [Chile Identity Card Number](entity-categories.md#type-chile-identity-card-number) |
-| [China Resident Identity Card Number](entity-categories.md#type-china-resident-identity-card-number) | [City 🆕](entity-categories.md#type-city-preview) | [Credit Card Number](entity-categories.md#type-credit-card-number) |
-| [Croatia Identity Card Number](entity-categories.md#type-croatia-identity-card-number) | [City 🆕](entity-categories.md#type-city-preview) |[Croatia National ID Number](entity-categories.md#type-croatia-national-id-number) |
-| [Croatia Personal Identification Number](entity-categories.md#type-croatia-personal-identification-number) | [CVV 🆕](entity-categories.md#type-card-verification-value-cvv-preview) | [Cyprus Identity Card](entity-categories.md#type-cyprus-identity-card) |
-| [Cyprus Tax Identification Number](entity-categories.md#type-cyprus-tax-identification-number) | [Date](entity-categories.md#type-date) | [Date Of Birth 🆕](entity-categories.md#type-date-of-birth-preview) |
-| [Denmark Personal Identification Number](entity-categories.md#type-denmark-personal-identification-number) | [Drivers License Number 🆕](entity-categories.md#type-drivers-license-number-preview) | [Email](entity-categories.md#type-email) | 
-| [Estonia Personal Identification Code](entity-categories.md#type-estonia-personal-identification-code) | [European Union Debit Card Number](entity-categories.md#type-european-union-debit-card-number) | [European Union Drivers License Number](entity-categories.md#type-european-union-drivers-license-number) |
-| [European Union GPS Coordinates](entity-categories.md#type-european-union-gps-coordinates) | [European Union National Identification Number](entity-categories.md#type-european-union-national-identification-number) | [European Union Passport Number](entity-categories.md#type-european-union-passport-number) |
-| [European Union Social Security Number](entity-categories.md#type-european-union-social-security-number) | [European Union Tax Identification Number](entity-categories.md#type-european-union-tax-identification-number) | [Expiration Date 🆕](entity-categories.md#type-expiration-date-preview) |
-| [Finland European Health Number](entity-categories.md#type-finland-european-health-number) | [Finland National ID](entity-categories.md#type-finland-national-id) | [Finland Passport Number](entity-categories.md#type-finland-passport-number) |
-| [France Drivers License Number](entity-categories.md#type-france-drivers-license-number) | [France National ID](entity-categories.md#type-france-national-id) | [France Passport Number](entity-categories.md#type-france-passport-number) |
-| [France Social Security Number](entity-categories.md#type-france-social-security-number) | [France Tax Identification Number](entity-categories.md#type-france-tax-identification-number) | [France Value Added Tax Number](entity-categories.md#type-france-value-added-tax-number) |
-| [Germany Drivers License Number](entity-categories.md#type-germany-drivers-license-number) | [Germany Identity Card Number](entity-categories.md#type-germany-identity-card-number) | [Germany Passport Number](entity-categories.md#type-germany-passport-number) |
-| [Germany Tax Identification Number](entity-categories.md#type-germany-tax-identification-number) | [Germany Value Added Number](entity-categories.md#type-germany-value-added-number) | [GPE 🆕](entity-categories.md#type-geopolitical-entity-gpe-preview) |
-| [Greece National ID Card](entity-categories.md#type-greece-national-id-card) | [Greece Tax Identification Number](entity-categories.md#type-greece-tax-identification-number) | [Hong Kong SAR Identity Card Number](entity-categories.md#type-hong-kong-sar-identity-card-number) |
-| [Hungary Personal Identification Number](entity-categories.md#type-hungary-personal-identification-number) | [Hungary Value Added Number](entity-categories.md#type-hungary-value-added-number) | [India Permanent Account](entity-categories.md#type-india-permanent-account) |
-| [India Unique Identification Number](entity-categories.md#type-india-unique-identification-number) | [Indonesia Identity Card Number](entity-categories.md#type-indonesia-identity-card-number) | [International Banking Account Number](entity-categories.md#type-international-banking-account-number) |
-| [IP Address](entity-categories.md#type-ip-address) | [Ireland Personal Public Service Number](entity-categories.md#type-ireland-personal-public-service-number) | [Israel Bank Account Number](entity-categories.md#type-israel-bank-account-number) |
-| [Israel National ID](entity-categories.md#type-israel-national-id) | [Italy Drivers License Number](entity-categories.md#type-italy-drivers-license-number) | [Italy Fiscal Code](entity-categories.md#type-italy-fiscal-code) |
-| [Italy Value Added Tax Number](entity-categories.md#type-italy-value-added-tax-number) | [Japan Bank Account Number](entity-categories.md#type-japan-bank-account-number) | [Japan Drivers License Number](entity-categories.md#type-japan-drivers-license-number) |
-| [Japan My Number Corporate](entity-categories.md#type-japan-my-number-corporate) | [Japan My Number Personal](entity-categories.md#type-japan-my-number-personal) | [Japan Passport Number](entity-categories.md#type-japan-passport-number) |
-| [Japan Residence Card Number](entity-categories.md#type-japan-residence-card-number) | [Japan Resident Registration Number](entity-categories.md#type-japan-resident-registration-number) | [Japan Social Insurance Number](entity-categories.md#type-japan-social-insurance-number) |
-| [Latvia Personal Code](entity-categories.md#type-latvia-personal-code) | [License Plate 🆕](entity-categories.md#type-license-plate-preview) | [Lithuania Personal Code](entity-categories.md#type-lithuania-personal-code) |
-| [Location 🆕](entity-categories.md#type-location-preview) | [Luxembourg National Identification Number Natural](entity-categories.md#type-luxembourg-national-identification-number-natural) | [Luxembourg National Identification Number Non Natural](entity-categories.md#type-luxembourg-national-identification-number-non-natural) |
-| [Malaysia Identity Card Number](entity-categories.md#type-malaysia-identity-card-number) | [Malta Identity Card Number](entity-categories.md#type-malta-identity-card-number) | [Malta Tax ID Number](entity-categories.md#type-malta-tax-id-number) |
-| [Netherlands Citizens Service Number](entity-categories.md#type-netherlands-citizens-service-number) | [Netherlands Tax Identification Number](entity-categories.md#type-netherlands-tax-identification-number) | [Netherlands Value Added Tax Number](entity-categories.md#type-netherlands-value-added-tax-number) |
-| [New Zealand Bank Account Number](entity-categories.md#type-new-zealand-bank-account-number) | [New Zealand Drivers License Number](entity-categories.md#type-new-zealand-drivers-license-number) | [New Zealand Inland Revenue Number](entity-categories.md#type-new-zealand-inland-revenue-number) |
-| [New Zealand Ministry Of Health Number](entity-categories.md#type-new-zealand-ministry-of-health-number) | [New Zealand Social Welfare Number](entity-categories.md#type-new-zealand-social-welfare-number) | [Norway Identity Number](entity-categories.md#type-norway-identity-number) |
-| [Organization](entity-categories.md#type-organization) | [Passport Number 🆕](entity-categories.md#type-passport-number-preview) | [Password 🆕](entity-categories.md#type-password-preview) |
-| [Person](entity-categories.md#type-person) | [Philippines Unified Multi Purpose ID Number](entity-categories.md#type-philippines-unified-multi-purpose-id-number) | [Phone Number](entity-categories.md#type-phone-number) |
-| [Poland Identity Card](entity-categories.md#type-poland-identity-card) | [Poland National ID](entity-categories.md#type-poland-national-id) | [Poland Passport Number](entity-categories.md#type-poland-passport-number) |
-| [Poland REGON Number](entity-categories.md#type-poland-regon-number) | [Poland Tax Identification Number](entity-categories.md#type-poland-tax-identification-number) | [Portugal Tax Identification Number](entity-categories.md#type-portugal-tax-identification-number) |
-| [Romania Personal Numerical Code](entity-categories.md#type-romania-personal-numerical-code) | [Russia Passport Number Domestic](entity-categories.md#type-russia-passport-number-domestic) | [Russia Passport Number International](entity-categories.md#type-russia-passport-number-international) |
-| [Saudi Arabia National ID](entity-categories.md#type-saudi-arabia-national-id) | [Singapore National Registration Identity Card Number](entity-categories.md#type-singapore-national-registration-identity-card-number) | [Slovakia Personal Number](entity-categories.md#type-slovakia-personal-number) |
-| [Slovenia Tax Identification Number](entity-categories.md#type-slovenia-tax-identification-number) | [Slovenia Unique Master Citizen Number](entity-categories.md#type-slovenia-unique-master-citizen-number) | [Sort Code 🆕](entity-categories.md#type-sort-code-preview) |
-| [South Africa Identification Number](entity-categories.md#type-south-africa-identification-number) | [South Korea Drivers License Number 🆕](entity-categories.md#type-south-korea-drivers-license-number-preview) | [South Korea Passport Number 🆕](entity-categories.md#type-south-korea-passport-number-preview) |
-| [South Korea Resident Registration Number](entity-categories.md#type-south-korea-resident-registration-number) | [South Korea Social Security Number 🆕](entity-categories.md#type-south-korea-social-security-number-preview) | [Spain DNI](entity-categories.md#type-spain-dni) |
-|[Spain Social Security Number](entity-categories.md#type-spain-social-security-number) | [Spain Tax Identification Number](entity-categories.md#type-spain-tax-identification-number) | [SQL Server Connection String](entity-categories.md#type-sql-server-connection-string) |
-| [State 🆕](entity-categories.md#type-state-preview) | [Sweden National ID](entity-categories.md#type-sweden-national-id) | [Sweden Passport Number](entity-categories.md#type-sweden-passport-number) |
-|[Sweden Tax Identification Number](entity-categories.md#type-sweden-tax-identification-number) | [SWIFT Code](entity-categories.md#type-swift-code) | [Taiwanese ID](entity-categories.md#type-taiwanese-id) |
-| [Taiwan Passport Number](entity-categories.md#type-taiwan-passport-number) | [Taiwan Resident Certificate](entity-categories.md#type-taiwan-resident-certificate) | [Thailand Population Identification Code](entity-categories.md#type-thailand-population-identification-code) |
-| [Türkiye National Identification Number](entity-categories.md#type-türkiye-national-identification-number) | [Ukraine Passport Number Domestic](entity-categories.md#type-ukraine-passport-number-domestic) | [Ukraine Passport Number International](entity-categories.md#type-ukraine-passport-number-international) |
-| [United Kingdom Drivers License Number](entity-categories.md#type-united-kingdom-drivers-license-number) | [United Kingdom Electoral Roll Number](entity-categories.md#type-united-kingdom-electoral-roll-number) | [United Kingdom National Health Number](entity-categories.md#type-united-kingdom-national-health-number) |
-| [United Kingdom National Insurance Number](entity-categories.md#type-united-kingdom-national-insurance-number) | [United Kingdom Unique Taxpayer Number](entity-categories.md#type-united-kingdom-unique-taxpayer-number) | [United States Bank Account Number](entity-categories.md#type-united-states-bank-account-number) |
-| [United States Drivers License Number](entity-categories.md#type-united-states-drivers-license-number) | [United States Drug Enforcement Agency Number](entity-categories.md#type-united-states-drug-enforcement-agency-number) |[United States Individual Taxpayer Identification](entity-categories.md#type-united-states-individual-taxpayer-identification) |
-| [United States Medicare Beneficiary Id 🆕](entity-categories.md#type-united-states-medicare-beneficiary-identification-preview) | [United States Social Security Number](entity-categories.md#type-united-states-social-security-number) | [United States/United Kingdom Passport Number](entity-categories.md#type-united-statesunited-kingdom-passport-number) |
-| [URL](entity-categories.md#type-url) | [VIN 🆕](entity-categories.md#type-vin-preview) | [ZipCode 🆕](entity-categories.md#type-zipcode-preview) |
+| &nbsp; | Entities | &nbsp; |
+| :--: | :--: | :--: |
+| &#8226; [Address](entity-categories.md#type-address) | &#8226; [Age](entity-categories.md#type-age) | &#8226; [American Bankers Association Routing Number](entity-categories.md#type-american-bankers-association-routing-number) |
+| &#8226; [Airport (**preview**)](entity-categories.md#type-airport-preview) | &#8226; [Argentina National Identity Number](entity-categories.md#type-argentina-national-identity-number) | &#8226; [Australia Bank Account Number](entity-categories.md#type-australia-bank-account-number) |
+| &#8226; [Australia Business Number](entity-categories.md#type-australia-business-number) | &#8226; [Australia Company Number](entity-categories.md#type-australia-company-number) | &#8226; [Australia Drivers License Number](entity-categories.md#type-australia-drivers-license-number) |
+| &#8226; [Australia Medical Account Number](entity-categories.md#type-australia-medical-account-number) | &#8226; [Australia Passport Number](entity-categories.md#type-australia-passport-number) | &#8226; [Australia Tax File Number](entity-categories.md#type-australia-tax-file-number) |
+| &#8226; [Austria Identity Card](entity-categories.md#type-austria-identity-card) | &#8226; [Austria Tax Identification Number](entity-categories.md#type-austria-tax-identification-number) | &#8226; [Austria Value Added Tax Number](entity-categories.md#type-austria-value-added-tax-number) |
+| &#8226; [Azure Document DB Auth Key](entity-categories.md#type-azure-document-db-auth-key) | &#8226; [Azure IAAS Database Connection And SQL String](entity-categories.md#type-azure-iaas-database-connection-and-sql-string) | &#8226; [Azure IoT Connection String](entity-categories.md#type-azure-iot-connection-string) |
+| &#8226; [Azure Publish Setting Password](entity-categories.md#type-azure-publish-setting-password) | &#8226; [Azure Redis Cache String](entity-categories.md#type-azure-redis-cache-string) | &#8226; [Azure SAS](entity-categories.md#type-azure-sas) |
+| &#8226; [Azure Service Bus String](entity-categories.md#type-azure-service-bus-string) | &#8226; [Azure Storage Account Generic](entity-categories.md#type-azure-storage-account-generic) | &#8226; [Azure Storage Account Key](entity-categories.md#type-azure-storage-account-key) |
+| &#8226; [Bank Account Number (**preview**)](entity-categories.md#type-bank-account-number-preview) | &#8226; [Belgium National Number](entity-categories.md#type-belgium-national-number) | &#8226; [Belgium Value Added Tax Number](entity-categories.md#type-belgium-value-added-tax-number) |
+| &#8226; [Brazil CPF Number](entity-categories.md#type-brazil-cpf-number) | &#8226; [Brazil Legal Entity Number](entity-categories.md#type-brazil-legal-entity-number) | &#8226; [Brazil National IDRG](entity-categories.md#type-brazil-national-idrg) |
+| &#8226; [Bulgaria Uniform Civil Number](entity-categories.md#type-bulgaria-uniform-civil-number) | &#8226; [Canada Bank Account Number](entity-categories.md#type-canada-bank-account-number) | &#8226; [Canada Drivers License Number](entity-categories.md#type-canada-drivers-license-number) |
+| &#8226; [Canada Health Service Number](entity-categories.md#type-canada-health-service-number) | &#8226; [Canada Passport Number](entity-categories.md#type-canada-passport-number) | &#8226; [Canada Personal Health Identification](entity-categories.md#type-canada-personal-health-identification) |
+| &#8226; [Canada Social Insurance Number](entity-categories.md#type-canada-social-insurance-number) | &#8226; [Canada Social Identification Number (**preview**)](entity-categories.md#type-canada-social-identification-number-preview) | &#8226; [Chile Identity Card Number](entity-categories.md#type-chile-identity-card-number) |
+| &#8226; [China Resident Identity Card Number](entity-categories.md#type-china-resident-identity-card-number) | &#8226; [City (**preview**)](entity-categories.md#type-city-preview) | &#8226; [Credit Card Number](entity-categories.md#type-credit-card-number) |
+| &#8226; [Croatia Identity Card Number](entity-categories.md#type-croatia-identity-card-number) | &#8226; [City (**preview**)](entity-categories.md#type-city-preview) | &#8226; [Croatia National ID Number](entity-categories.md#type-croatia-national-id-number) |
+| &#8226; [Croatia Personal Identification Number](entity-categories.md#type-croatia-personal-identification-number) | &#8226; [CVV (**preview**)](entity-categories.md#type-card-verification-value-cvv-preview) | &#8226; [Cyprus Identity Card](entity-categories.md#type-cyprus-identity-card) |
+| &#8226; [Cyprus Tax Identification Number](entity-categories.md#type-cyprus-tax-identification-number) | &#8226; [Date](entity-categories.md#type-date) | &#8226; [Date Of Birth (**preview**)](entity-categories.md#type-date-of-birth-preview) |
+| &#8226; [Denmark Personal Identification Number](entity-categories.md#type-denmark-personal-identification-number) | &#8226; [Drivers License Number (**preview**)](entity-categories.md#type-drivers-license-number-preview) | &#8226; [Email](entity-categories.md#type-email) | 
+| &#8226; [Estonia Personal Identification Code](entity-categories.md#type-estonia-personal-identification-code) | &#8226; [European Union Debit Card Number](entity-categories.md#type-european-union-debit-card-number) | &#8226; [European Union Drivers License Number](entity-categories.md#type-european-union-drivers-license-number) |
+| &#8226; [European Union GPS Coordinates](entity-categories.md#type-european-union-gps-coordinates) | &#8226; [European Union National Identification Number](entity-categories.md#type-european-union-national-identification-number) | &#8226; [European Union Passport Number](entity-categories.md#type-european-union-passport-number) |
+| &#8226; [European Union Social Security Number](entity-categories.md#type-european-union-social-security-number) | &#8226; [European Union Tax Identification Number](entity-categories.md#type-european-union-tax-identification-number) | &#8226; [Expiration Date (**preview**)](entity-categories.md#type-expiration-date-preview) |
+| &#8226; [Finland European Health Number](entity-categories.md#type-finland-european-health-number) | &#8226; [Finland National ID](entity-categories.md#type-finland-national-id) | &#8226; [Finland Passport Number](entity-categories.md#type-finland-passport-number) |
+| &#8226; [France Drivers License Number](entity-categories.md#type-france-drivers-license-number) | &#8226; [France National ID](entity-categories.md#type-france-national-id) | &#8226; [France Passport Number](entity-categories.md#type-france-passport-number) |
+| &#8226; [France Social Security Number](entity-categories.md#type-france-social-security-number) | &#8226; [France Tax Identification Number](entity-categories.md#type-france-tax-identification-number) | &#8226; [France Value Added Tax Number](entity-categories.md#type-france-value-added-tax-number) |
+| &#8226; [Germany Drivers License Number](entity-categories.md#type-germany-drivers-license-number) | &#8226; [Germany Identity Card Number](entity-categories.md#type-germany-identity-card-number) | &#8226; [Germany Passport Number](entity-categories.md#type-germany-passport-number) |
+| &#8226; [Germany Tax Identification Number](entity-categories.md#type-germany-tax-identification-number) | &#8226; [Germany Value Added Number](entity-categories.md#type-germany-value-added-number) | &#8226; [GPE (**preview**)](entity-categories.md#type-geopolitical-entity-gpe-preview) |
+| &#8226; [Greece National ID Card](entity-categories.md#type-greece-national-id-card) | &#8226; [Greece Tax Identification Number](entity-categories.md#type-greece-tax-identification-number) | &#8226; [Hong Kong SAR Identity Card Number](entity-categories.md#type-hong-kong-sar-identity-card-number) |
+| &#8226; [Hungary Personal Identification Number](entity-categories.md#type-hungary-personal-identification-number) | &#8226; [Hungary Value Added Number](entity-categories.md#type-hungary-value-added-number) | &#8226; [India Permanent Account](entity-categories.md#type-india-permanent-account) |
+| &#8226; [India Unique Identification Number](entity-categories.md#type-india-unique-identification-number) | &#8226; [Indonesia Identity Card Number](entity-categories.md#type-indonesia-identity-card-number) | &#8226; [International Banking Account Number](entity-categories.md#type-international-banking-account-number) |
+| &#8226; [IP Address](entity-categories.md#type-ip-address) | &#8226; [Ireland Personal Public Service Number](entity-categories.md#type-ireland-personal-public-service-number) | &#8226; [Israel Bank Account Number](entity-categories.md#type-israel-bank-account-number) |
+| &#8226; [Israel National ID](entity-categories.md#type-israel-national-id) | &#8226; [Italy Drivers License Number](entity-categories.md#type-italy-drivers-license-number) | &#8226; [Italy Fiscal Code](entity-categories.md#type-italy-fiscal-code) |
+| &#8226; [Italy Value Added Tax Number](entity-categories.md#type-italy-value-added-tax-number) | &#8226; [Japan Bank Account Number](entity-categories.md#type-japan-bank-account-number) | &#8226; [Japan Drivers License Number](entity-categories.md#type-japan-drivers-license-number) |
+| &#8226; [Japan My Number Corporate](entity-categories.md#type-japan-my-number-corporate) | &#8226; [Japan My Number Personal](entity-categories.md#type-japan-my-number-personal) | &#8226; [Japan Passport Number](entity-categories.md#type-japan-passport-number) |
+| &#8226; [Japan Residence Card Number](entity-categories.md#type-japan-residence-card-number) | &#8226; [Japan Resident Registration Number](entity-categories.md#type-japan-resident-registration-number) | &#8226; [Japan Social Insurance Number](entity-categories.md#type-japan-social-insurance-number) |
+| &#8226; [Latvia Personal Code](entity-categories.md#type-latvia-personal-code) | &#8226; [License Plate (**preview**)](entity-categories.md#type-license-plate-preview) | &#8226; [Lithuania Personal Code](entity-categories.md#type-lithuania-personal-code) |
+| &#8226; [Location (**preview**)](entity-categories.md#type-location-preview) | &#8226; [Luxembourg National Identification Number Natural](entity-categories.md#type-luxembourg-national-identification-number-natural) | &#8226; [Luxembourg National Identification Number Non-Natural](entity-categories.md#type-luxembourg-national-identification-number-non-natural) |
+| &#8226; [Malaysia Identity Card Number](entity-categories.md#type-malaysia-identity-card-number) | &#8226; [Malta Identity Card Number](entity-categories.md#type-malta-identity-card-number) | &#8226; [Malta Tax ID Number](entity-categories.md#type-malta-tax-id-number) |
+| &#8226; [Netherlands Citizens Service Number](entity-categories.md#type-netherlands-citizens-service-number) | &#8226; [Netherlands Tax Identification Number](entity-categories.md#type-netherlands-tax-identification-number) | &#8226; [Netherlands Value Added Tax Number](entity-categories.md#type-netherlands-value-added-tax-number) |
+| &#8226; [New Zealand Bank Account Number](entity-categories.md#type-new-zealand-bank-account-number) | &#8226; [New Zealand Drivers License Number](entity-categories.md#type-new-zealand-drivers-license-number) | &#8226; [New Zealand Inland Revenue Number](entity-categories.md#type-new-zealand-inland-revenue-number) |
+| &#8226; [New Zealand Ministry Of Health Number](entity-categories.md#type-new-zealand-ministry-of-health-number) | &#8226; [New Zealand Social Welfare Number](entity-categories.md#type-new-zealand-social-welfare-number) | &#8226; [Norway Identity Number](entity-categories.md#type-norway-identity-number) |
+| &#8226; [Organization](entity-categories.md#type-organization) | &#8226; [Passport Number (**preview**)](entity-categories.md#type-passport-number-preview) | &#8226; [Password (**preview**)](entity-categories.md#type-password-preview) |
+| &#8226; [Person](entity-categories.md#type-person) | &#8226; [Philippines Unified Multipurpose ID Number](entity-categories.md#type-philippines-unified-multi-purpose-id-number) | &#8226; [Phone Number](entity-categories.md#type-phone-number) |
+| &#8226; [Poland Identity Card](entity-categories.md#type-poland-identity-card) | &#8226; [Poland National ID](entity-categories.md#type-poland-national-id) | &#8226; [Poland Passport Number](entity-categories.md#type-poland-passport-number) |
+| &#8226; [Poland REGON Number](entity-categories.md#type-poland-regon-number) | &#8226; [Poland Tax Identification Number](entity-categories.md#type-poland-tax-identification-number) | &#8226; [Portugal Tax Identification Number](entity-categories.md#type-portugal-tax-identification-number) |
+| &#8226; [Romania Personal Numerical Code](entity-categories.md#type-romania-personal-numerical-code) | &#8226; [Russia Passport Number Domestic](entity-categories.md#type-russia-passport-number-domestic) | &#8226; [Russia Passport Number International](entity-categories.md#type-russia-passport-number-international) |
+| &#8226; [Saudi Arabia National ID](entity-categories.md#type-saudi-arabia-national-id) | &#8226; [Singapore National Registration Identity Card Number](entity-categories.md#type-singapore-national-registration-identity-card-number) | &#8226; [Slovakia Personal Number](entity-categories.md#type-slovakia-personal-number) |
+| &#8226; [Slovenia Tax Identification Number](entity-categories.md#type-slovenia-tax-identification-number) | &#8226; [Slovenia Unique Master Citizen Number](entity-categories.md#type-slovenia-unique-master-citizen-number) | &#8226; [Sort Code (**preview**)](entity-categories.md#type-sort-code-preview) |
+| &#8226; [South Africa Identification Number](entity-categories.md#type-south-africa-identification-number) | &#8226; [South Korea Drivers License Number (**preview**)](entity-categories.md#type-south-korea-drivers-license-number-preview) | &#8226; [South Korea Passport Number (**preview**)](entity-categories.md#type-south-korea-passport-number-preview) |
+| &#8226; [South Korea Resident Registration Number](entity-categories.md#type-south-korea-resident-registration-number) | &#8226; [South Korea Social Security Number (**preview**)](entity-categories.md#type-south-korea-social-security-number-preview) | &#8226; [Spain DNI](entity-categories.md#type-spain-dni) |
+| &#8226; [Spain Social Security Number](entity-categories.md#type-spain-social-security-number) | &#8226; [Spain Tax Identification Number](entity-categories.md#type-spain-tax-identification-number) | &#8226; [SQL Server Connection String](entity-categories.md#type-sql-server-connection-string) |
+| &#8226; [State (**preview**)](entity-categories.md#type-state-preview) | &#8226; [Sweden National ID](entity-categories.md#type-sweden-national-id) | &#8226; [Sweden Passport Number](entity-categories.md#type-sweden-passport-number) |
+| &#8226; [Sweden Tax Identification Number](entity-categories.md#type-sweden-tax-identification-number) | &#8226; [SWIFT Code](entity-categories.md#type-swift-code) | &#8226; [Taiwanese ID](entity-categories.md#type-taiwanese-id) |
+| &#8226; [Taiwan Passport Number](entity-categories.md#type-taiwan-passport-number) | &#8226; [Taiwan Resident Certificate](entity-categories.md#type-taiwan-resident-certificate) | &#8226; [Thailand Population Identification Code](entity-categories.md#type-thailand-population-identification-code) |
+| &#8226; [Türkiye National Identification Number](entity-categories.md#type-türkiye-national-identification-number) | &#8226; [Ukraine Passport Number Domestic](entity-categories.md#type-ukraine-passport-number-domestic) | &#8226; [Ukraine Passport Number International](entity-categories.md#type-ukraine-passport-number-international) |
+| &#8226; [United Kingdom Drivers License Number](entity-categories.md#type-united-kingdom-drivers-license-number) | &#8226; [United Kingdom Electoral Roll Number](entity-categories.md#type-united-kingdom-electoral-roll-number) | &#8226; [United Kingdom National Health Number](entity-categories.md#type-united-kingdom-national-health-number) |
+| &#8226; [United Kingdom National Insurance Number](entity-categories.md#type-united-kingdom-national-insurance-number) | &#8226; [United Kingdom Unique Taxpayer Number](entity-categories.md#type-united-kingdom-unique-taxpayer-number) | &#8226; [United States Bank Account Number](entity-categories.md#type-united-states-bank-account-number) |
+| &#8226; [United States Drivers License Number](entity-categories.md#type-united-states-drivers-license-number) | &#8226; [United States Drug Enforcement Agency Number](entity-categories.md#type-united-states-drug-enforcement-agency-number) | &#8226; [United States Individual Taxpayer Identification](entity-categories.md#type-united-states-individual-taxpayer-identification) |
+| &#8226; [United States Medicare Beneficiary ID (**preview**)](entity-categories.md#type-united-states-medicare-beneficiary-identification-preview) | &#8226; [United States Social Security Number](entity-categories.md#type-united-states-social-security-number) | &#8226; [United States/United Kingdom Passport Number](entity-categories.md#type-united-statesunited-kingdom-passport-number) |
+| &#8226; [URL](entity-categories.md#type-url) | &#8226; [VIN (**preview**)](entity-categories.md#type-vin-preview) | &#8226; [ZipCode (**preview**)](entity-categories.md#type-zipcode-preview) |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PIIエンティティカテゴリリストの更新"
}
```

### Explanation
この変更は、会話型個人情報（PII）エンティティのリストを含むドキュメントの内容を更新したものです。具体的には、エンティティ名の修正、注釈の追加、そして新しいエンティティのサポートを含むリストの更新が行われました。

- ドキュメントのタイトルが「認識されたPIIエンティティリスト」から「認識されたテキストPIIエンティティリスト」に変更され、コンテンツの焦点が明確になりました。
- エンティティの情報が整形され、表の形式で見やすく整理されています。また、エンティティの種類に「プレビュー」タグが追加されることで、どのエンティティがまだ開発中であるかを示しています。
- 新たに追加されたエンティティカテゴリには、「空港」や「市」などのジャンルが含まれ、さらなる情報を得やすくなっています。
- それぞれのエンティティリンクが強調表示され、ユーザーが特定の情報にアクセスしやすくなりました。

この更新によって、Azureの会話型PII検出機能を利用する開発者やユーザーが、個人情報の識別と扱いについての理解を深める手助けができることを目的としています。全体として、情報がより明確に構造化され、利便性が向上しています。

## articles/ai-services/language-service/personally-identifiable-information/concepts/entity-categories.md{#item-ba2623}

<details>
<summary>Diff</summary>
````diff
@@ -75,32 +75,32 @@ Data that details an individual's physical location that can be used to pinpoint
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **Airport** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payloads. |[Airport]|
+|To retrieve this entity type, specify **Airport** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payloads.|[**Airport**]|
 
 ### Type: City (preview)
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **City** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payloads. |[City]|
+|To retrieve this entity type, specify **City** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payloads.|[**City**]|
 
 ### Type: Geopolitical Entity GPE (preview)
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **GPE** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payloads. |[GPE]|
+|To retrieve this entity type, specify **GPE** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payloads.|[**GPE**]|
 
 ### Type: Location (preview)
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **Location** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payloads. |[Location]|
+|To retrieve this entity type, specify **Location** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payloads.|[**Location**]|
 
 
 ### Type: State (preview)
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **State** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payloads. |[State]|
+|To retrieve this entity type, specify **State** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payloads.|[**State**]|
 
 
 ## Personal
@@ -111,80 +111,80 @@ Any data, collected or stored, that can be used to identify or contact a specifi
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **Address** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** and **PHI** response payloads. |[Address]|
+|To retrieve this entity type, specify **Address** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** and **PHI** response payloads.|[**Address**]|
 
 ### Type: Age
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **Age** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[Age]|
+|To retrieve this entity type, specify **Age** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**Age**]|
 
 ### Type: Date Of Birth (preview)
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **DateOfBirth** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[DateOfBirth]|
+|To retrieve this entity type, specify **DateOfBirth** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**DateOfBirth**]|
 
 ### Type: Drivers License Number (preview)
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **DriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[DriversLicenseNumber]|
+|To retrieve this entity type, specify **DriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**DriversLicenseNumber**]|
 
 ### Type: Email
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **Email** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** and **PHI** response payloads.|[Email]|
+|To retrieve this entity type, specify **Email** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** and **PHI** response payloads.|[**Email**]|
 
 ### Type: IP Address
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **IPAddress** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** and **PHI** response payloads.|[IPAddress]|
+|To retrieve this entity type, specify **IPAddress** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** and **PHI** response payloads.|[**IPAddress**]|
 
 ### Type: License Plate (preview)
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **LicensePlate** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[LicensePlate]|
+|To retrieve this entity type, specify **LicensePlate** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**LicensePlate**]|
 
 ### Type: Passport Number (preview)
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **PassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[PassportNumber]|
+|To retrieve this entity type, specify **PassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**PassportNumber**]|
 
 ### Type: Password (preview)
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **Password** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[Password]|
+|To retrieve this entity type, specify **Password** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**Password**]|
 
 
 ### Type: Person
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **Person** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payloads.|[Person]|
+|To retrieve this entity type, specify **Person** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payloads.|[**Person**]|
 
 ### Type: Phone Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **PhoneNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** and **PHI** response payloads.|[PhoneNumber]|
+|To retrieve this entity type, specify **PhoneNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** and **PHI** response payloads.|[**PhoneNumber**]|
 
 ### Type: URL
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **URL** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** and **PHI** response payloads.|[URL]|
+|To retrieve this entity type, specify **URL** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** and **PHI** response payloads.|[**URL**]|
 
 ### Type: VIN (preview)
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **VIN** (vehicle registration number) in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[VIN]|
+|To retrieve this entity type, specify **VIN** (vehicle registration number) in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**VIN**]|
 
 ## Financial
 
@@ -195,37 +195,37 @@ Any financial information is connected to a particular individual that can, thro
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **ABARoutingNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[ABARoutingNumber]|
+|To retrieve this entity type, specify **ABARoutingNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**ABARoutingNumber**]|
 
 ### Type: Bank Account Number (preview) 
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **BankAccountNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[BankAccountNumber]|
+|To retrieve this entity type, specify **BankAccountNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**BankAccountNumber**]|
 
 ### Type: Credit Card Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **CreditCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[CreditCardNumber]|
+|To retrieve this entity type, specify **CreditCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**CreditCardNumber**]|
 
 ### Type: International Banking Account Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **InternationalBankingAccountNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[InternationalBankingAccountNumber]|
+|To retrieve this entity type, specify **InternationalBankingAccountNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**InternationalBankingAccountNumber**]|
 
 ### Type: Sort Code (preview)
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **SortCode** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[SortCode]|
+|To retrieve this entity type, specify **SortCode** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**SortCode**]|
 
 ### Type: SWIFT Code
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **SWIFTCode** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[SWIFTCode]|
+|To retrieve this entity type, specify **SWIFTCode** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**SWIFTCode**]|
 
 ## Organization
 
@@ -235,7 +235,7 @@ Any data that an organization collects, stores, or processes that can be used to
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **Organization** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** and **PHI** response payloads.|[Organization]|
+|To retrieve this entity type, specify **Organization** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** and **PHI** response payloads.|[**Organization**]|
 
 ## DateTime
 
@@ -245,13 +245,13 @@ Any data that an organization collects, stores, or processes that can be used to
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **Date** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** and **PHI** response payloads.|[Date]|
+|To retrieve this entity type, specify **Date** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** and **PHI** response payloads.|[**Date**]|
 
 ### Type: Expiration Date (preview)
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **ExpirationDate** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payloads.|[ExpirationDate]|
+|To retrieve this entity type, specify **ExpirationDate** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payloads.|[**ExpirationDate**]|
 
 ## Azure-related
 
@@ -261,61 +261,61 @@ Any identifiable Azure information like authentication information and connectio
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **AzureDocumentDBAuthKey** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[AzureDocumentDBAuthKey]|
+|To retrieve this entity type, specify **AzureDocumentDBAuthKey** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**AzureDocumentDBAuthKey**]|
 
 ### Type: Azure IAAS Database Connection And SQL String
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **AzureIAASDatabaseConnectionAndSQLString** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[AzureIAASDatabaseConnectionAndSQLString]|
+|To retrieve this entity type, specify **AzureIAASDatabaseConnectionAndSQLString** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**AzureIAASDatabaseConnectionAndSQLString**]|
 
 ### Type: Azure IoT Connection String
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **AzureIoTConnectionString** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[AzureIoTConnectionString]|
+|To retrieve this entity type, specify **AzureIoTConnectionString** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**AzureIoTConnectionString**]|
 
 ### Type: Azure Publish Setting Password
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **AzurePublishSettingPassword** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[AzurePublishSettingPassword]|
+|To retrieve this entity type, specify **AzurePublishSettingPassword** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**AzurePublishSettingPassword**]|
 
 ### Type: Azure Redis Cache String
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **AzureRedisCacheString** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[AzureRedisCacheString]|
+|To retrieve this entity type, specify **AzureRedisCacheString** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**AzureRedisCacheString**]|
 
 ### Type: Azure SAS
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **AzureSAS** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[AzureSAS]|
+|To retrieve this entity type, specify **AzureSAS** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**AzureSAS**]|
 
 ### Type: Azure Service Bus String
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **AzureServiceBusString** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[AzureServiceBusString]|
+|To retrieve this entity type, specify **AzureServiceBusString** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**AzureServiceBusString**]|
 
 ### Type: Azure Storage Account Generic
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **AzureStorageAccountGeneric** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[AzureStorageAccountGeneric]|
+|To retrieve this entity type, specify **AzureStorageAccountGeneric** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**AzureStorageAccountGeneric**]|
 
 ### Type: Azure Storage Account Key
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **AzureStorageAccountKey** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[AzureStorageAccountKey]|
+|To retrieve this entity type, specify **AzureStorageAccountKey** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**AzureStorageAccountKey**]|
 
 ### Type: SQL Server Connection String
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **SQLServerConnectionString** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[AzureStorageAccountKey]|
+|To retrieve this entity type, specify **SQLServerConnectionString** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**AzureStorageAccountKey**]|
 
 
 ## Government
@@ -326,843 +326,843 @@ Any government-issued identification that can be used along or combined with oth
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **ARNationalIdentityNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[ARNationalIdentityNumber]|
+|To retrieve this entity type, specify **ARNationalIdentityNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**ARNationalIdentityNumber**]|
 
 ### Type: Australia Bank Account Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **AUBankAccountNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[AUBankAccountNumber]|
+|To retrieve this entity type, specify **AUBankAccountNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**AUBankAccountNumber**]|
 
 ### Type: Australia Business Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **AUBusinessNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[AUBusinessNumber]|
+|To retrieve this entity type, specify **AUBusinessNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**AUBusinessNumber**]|
 
 ### Type: Australia Company Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **AUCompanyNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[AUCompanyNumber]|
+|To retrieve this entity type, specify **AUCompanyNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**AUCompanyNumber**]|
 
 ### Type: Australia Drivers License Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **AUDriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[AUDriversLicenseNumber]|
+|To retrieve this entity type, specify **AUDriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**AUDriversLicenseNumber**]|
 
 ### Type: Australia Medical Account Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **AUMedicalAccountNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[AUMedicalAccountNumber]|
+|To retrieve this entity type, specify **AUMedicalAccountNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**AUMedicalAccountNumber**]|
 
 ### Type: Australia Passport Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **AUPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[AUPassportNumber]|
+|To retrieve this entity type, specify **AUPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**AUPassportNumber**]|
 
 ### Type: Australia Tax File Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **AUTaxFileNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[AUTaxFileNumber]|
+|To retrieve this entity type, specify **AUTaxFileNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**AUTaxFileNumber**]|
 
 ### Type: Austria Identity Card
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **ATIdentityCard** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[ATIdentityCard]|
+|To retrieve this entity type, specify **ATIdentityCard** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**ATIdentityCard**]|
 
 ### Type: Austria Tax Identification Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **ATTaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[ATTaxIdentificationNumber]|
+|To retrieve this entity type, specify **ATTaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**ATTaxIdentificationNumber**]|
 
 ### Type: Austria Value Added Tax Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **ATValueAddedTaxNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[ATValueAddedTaxNumber]|
+|To retrieve this entity type, specify **ATValueAddedTaxNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**ATValueAddedTaxNumber**]|
 
 ### Type: Belgium National Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **BENationalNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[BENationalNumber]|
+|To retrieve this entity type, specify **BENationalNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**BENationalNumber**]|
 
 ### Type: Belgium Value Added Tax Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **BEValueAddedTaxNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[BEValueAddedTaxNumber]|
+|To retrieve this entity type, specify **BEValueAddedTaxNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**BEValueAddedTaxNumber**]|
 
 
 ### Type: Brazil CPF Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **BRCPFNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[BRCPFNumber]|
+|To retrieve this entity type, specify **BRCPFNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**BRCPFNumber**]|
 
 ### Type: Brazil Legal Entity Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **BRLegalEntityNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[BRLegalEntityNumber]|
+|To retrieve this entity type, specify **BRLegalEntityNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**BRLegalEntityNumber**]|
 
 ### Type: Brazil National IDRG
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **BRNationalIDRG** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[BRNationalIDRG]|
+|To retrieve this entity type, specify **BRNationalIDRG** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**BRNationalIDRG**]|
 
 ### Type: Bulgaria Uniform Civil Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **BGUniformCivilNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[BGUniformCivilNumber]|
+|To retrieve this entity type, specify **BGUniformCivilNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**BGUniformCivilNumber**]|
 
 ### Type: Canada Bank Account Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **CABankAccountNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[CABankAccountNumber]|
+|To retrieve this entity type, specify **CABankAccountNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**CABankAccountNumber**]|
 
 ### Type: Canada Drivers License Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **CADriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[CADriversLicenseNumber]|
+|To retrieve this entity type, specify **CADriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**CADriversLicenseNumber**]|
 
 ### Type: Canada Health Service Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **CAHealthServiceNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[CAHealthServiceNumber]|
+|To retrieve this entity type, specify **CAHealthServiceNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**CAHealthServiceNumber**]|
 
 ### Type: Canada Passport Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **CAPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[CAPassportNumber]|
+|To retrieve this entity type, specify **CAPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**CAPassportNumber**]|
 
 ### Type: Canada Personal Health Identification
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **CAPersonalHealthIdentification** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** and **PHI** response payload.|[CAPersonalHealthIdentification]|
+|To retrieve this entity type, specify **CAPersonalHealthIdentification** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** and **PHI** response payload.|[**CAPersonalHealthIdentification**]|
 
 ### Type: Canada Social Identification Number (preview)
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **CASocialIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[CASocialIdentificationNumber]|
+|To retrieve this entity type, specify **CASocialIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**CASocialIdentificationNumber**]|
 
 
 ### Type: Canada Social Insurance Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **CASocialInsuranceNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[CASocialInsuranceNumber]|
+|To retrieve this entity type, specify **CASocialInsuranceNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**CASocialInsuranceNumber**]|
 
 ### Type: Card Verification Value CVV (preview)
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **CVV** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[CVV]|
+|To retrieve this entity type, specify **CVV** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**CVV**]|
 
 
 ### Type: Chile Identity Card Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **CLIdentityCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[CLIdentityCardNumber]|
+|To retrieve this entity type, specify **CLIdentityCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**CLIdentityCardNumber**]|
 
 ### Type: China Resident Identity Card Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **CNResidentIdentityCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[CNResidentIdentityCardNumber]|
+|To retrieve this entity type, specify **CNResidentIdentityCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**CNResidentIdentityCardNumber**]|
 
 ### Type: Croatia Identity Card Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **HRIdentityCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[HRIdentityCardNumber]|
+|To retrieve this entity type, specify **HRIdentityCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**HRIdentityCardNumber**]|
 
 ### Type: Croatia National ID Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **HRNationalIDNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[HRNationalIDNumber]|
+|To retrieve this entity type, specify **HRNationalIDNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**HRNationalIDNumber**]|
 
 ### Type: Croatia Personal Identification Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **HRPersonalIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[HRPersonalIdentificationNumber]|
+|To retrieve this entity type, specify **HRPersonalIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**HRPersonalIdentificationNumber**]|
 
 ### Type: Cyprus Identity Card
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **CYIdentityCard** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[CYIdentityCard]|
+|To retrieve this entity type, specify **CYIdentityCard** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**CYIdentityCard**]|
 
 ### Type: Cyprus Tax Identification Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **CYTaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[CYTaxIdentificationNumber]|
+|To retrieve this entity type, specify **CYTaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**CYTaxIdentificationNumber**]|
 
 ### Type: Czech Republic Personal Identity Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **CZPersonalIdentityNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[CZPersonalIdentityNumber]|
+|To retrieve this entity type, specify **CZPersonalIdentityNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**CZPersonalIdentityNumber**]|
 
 ### Type: Denmark Personal Identification Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **DKPersonalIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[DKPersonalIdentificationNumber]|
+|To retrieve this entity type, specify **DKPersonalIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**DKPersonalIdentificationNumber**]|
 
 ### Type: Estonia Personal Identification Code
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **EEPersonalIdentificationCode** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[EEPersonalIdentificationCode]|
+|To retrieve this entity type, specify **EEPersonalIdentificationCode** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**EEPersonalIdentificationCode**]|
 
 ### Type: European Union Debit Card Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **EUDebitCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[EUDebitCardNumber]|
+|To retrieve this entity type, specify **EUDebitCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**EUDebitCardNumber**]|
 
 ### Type: European Union Drivers License Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **EUDriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[EUDriversLicenseNumber]|
+|To retrieve this entity type, specify **EUDriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**EUDriversLicenseNumber**]|
 
 ### Type: European Union GPS Coordinates
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **EUGPSCoordinates** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[EUGPSCoordinates]|
+|To retrieve this entity type, specify **EUGPSCoordinates** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**EUGPSCoordinates**]|
 
 ### Type: European Union National Identification Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **EUNationalIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[EUNationalIdentificationNumber]|
+|To retrieve this entity type, specify **EUNationalIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**EUNationalIdentificationNumber**]|
 
 ### Type: European Union Passport Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **EUPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[EUPassportNumber]|
+|To retrieve this entity type, specify **EUPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**EUPassportNumber**]|
 
 ### Type: European Union Social Security Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **EUSocialSecurityNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[EUSocialSecurityNumber]|
+|To retrieve this entity type, specify **EUSocialSecurityNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**EUSocialSecurityNumber**]|
 
 ### Type: European Union Tax Identification Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **EUTaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[EUTaxIdentificationNumber]|
+|To retrieve this entity type, specify **EUTaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**EUTaxIdentificationNumber**]|
 
 ### Type: Expiration Date (preview)
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **ExpirationDate** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[ExpirationDate]|
+|To retrieve this entity type, specify **ExpirationDate** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**ExpirationDate**]|
 
 
 
 ### Type: Finland European Health Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **FIEuropeanHealthNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[FIEuropeanHealthNumber]|
+|To retrieve this entity type, specify **FIEuropeanHealthNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**FIEuropeanHealthNumber**]|
 
 ### Type: Finland National ID
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **FINationalID** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[FINationalID]|
+|To retrieve this entity type, specify **FINationalID** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**FINationalID**]|
 
 ### Type: Finland Passport Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **FIPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[FIPassportNumber]|
+|To retrieve this entity type, specify **FIPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**FIPassportNumber**]|
 
 ### Type: France Drivers License Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **FRDriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[FRDriversLicenseNumber]|
+|To retrieve this entity type, specify **FRDriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**FRDriversLicenseNumber**]|
 
 ### Type: France Health Insurance Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **FRHealthInsuranceNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[FRHealthInsuranceNumber]|
+|To retrieve this entity type, specify **FRHealthInsuranceNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**FRHealthInsuranceNumber**]|
 
 ### Type: France National ID
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **FRNationalID** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[FRNationalID]|
+|To retrieve this entity type, specify **FRNationalID** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**FRNationalID**]|
 
 ### Type: France Passport Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **FRPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[FRPassportNumber]|
+|To retrieve this entity type, specify **FRPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**FRPassportNumber**]|
 
 ### Type: France Social Security Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **FRSocialSecurityNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[FRSocialSecurityNumber]|
+|To retrieve this entity type, specify **FRSocialSecurityNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**FRSocialSecurityNumber**]|
 
 ### Type: France Tax Identification Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **FRTaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[FRTaxIdentificationNumber]|
+|To retrieve this entity type, specify **FRTaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**FRTaxIdentificationNumber**]|
 
 ### Type: France Value Added Tax Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **FRValueAddedTaxNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[FRValueAddedTaxNumber]|
+|To retrieve this entity type, specify **FRValueAddedTaxNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**FRValueAddedTaxNumber**]|
 
 ### Type: Germany Drivers License Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **DEDriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[DEDriversLicenseNumber]|
+|To retrieve this entity type, specify **DEDriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**DEDriversLicenseNumber**]|
 
 ### Type: Germany Identity Card Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **DEIdentityCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[DEIdentityCardNumber]|
+|To retrieve this entity type, specify **DEIdentityCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**DEIdentityCardNumber**]|
 
 ### Type: Germany Passport Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **DEPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[DEPassportNumber]|
+|To retrieve this entity type, specify **DEPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**DEPassportNumber**]|
 
 ### Type: Germany Tax Identification Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **DETaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[DETaxIdentificationNumber]|
+|To retrieve this entity type, specify **DETaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**DETaxIdentificationNumber**]|
 
 ### Type: Germany Value Added Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **DEValueAddedNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[DEValueAddedNumber]|
+|To retrieve this entity type, specify **DEValueAddedNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**DEValueAddedNumber**]|
 
 ### Type: Greece National ID Card
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **GRNationalIDCard** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[GRNationalIDCard]|
+|To retrieve this entity type, specify **GRNationalIDCard** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**GRNationalIDCard**]|
 
 ### Type: Greece Tax Identification Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **GRTaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[GRTaxIdentificationNumber]|
+|To retrieve this entity type, specify **GRTaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**GRTaxIdentificationNumber**]|
 
 ### Type: Hong Kong SAR Identity Card Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **HKIdentityCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[HKIdentityCardNumber]|
+|To retrieve this entity type, specify **HKIdentityCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**HKIdentityCardNumber**]|
 
 ### Type: Hungary Personal Identification Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **HUPersonalIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[HUPersonalIdentificationNumber]|
+|To retrieve this entity type, specify **HUPersonalIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**HUPersonalIdentificationNumber**]|
 
 ### Type: Hungary Tax Identification Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **HUTaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[HUTaxIdentificationNumber]|
+|To retrieve this entity type, specify **HUTaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**HUTaxIdentificationNumber**]|
 
 ### Type: Hungary Value Added Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **HUValueAddedNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[HUValueAddedNumber]|
+|To retrieve this entity type, specify **HUValueAddedNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**HUValueAddedNumber**]|
 
 ### Type: India Permanent Account
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **INPermanentAccount** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[INPermanentAccount]|
+|To retrieve this entity type, specify **INPermanentAccount** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**INPermanentAccount**]|
 
 ### Type: India Unique Identification Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **INUniqueIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[INUniqueIdentificationNumber]|
+|To retrieve this entity type, specify **INUniqueIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**INUniqueIdentificationNumber**]|
 
 ### Type: Indonesia Identity Card Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **IDIdentityCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[IDIdentityCardNumber]|
+|To retrieve this entity type, specify **IDIdentityCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**IDIdentityCardNumber**]|
 
 ### Type: Ireland Personal Public Service Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **IEPersonalPublicServiceNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[IEPersonalPublicServiceNumber]|
+|To retrieve this entity type, specify **IEPersonalPublicServiceNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**IEPersonalPublicServiceNumber**]|
 
 ### Type: Israel Bank Account Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **ILBankAccountNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[ILBankAccountNumber]|
+|To retrieve this entity type, specify **ILBankAccountNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**ILBankAccountNumber**]|
 
 ### Type: Israel National ID
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **ILNationalID** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[ILNationalID]|
+|To retrieve this entity type, specify **ILNationalID** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**ILNationalID**]|
 
 ### Type: Italy Drivers License Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **ITDriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[ITDriversLicenseNumber]|
+|To retrieve this entity type, specify **ITDriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**ITDriversLicenseNumber**]|
 
 ### Type: Italy Fiscal Code
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **ITFiscalCode** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[ITFiscalCode]|
+|To retrieve this entity type, specify **ITFiscalCode** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**ITFiscalCode**]|
 
 ### Type: Italy Value Added Tax Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **ITValueAddedTaxNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[ITValueAddedTaxNumber]|
+|To retrieve this entity type, specify **ITValueAddedTaxNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**ITValueAddedTaxNumber**]|
 
 ### Type: Japan Bank Account Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **JPBankAccountNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[JPBankAccountNumber]|
+|To retrieve this entity type, specify **JPBankAccountNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**JPBankAccountNumber**]|
 
 ### Type: Japan Drivers License Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **JPDriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[JPDriversLicenseNumber]|
+|To retrieve this entity type, specify **JPDriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**JPDriversLicenseNumber**]|
 
 ### Type: Japan My Number Corporate
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **JPMyNumberCorporate** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[JPMyNumberCorporate]|
+|To retrieve this entity type, specify **JPMyNumberCorporate** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**JPMyNumberCorporate**]|
 
 ### Type: Japan My Number Personal
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **JPMyNumberPersonal** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[JPMyNumberPersonal]|
+|To retrieve this entity type, specify **JPMyNumberPersonal** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**JPMyNumberPersonal**]|
 
 ### Type: Japan Passport Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **JPPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[JPPassportNumber]|
+|To retrieve this entity type, specify **JPPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**JPPassportNumber**]|
 
 ### Type: Japan Residence Card Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **JPResidenceCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[JPResidenceCardNumber]|
+|To retrieve this entity type, specify **JPResidenceCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**JPResidenceCardNumber**]|
 
 ### Type: Japan Resident Registration Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **JPResidentRegistrationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[JPResidentRegistrationNumber]|
+|To retrieve this entity type, specify **JPResidentRegistrationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**JPResidentRegistrationNumber**]|
 
 ### Type: Japan Social Insurance Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **JPSocialInsuranceNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[JPSocialInsuranceNumber]|
+|To retrieve this entity type, specify **JPSocialInsuranceNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**JPSocialInsuranceNumber**]|
 
 ### Type: Latvia Personal Code
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **LVPersonalCode** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[LVPersonalCode]|
+|To retrieve this entity type, specify **LVPersonalCode** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**LVPersonalCode**]|
 
 ### Type: Lithuania Personal Code
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **LTPersonalCode** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[LTPersonalCode]|
+|To retrieve this entity type, specify **LTPersonalCode** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**LTPersonalCode**]|
 
 ### Type: Luxembourg National Identification Number Natural
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **LUNationalIdentificationNumberNatural** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[LUNationalIdentificationNumberNatural]|
+|To retrieve this entity type, specify **LUNationalIdentificationNumberNatural** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**LUNationalIdentificationNumberNatural**]|
 
 ### Type: Luxembourg National Identification Number Non Natural
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **LUNationalIdentificationNumberNonNatural** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[LUNationalIdentificationNumberNonNatural]|
+|To retrieve this entity type, specify **LUNationalIdentificationNumberNonNatural** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**LUNationalIdentificationNumberNonNatural**]|
 
 ### Type: Malaysia Identity Card Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **MYIdentityCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[MYIdentityCardNumber]|
+|To retrieve this entity type, specify **MYIdentityCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**MYIdentityCardNumber**]|
 
 
 ### Type: Malta Identity Card Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **MTIdentityCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[MTIdentityCardNumber]|
+|To retrieve this entity type, specify **MTIdentityCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**MTIdentityCardNumber**]|
 
 ### Type: Malta Tax ID Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **MTTaxIDNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[MTTaxIDNumber]|
+|To retrieve this entity type, specify **MTTaxIDNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**MTTaxIDNumber**]|
 
 ### Type: Netherlands Citizens Service Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **NLCitizensServiceNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[NLCitizensServiceNumber]|
+|To retrieve this entity type, specify **NLCitizensServiceNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**NLCitizensServiceNumber**]|
 
 ### Type: Netherlands Tax Identification Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **NLTaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[NLTaxIdentificationNumber]|
+|To retrieve this entity type, specify **NLTaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**NLTaxIdentificationNumber**]|
 
 ### Type: Netherlands Value Added Tax Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **NLValueAddedTaxNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[NLValueAddedTaxNumber]|
+|To retrieve this entity type, specify **NLValueAddedTaxNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**NLValueAddedTaxNumber**]|
 
 ### Type: New Zealand Bank Account Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **NZBankAccountNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[NZBankAccountNumber]|
+|To retrieve this entity type, specify **NZBankAccountNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**NZBankAccountNumber**]|
 
 ### Type: New Zealand Drivers License Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **NZDriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[NZDriversLicenseNumber]|
+|To retrieve this entity type, specify **NZDriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**NZDriversLicenseNumber**]|
 
 ### Type: New Zealand Inland Revenue Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **NZInlandRevenueNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[NZInlandRevenueNumber]|
+|To retrieve this entity type, specify **NZInlandRevenueNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**NZInlandRevenueNumber**]|
 
 ### Type: New Zealand Ministry Of Health Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **NZMinistryOfHealthNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[NZMinistryOfHealthNumber]|
+|To retrieve this entity type, specify **NZMinistryOfHealthNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**NZMinistryOfHealthNumber**]|
 
 ### Type: New Zealand Social Welfare Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **NZSocialWelfareNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[NZSocialWelfareNumber]|
+|To retrieve this entity type, specify **NZSocialWelfareNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**NZSocialWelfareNumber**]|
 
 ### Type: Norway Identity Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **NOIdentityNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[NOIdentityNumber]|
+|To retrieve this entity type, specify **NOIdentityNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**NOIdentityNumber**]|
 
 
 ### Type: Philippines Unified Multi Purpose ID Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **PHUnifiedMultiPurposeIDNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[PHUnifiedMultiPurposeIDNumber]|
+|To retrieve this entity type, specify **PHUnifiedMultiPurposeIDNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**PHUnifiedMultiPurposeIDNumber**]|
 
 ### Type: Poland Identity Card
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **PLIdentityCard** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[PLIdentityCard]|
+|To retrieve this entity type, specify **PLIdentityCard** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**PLIdentityCard**]|
 
 ### Type: Poland National ID
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **PLNationalID** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[PLNationalID]|
+|To retrieve this entity type, specify **PLNationalID** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**PLNationalID**]|
 
 ### Type: Poland Passport Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **PLPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[PLPassportNumber]|
+|To retrieve this entity type, specify **PLPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**PLPassportNumber**]|
 
 ### Type: Poland REGON Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **PLREGONNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[PLREGONNumber]|
+|To retrieve this entity type, specify **PLREGONNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**PLREGONNumber**]|
 
 ### Type: Poland Tax Identification Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **PLTaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[PLTaxIdentificationNumber]|
+|To retrieve this entity type, specify **PLTaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**PLTaxIdentificationNumber**]|
 
 ### Type: Portugal Citizen Card Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **PTCitizenCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[PTCitizenCardNumber]|
+|To retrieve this entity type, specify **PTCitizenCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**PTCitizenCardNumber**]|
 
 ### Type: Portugal Tax Identification Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **PTTaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[PTTaxIdentificationNumber]|
+|To retrieve this entity type, specify **PTTaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**PTTaxIdentificationNumber**]|
 
 ### Type: Romania Personal Numerical Code
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **ROPersonalNumericalCode** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[ROPersonalNumericalCode]|
+|To retrieve this entity type, specify **ROPersonalNumericalCode** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**ROPersonalNumericalCode**]|
 
 ### Type: Russia Passport Number Domestic
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **RUPassportNumberDomestic** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[RUPassportNumberDomestic]|
+|To retrieve this entity type, specify **RUPassportNumberDomestic** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**RUPassportNumberDomestic**]|
 
 ### Type: Russia Passport Number International
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **RUPassportNumberInternational** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[RUPassportNumberInternational]|
+|To retrieve this entity type, specify **RUPassportNumberInternational** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**RUPassportNumberInternational**]|
 
 ### Type: Saudi Arabia National ID
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **SANationalID** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[SANationalID]|
+|To retrieve this entity type, specify **SANationalID** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**SANationalID**]|
 
 ### Type: Singapore National Registration Identity Card Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **SGNationalRegistrationIdentityCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[SGNationalRegistrationIdentityCardNumber]|
+|To retrieve this entity type, specify **SGNationalRegistrationIdentityCardNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**SGNationalRegistrationIdentityCardNumber**]|
 
 ### Type: Slovakia Personal Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **SKPersonalNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[SKPersonalNumber]|
+|To retrieve this entity type, specify **SKPersonalNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**SKPersonalNumber**]|
 
 ### Type: Slovenia Tax Identification Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **SITaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[SITaxIdentificationNumber]|
+|To retrieve this entity type, specify **SITaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**SITaxIdentificationNumber**]|
 
 ### Type: Slovenia Unique Master Citizen Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **SIUniqueMasterCitizenNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[SIUniqueMasterCitizenNumber]|
+|To retrieve this entity type, specify **SIUniqueMasterCitizenNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**SIUniqueMasterCitizenNumber**]|
 
 ### Type: South Africa Identification Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **ZAIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[ZAIdentificationNumber]|
+|To retrieve this entity type, specify **ZAIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**ZAIdentificationNumber**]|
 
 ### Type: South Korea Drivers License Number (preview)
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **KRDriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[KRDriversLicenseNumber]|
+|To retrieve this entity type, specify **KRDriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**KRDriversLicenseNumber**]|
 
 
 ### Type: South Korea Passport Number (preview)
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **KRPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[KRPassportNumber]|
+|To retrieve this entity type, specify **KRPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**KRPassportNumber**]|
 
 ### Type: South Korea Social Security Number (preview)
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **KRSocialSecurityNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[KRSocialSecurityNumber]|
+|To retrieve this entity type, specify **KRSocialSecurityNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**KRSocialSecurityNumber**]|
 
 ### Type: South Korea Resident Registration Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **KRResidentRegistrationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[KRResidentRegistrationNumber]|
+|To retrieve this entity type, specify **KRResidentRegistrationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**KRResidentRegistrationNumber**]|
 
 ### Type: Spain DNI
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **ESDNI** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[ESDNI]|
+|To retrieve this entity type, specify **ESDNI** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**ESDNI**]|
 
 ### Type: Spain Social Security Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **ESSocialSecurityNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[ESSocialSecurityNumber]|
+|To retrieve this entity type, specify **ESSocialSecurityNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**ESSocialSecurityNumber**]|
 
 ### Type: Spain Tax Identification Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **ESTaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[ESTaxIdentificationNumber]|
+|To retrieve this entity type, specify **ESTaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**ESTaxIdentificationNumber**]|
 
 ### Type: Sweden National ID
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **SENationalID** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[SENationalID]|
+|To retrieve this entity type, specify **SENationalID** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**SENationalID**]|
 
 ### Type: Sweden Passport Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **SEPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[SEPassportNumber, PassportNumber]|
+|To retrieve this entity type, specify **SEPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**SEPassportNumber**, **PassportNumber**]|
 
 ### Type: Sweden Tax Identification Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **SETaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[SETaxIdentificationNumber]|
+|To retrieve this entity type, specify **SETaxIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**SETaxIdentificationNumber**]|
 
 ### Type: Switzerland Social Security Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **CHSocialSecurityNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[CHSocialSecurityNumber]|
+|To retrieve this entity type, specify **CHSocialSecurityNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**CHSocialSecurityNumber**]|
 
 ### Type: Taiwanese ID
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **TWNationalID** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[TWNationalID]|
+|To retrieve this entity type, specify **TWNationalID** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**TWNationalID**]|
 
 ### Type: Taiwan Passport Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **TWPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[TWPassportNumber]|
+|To retrieve this entity type, specify **TWPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**TWPassportNumber**]|
 
 ### Type: Taiwan Resident Certificate
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **TWResidentCertificate** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[TWResidentCertificate]|
+|To retrieve this entity type, specify **TWResidentCertificate** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**TWResidentCertificate**]|
 
 ### Type: Thailand Population Identification Code
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **THPopulationIdentificationCode** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[THPopulationIdentificationCode]|
+|To retrieve this entity type, specify **THPopulationIdentificationCode** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**THPopulationIdentificationCode**]|
 
 ### Type: Türkiye National Identification Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **TRNationalIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[TRNationalIdentificationNumber]|
+|To retrieve this entity type, specify **TRNationalIdentificationNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**TRNationalIdentificationNumber**]|
 
 ### Type: Ukraine Passport Number Domestic
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **UAPassportNumberDomestic** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[UAPassportNumberDomestic]|
+|To retrieve this entity type, specify **UAPassportNumberDomestic** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**UAPassportNumberDomestic**]|
 
 ### Type: Ukraine Passport Number International
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **UAPassportNumberInternational** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[UAPassportNumberInternational]|
+|To retrieve this entity type, specify **UAPassportNumberInternational** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**UAPassportNumberInternational**]|
 
 ### Type: United Kingdom Drivers License Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **UKDriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[UKDriversLicenseNumber]|
+|To retrieve this entity type, specify **UKDriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**UKDriversLicenseNumber**]|
 
 ### Type: United Kingdom Electoral Roll Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **UKElectoralRollNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[UKElectoralRollNumber]|
+|To retrieve this entity type, specify **UKElectoralRollNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**UKElectoralRollNumber**]|
 
 ### Type: United Kingdom National Health Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **UKNationalHealthNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[UKNationalHealthNumber]|
+|To retrieve this entity type, specify **UKNationalHealthNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**UKNationalHealthNumber**]|
 
 ### Type: United Kingdom National Insurance Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **UKNationalInsuranceNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[UKNationalInsuranceNumber]|
+|To retrieve this entity type, specify **UKNationalInsuranceNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**UKNationalInsuranceNumber**]|
 
 ### Type: United Kingdom Unique Taxpayer Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **UKUniqueTaxpayerNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[UKUniqueTaxpayerNumber]|
+|To retrieve this entity type, specify **UKUniqueTaxpayerNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**UKUniqueTaxpayerNumber**]|
 
 ### Type: United States Bank Account Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **USBankAccountNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[USBankAccountNumber]|
+|To retrieve this entity type, specify **USBankAccountNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**USBankAccountNumber**]|
 
 ### Type: United States Drivers License Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **USDriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[USDriversLicenseNumber]|
+|To retrieve this entity type, specify **USDriversLicenseNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**USDriversLicenseNumber**]|
 
 ### Type: United States Drug Enforcement Agency Number
 
@@ -1174,7 +1174,7 @@ Any government-issued identification that can be used along or combined with oth
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **USIndividualTaxpayerIdentification** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[USIndividualTaxpayerIdentification]|
+|To retrieve this entity type, specify **USIndividualTaxpayerIdentification** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**USIndividualTaxpayerIdentification**]|
 
 ### Type: United States Medicare Beneficiary Identification (preview)
 
@@ -1187,19 +1187,19 @@ Any government-issued identification that can be used along or combined with oth
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **USSocialSecurityNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[USSocialSecurityNumber]|
+|To retrieve this entity type, specify **USSocialSecurityNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**USSocialSecurityNumber**]|
 
 ### Type: United States/United Kingdom Passport Number
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **USUKPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[USUKPassportNumber]|
+|To retrieve this entity type, specify **USUKPassportNumber** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**USUKPassportNumber**]|
 
 ### Type: ZipCode (preview)
 
 |Details|Tag|
 |---|---|
-|To retrieve this entity type, specify **ZipCode** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[USUKPassportNumber]|
+|To retrieve this entity type, specify **ZipCode** in the **piiCategories** request parameter. If detected, the entity appears in the **PII** response payload.|[**USUKPassportNumber**]|
 
 
 ## Related content
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンティティカテゴリの表示形式の改善"
}
```

### Explanation
この変更は、個人情報（PII）エンティティカテゴリのドキュメントにおいて、エンティティタイプの表示形式を一貫性を持たせ、視認性を向上させるために行われました。具体的には、各エンティティのタグがマークアップに統一されており、より明瞭にしています。

主な変更点は以下の通りです：
- 各エンティティのテーブルでタグのフォーマットを修正し、視覚的に強調されるように、エンティティ名にアスタリスクが付加されました（例：`[**Airport**]`）。
- 各エンティティタイプの説明文は変更されずに保持され、エンティティの取得方法は一貫性を保たれていますが、見た目が改善されているため、一目で重要な情報が把握しやすくなっています。
- 新たにプレビューされるエンティティタイプも含め、全てのエンティティが同様の形式で表示され、ユーザーが容易に理解できるよう配慮されています。

この変更により、ドキュメントの整合性が高まり、エンティティ情報にアクセスする際のユーザビリティが向上しました。特に、プレビューのエンティティに関する情報は、開発者やユーザーが迅速に必要な文書を見つける際に役立つようになっています。

## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -624,15 +624,20 @@ items:
             href: ../containers/disconnected-containers.md
           - name: Azure AI containers overview
             href: ../cognitive-services-container-support.md
-    - name: Recognized entities
-      items:
-      - name: Entity types for text (extended format)  🆕
-        href: personally-identifiable-information/concepts/entity-categories.md
-      - name: Entities for text (list format) 🆕
-        href: personally-identifiable-information/concepts/entity-categories-list.md
-      - name: Entity categories for conversation
-        href: personally-identifiable-information/concepts/conversations-entity-categories.md
-
+    - name: Recognized entity categories
+      items:
+      - name: PII in text
+        items:
+        - name: Extended format
+          href: personally-identifiable-information/concepts/entity-categories.md
+        - name: List format
+          href: personally-identifiable-information/concepts/entity-categories-list.md
+      - name: PII in conversations
+        items:
+        - name: Extended format
+          href: personally-identifiable-information/concepts/conversations-entity-categories.md
+        - name: List format
+          href: personally-identifiable-information/concepts/conversations-entities-list.md
   - name: Sentiment analysis and opinion mining
     items:
       - name: Overview
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンティティカテゴリの構成の改善"
}
```

### Explanation
この変更は、Azure AIサービスに関するドキュメントの目次（TOC）の構成を改善したものです。具体的には、個人情報（PII）関連のエンティティがより分かりやすく整理され、ユーザーのナビゲーションが向上しました。

主な変更点は次の通りです：
- エンティティカテゴリの名称が「認識されたエンティティ」から「認識されたエンティティカテゴリ」に変更され、明確さが増しました。
- PIIに関するエンティティの構成が再編成され、テキストと会話のそれぞれに対して、拡張フォーマットとリストフォーマットのセクションが個別に作成されました。
- 各セクションには、それぞれ関連するリンクが含まれており、用途に応じた情報へ直接遷移しやすくなっています。例えば、テキスト用のエンティティカテゴリーと会話用のエンティティカテゴリーがそれぞれ独立した項目として配置されています。
  
この変更により、ユーザーが必要な情報をより迅速かつ簡潔に見つけることができるようになり、ドキュメント全体の可読性と利用しやすさが向上しています。


