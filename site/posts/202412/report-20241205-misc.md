---
date: '2024-12-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2c6389f...MicrosoftDocs:04e3114
summary: このコード変更は、主にAzure Language Serviceに関連するMarkdownファイルのサンプルデータや情報を更新する内容です。特に、個人情報検出（PII）機能の新しいプレビューAPIが追加され、敏感情報をラベルでマスクする新オプションが実装されました。破壊的変更はなく、各種リソースID、アプリIDの更新や地域サポート情報の最新化、コンテンツフィルタリングのリファレンスリンクの更新が行われています。この更新は、ドキュメントの正確性と分かりやすさを向上させ、ユーザーに対して最新の情報を提供することを目的としています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2c6389f...MicrosoftDocs:04e3114){target="_blank"}

# ハイライト

このコード変更は、主にAzure Language Serviceに関連する複数のMarkdownファイルにおけるサンプルデータや情報更新を含んでいます。各ファイルにはリソースIDやアプリID、地域サポート情報、リファレンスリンクなどのマイナーな修正が加えられています。特に、個人情報検出（PII）機能の新機能と改善が注目すべきポイントです。

## 新しい機能
- PII検出に新しいプレビューAPIの追加。
- 検出した敏感情報をラベルでマスクする新しいオプション。

## 破壊的変更
- 破壊的変更は特にありません。

## その他の更新
- 各種MarkdownファイルのサンプルリソースIDやアプリIDの更新。
- サマリ機能の地域サポート情報の更新。
- コンテンツフィルタリングリファレンスリンクの更新。

# インサイト

この更新は、Azure Language Serviceおよび関連AIサービスのドキュメントにおける一貫性とユーザーに対する正確な情報提供を目的としています。主にサンプルのリソースIDやアプリIDが更新され、ユーザーにとって理解しやすい最新の情報を反映するための小幅な修正が行われています。

具体的には、古いサブスクリプションIDやアプリIDといった例示が実際の使用状況により即した形で更新され、ユーザーが自分のAzure環境により適応した形でドキュメントを利用できるようにする配慮がされています。また、PII検出に関しては、最新のプレビューAPIによってサービスのカバレッジが拡大し、検出精度が向上したことが示されています。これにより、Azureを利用する企業は、自らが取り扱うデータのプライバシーを一層強化することが可能です。

地域サポートの更新についても、特定の地域を新たにサポートすることで、Azureサービスの利用範囲が拡大し、多様なユーザーが最先端のテクノロジーをより快適に利用できるようになっています。加えて、コンテンツフィルタリングにおける新しいリファレンスリンクの追加により、ユーザーはコンテンツの管理や監視しやすくなり、システムのセキュリティが一段と向上します。

全体として、この更新はドキュメントの正確性とわかりやすさを改善することで、Azure Language Serviceおよび関連AIサービスを利用するユーザーにとっての利便性を高めることに貢献しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [assign-resources.md](#item-34766a) | minor update | リソースIDのサンプル更新 | modified | 1 | 1 | 2 | 
| [unassign-resources.md](#item-46488a) | minor update | リソースIDのサンプル更新 | modified | 1 | 1 | 2 | 
| [assign-resources.md](#item-e0b758) | minor update | リソースIDのサンプル更新 | modified | 1 | 1 | 2 | 
| [unassign-resources.md](#item-e7c3f6) | minor update | リソースIDのサンプル更新 | modified | 1 | 1 | 2 | 
| [import-project.md](#item-c378dd) | minor update | アプリIDのサンプル更新 | modified | 1 | 2 | 3 | 
| [overview.md](#item-8a6932) | minor update | PII検出機能の新機能と改善 | modified | 8 | 3 | 11 | 
| [assign-resources.md](#item-5d6080) | minor update | Azure Resource IDのサンプル変更 | modified | 1 | 1 | 2 | 
| [unassign-resources.md](#item-05bc52) | minor update | AssignリソースIDのサンプル変更 | modified | 1 | 1 | 2 | 
| [region-support.md](#item-d74574) | minor update | 地域サポート情報の更新 | modified | 14 | 14 | 28 | 
| [content-filtering.md](#item-91b372) | minor update | コンテンツフィルタリングのリファレンスリンクの更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/language-service/conversational-language-understanding/includes/rest-api/assign-resources.md{#item-34766a}

<details>
<summary>Diff</summary>
````diff
@@ -51,7 +51,7 @@ Use the following sample JSON as your body.
 
 |Key  |Placeholder  |Value  | Example |
 |---------|---------|----------|--|
-| `azureResourceId` | `{AZURE-RESOURCE-ID}` | The full resource ID path you want to assign. Found in the Azure portal under the **Properties** tab for the resource, within the **Resource ID** field. | `/subscriptions/12345678-0000-0000-0000-0000abcd1234/resourceGroups/ContosoResourceGroup/providers/Microsoft.CognitiveServices/accounts/ContosoResource` |
+| `azureResourceId` | `{AZURE-RESOURCE-ID}` | The full resource ID path you want to assign. Found in the Azure portal under the **Properties** tab for the resource, within the **Resource ID** field. | `/subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/resourceGroups/ContosoResourceGroup/providers/Microsoft.CognitiveServices/accounts/ContosoResource` |
 | `customDomain` | `{CUSTOM-DOMAIN}` | The custom subdomain of the resource you want to assign. Found in the Azure portal under the **Keys and Endpoint** tab for the resource, part of the **Endpoint** field in the URL `https://<your-custom-subdomain>.cognitiveservices.azure.com/` | `contosoresource`  |
 | `region` | `{REGION-CODE}` |  A region code specifying the region of the resource you want to assign. Found in the Azure portal under the **Keys and Endpoint** tab for the resource, as part of the **Location/Region** field. |`eastus`|
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースIDのサンプル更新"
}
```

### Explanation
この変更は、Markdownファイル「assign-resources.md」に対する小さな更新です。具体的には、`azureResourceId`の値を変更しました。旧値では、リソースIDが特定のサブスクリプションID「12345678-0000-0000-0000-0000abcd1234」で指定されていましたが、新しい例では、サブスクリプションIDが「aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e」に更新されています。この変更により、実際のAzureリソース環境における最新の情報を反映したサンプルが提供され、利用者が正しいリソースIDを理解しやすくなります。全体として、この変更はわずかな更新であり、ユーザーに対する有用な情報提供を目的としています。

## articles/ai-services/language-service/conversational-language-understanding/includes/rest-api/unassign-resources.md{#item-46488a}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,7 @@ Use the following sample JSON as your body.
 
 |Key  |Placeholder  |Value  | Example |
 |---------|---------|----------|--|
-| `assignedResourceIds` | `{AZURE-RESOURCE-ID}` | The full resource ID path you want to unassign. Found in the Azure portal under the _Properties_ tab for the resource as the _Resource ID_ field. | `/subscriptions/d73a1925-0000-0000-0000-0000c5fe888e/resourceGroups/ContosoResourceGroup/providers/Microsoft.CognitiveServices/accounts/ContosoResource` |
+| `assignedResourceIds` | `{AZURE-RESOURCE-ID}` | The full resource ID path you want to unassign. Found in the Azure portal under the _Properties_ tab for the resource as the _Resource ID_ field. | `/subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/resourceGroups/ContosoResourceGroup/providers/Microsoft.CognitiveServices/accounts/ContosoResource` |
 
 ### Get unassign resource status
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースIDのサンプル更新"
}
```

### Explanation
この変更は、Markdownファイル「unassign-resources.md」に対する小さな更新です。具体的には、`assignedResourceIds`の値が変更されました。旧値では、リソースIDが特定のサブスクリプションID「d73a1925-0000-0000-0000-0000c5fe888e」で示されていましたが、新しい例では、サブスクリプションIDが「aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e」に更新されています。この変更により、実際のAzureリソース環境における最新の情報が反映され、ユーザーが正しいリソースIDをより理解しやすくなります。全体として、この更新はわずかな変更ですが、ドキュメントの正確性と有用性を高めるものです。

## articles/ai-services/language-service/custom-text-classification/includes/rest-api/assign-resources.md{#item-e0b758}

<details>
<summary>Diff</summary>
````diff
@@ -51,7 +51,7 @@ Use the following sample JSON as your body.
 
 |Key  |Placeholder  |Value  | Example |
 |---------|---------|----------|--|
-| `azureResourceId` | `{AZURE-RESOURCE-ID}` | The full resource ID path you want to assign. Found in the Azure portal under the **Properties** tab for the resource, in the **Resource ID** field. | `/subscriptions/d73a1925-0000-0000-0000-0000c5fe888e/resourceGroups/ContosoResourceGroup/providers/Microsoft.CognitiveServices/accounts/ContosoResource` |
+| `azureResourceId` | `{AZURE-RESOURCE-ID}` | The full resource ID path you want to assign. Found in the Azure portal under the **Properties** tab for the resource, in the **Resource ID** field. | `/subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/resourceGroups/ContosoResourceGroup/providers/Microsoft.CognitiveServices/accounts/ContosoResource` |
 | `customDomain` | `{CUSTOM-DOMAIN}` | The custom subdomain of the resource you want to assign. Found in the Azure portal under the **Keys and Endpoint** tab for the resource, as the **Endpoint** field in the URL `https://<your-custom-subdomain>.cognitiveservices.azure.com/` | `contosoresource`  |
 | `region` | `{REGION-CODE}` |  A region code specifying the region of the resource you want to assign. Found in the Azure portal under the **Keys and Endpoint** tab for the resource, in the **Location/Region** field. |`eastus`|
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースIDのサンプル更新"
}
```

### Explanation
この変更は、Markdownファイル「assign-resources.md」に対する小さな更新を表しています。具体的には、`azureResourceId`というフィールドの例として示されるリソースIDが変更されました。旧バージョンでは、リソースIDが「d73a1925-0000-0000-0000-0000c5fe888e」であることが示されていましたが、更新されたバージョンでは「aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e」に変更されています。この修正により、ユーザーは最新のAzureリソースIDを正確に理解でき、実際のリソースに適用する際の信頼性が向上します。全体として、この修正はドキュメントの正確性を保つものであり、特に利用者にとっての利便性を向上させるものです。

## articles/ai-services/language-service/custom-text-classification/includes/rest-api/unassign-resources.md{#item-e7c3f6}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,7 @@ Use the following sample JSON as your body.
 
 |Key  |Placeholder  |Value  | Example |
 |---------|---------|----------|--|
-| `assignedResourceIds` | `{AZURE-RESOURCE-ID}` | The full resource ID path you want to unassign. Found in the Azure portal under the _Properties_ tab for the resource as the _Resource ID_ field. | `/subscriptions/d73a1925-0000-0000-0000-0000c5fe888e/resourceGroups/ContosoResourceGroup/providers/Microsoft.CognitiveServices/accounts/ContosoResource` |
+| `assignedResourceIds` | `{AZURE-RESOURCE-ID}` | The full resource ID path you want to unassign. Found in the Azure portal under the _Properties_ tab for the resource as the _Resource ID_ field. | `/subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/resourceGroups/ContosoResourceGroup/providers/Microsoft.CognitiveServices/accounts/ContosoResource` |
 
 ### Get unassign resource status
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソースIDのサンプル更新"
}
```

### Explanation
この変更は、Markdownファイル「unassign-resources.md」に対する小さな更新を示しています。主な変更点は、`assignedResourceIds`フィールドの例として記載されているリソースIDが更新されたことです。以前のリソースIDは「d73a1925-0000-0000-0000-0000c5fe888e」でしたが、更新後は「aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e」になっています。この改訂により、AzureポータルでのリソースIDの取得方法が明確に示され、ユーザーがより正確な情報を基に操作を行うことができるようになります。この修正はドキュメントの正確性を維持するためのものであり、ユーザーにとっての利便性を向上させる役割を果たします。

## articles/ai-services/language-service/orchestration-workflow/includes/rest-api/import-project.md{#item-c378dd}

<details>
<summary>Diff</summary>
````diff
@@ -60,7 +60,7 @@ Use the following sample JSON as your body.
         "orchestration": {
           "kind": "luis",
           "luisOrchestration": {
-            "appId": "00000000-0000-0000-0000-000000000000",
+            "appId": "00001111-aaaa-2222-bbbb-3333cccc4444",
             "appVersion": "string",
             "slotName": "string"
           },
@@ -91,4 +91,3 @@ Use the following sample JSON as your body.
 | `api-version` | `{API-VERSION}` | The version of the API you are calling. The version used here must be the same API version in the URL. | `2022-03-01-preview` |
 | `projectName` | `{PROJECT-NAME}` | The name of your project. This value is case-sensitive. | `EmailApp` |
 | `language` | `{LANGUAGE-CODE}` |  A string specifying the language code for the utterances used in your project. If your project is a multilingual project, choose the [language code](../../language-support.md) of the majority of the utterances. |`en-us`|
-
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "アプリIDのサンプル更新"
}
```

### Explanation
この変更は、Markdownファイル「import-project.md」に対する小さな更新を示しています。主な変更は、`luisOrchestration`オブジェクト内の`appId`フィールドに使われているサンプルアプリIDの変更です。旧バージョンではアプリIDが「00000000-0000-0000-0000-000000000000」として記載されていましたが、更新後は「00001111-aaaa-2222-bbbb-3333cccc4444」に変更されました。この更新により、ユーザーはより具体的かつ現実的なサンプルを参照できるようになり、実際のアプリケーション設定においても適切な情報を得ることができます。また、同ファイルの他の部分でも若干の削除及び変更が行われており、情報が整理されています。この修正は、ドキュメントの明瞭さと有用性を高めるためのものです。

## articles/ai-services/language-service/personally-identifiable-information/overview.md{#item-8a6932}

<details>
<summary>Diff</summary>
````diff
@@ -14,11 +14,16 @@ ms.custom: language-service-pii, build-2024, ignite-2024
 
 # What is Personally Identifiable Information (PII) detection in Azure AI Language?
 
-As of June 2024, we now provide General Availability support for the Conversational PII service (English-language only).
-Customers can now redact transcripts, chats, and other text written in a conversational style (i.e. text with “um”s, “ah”s, multiple speakers, and the spelling out of words for more clarity) with better confidence in AI quality, Azure SLA support and production environment support, and enterprise-grade security in mind.
-
 PII detection is one of the features offered by [Azure AI Language](../overview.md), a collection of machine learning and AI algorithms in the cloud for developing intelligent applications that involve written language. The PII detection feature can **identify, categorize, and redact** sensitive information in unstructured text. For example: phone numbers, email addresses, and forms of identification. Azure AI Language supports general text PII redaction, as well as [Conversational PII](how-to-call-for-conversations.md), a specialized model for handling speech transcriptions and the more informal, conversational tone of meeting and call transcripts. The service also supports [Native Document PII redaction](#native-document-support), where the input and output are structured document files.
 
+## What's new
+
+The Text PII and Conversational PII detection preview API (version `2024-11-15-preview`) now supports the option to mask detected sensitive entities with a label beyond just redaction characters. Customers have the option to specify if personally identifiable information content such as names and phone numbers, i.e. `“John Doe received a call from 424-878-9192”`, are masked with a redaction character, i.e. `“******** received a call from ************”`, or masked with an entity label, i.e. `“[PERSON_1] received a call from [PHONENUMBER_1]”`. More on how to specify the redaction policy style for your outputs can be found in our [how-to guides](how-to-call.md). 
+
+The Conversational PII detection models (both version `2024-11-01-preview` and `GA`) have been updated to provide enhanced AI quality and accuracy. The numeric identifier entity type now also includes Drivers License and Medicare Beneficiary Identifier.
+
+As of June 2024, we now provide General Availability support for the Conversational PII service (English-language only). Customers can now redact transcripts, chats, and other text written in a conversational style (i.e. text with “um”s, “ah”s, multiple speakers, and the spelling out of words for more clarity) with better confidence in AI quality, Azure SLA support and production environment support, and enterprise-grade security in mind.
+
 > [!TIP]
 > Try out PII detection [in AI Foundry portal](https://ai.azure.com/explore/language), where you can [utilize a currently existing Language Studio resource or create a new AI Foundry resource](../../../ai-studio/ai-services/connect-ai-services.md)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PII検出機能の新機能と改善"
}
```

### Explanation
この変更は、Markdownファイル「overview.md」に対する更新を示しており、個人を特定できる情報（PII）の検出機能に関する新しい情報が追加されています。主な追加内容には、テキストPIIおよび会話型PII検出のプレビューAPIが最新のバージョン`2024-11-15-preview`にて、検出した敏感なエンティティを赤文字記号だけでなく、ラベルでマスクするオプションが追加されたことが含まれています。また、会話型PII検出モデルの品質と精度が向上し、運転免許証番号やメディケア受益者番号が新たに数値識別子エンティティタイプとして追加されました。

さらに、2024年6月より、会話型PIIサービスが英語に関して一般提供されることが強調されています。この更新により、顧客はトランスクリプトやチャット、会話スタイルで書かれた他のテキストをより高い精度で赤外することができるようになります。新機能や改善点は、包括的なセキュリティと Azure SLA サポートを考慮に入れたものです。最後に、新機能を試すために AI Foundry ポータルの利用を促す情報も含まれています。この更新は、サービスの利用者にとって価値のある情報を提供し、AIの機能性を向上させることを目的としています。

## articles/ai-services/language-service/sentiment-opinion-mining/includes/custom/rest-api/assign-resources.md{#item-5d6080}

<details>
<summary>Diff</summary>
````diff
@@ -51,7 +51,7 @@ Use the following sample JSON as your body.
 
 |Key  |Placeholder  |Value  | Example |
 |---------|---------|----------|--|
-| `azureResourceId` | `{AZURE-RESOURCE-ID}` | The full resource ID path you want to assign. Found in the Azure portal under the **Properties** tab for the resource, in the **Resource ID** field. | `/subscriptions/d73a1925-0000-0000-0000-0000c5fe888e/resourceGroups/ContosoResourceGroup/providers/Microsoft.CognitiveServices/accounts/ContosoResource` |
+| `azureResourceId` | `{AZURE-RESOURCE-ID}` | The full resource ID path you want to assign. Found in the Azure portal under the **Properties** tab for the resource, in the **Resource ID** field. | `/subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/resourceGroups/ContosoResourceGroup/providers/Microsoft.CognitiveServices/accounts/ContosoResource` |
 | `customDomain` | `{CUSTOM-DOMAIN}` | The custom subdomain of the resource you want to assign. Found in the Azure portal under the **Keys and Endpoint** tab for the resource, as the **Endpoint** field in the URL `https://<your-custom-subdomain>.cognitiveservices.azure.com/` | `contosoresource`  |
 | `region` | `{REGION-CODE}` |  A region code specifying the region of the resource you want to assign. Found in the Azure portal under the **Keys and Endpoint** tab for the resource, in the **Location/Region** field. |`eastus`|
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Resource IDのサンプル変更"
}
```

### Explanation
この変更は、Markdownファイル「assign-resources.md」に対する小さな修正を示しています。具体的には、`azureResourceId`のサンプル値が更新されました。旧バージョンでは、リソースIDのサンプルが「/subscriptions/d73a1925-0000-0000-0000-0000c5fe888e/resourceGroups/ContosoResourceGroup/providers/Microsoft.CognitiveServices/accounts/ContosoResource」として示されていましたが、更新後は「/subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4/resourceGroups/ContosoResourceGroup/providers/Microsoft.CognitiveServices/accounts/ContosoResource」に変更されました。

この変更は、ユーザーがリソースIDを特定する際に最新の情報を反映するためのもので、Azureポータル内でのリソース識別を容易にする意図があります。また、そのほかの文は変更されておらず、全体的な文書の整合性は保たれています。このような更新により、ユーザーはより正確な情報を参照でき、効率的にリソースを管理することが可能となります。

## articles/ai-services/language-service/sentiment-opinion-mining/includes/custom/rest-api/unassign-resources.md{#item-05bc52}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,7 @@ Use the following sample JSON as your body.
 
 |Key  |Placeholder  |Value  | Example |
 |---------|---------|----------|--|
-| `assignedResourceIds` | `{AZURE-RESOURCE-ID}` | The full resource ID path you want to unassign. Found in the Azure portal under the _Properties_ tab for the resource as the _Resource ID_ field. | `/subscriptions/d73a1925-0000-0000-0000-0000c5fe888e/resourceGroups/ContosoResourceGroup/providers/Microsoft.CognitiveServices/accounts/ContosoResource` |
+| `assignedResourceIds` | `{AZURE-RESOURCE-ID}` | The full resource ID path you want to unassign. Found in the Azure portal under the _Properties_ tab for the resource as the _Resource ID_ field. | `/subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/resourceGroups/ContosoResourceGroup/providers/Microsoft.CognitiveServices/accounts/ContosoResource` |
 
 ### Get unassign resource status
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AssignリソースIDのサンプル変更"
}
```

### Explanation
この変更は、Markdownファイル「unassign-resources.md」における小規模な修正を示しています。具体的には、`assignedResourceIds`のサンプル値が更新されました。変更前のリソースIDの例は「/subscriptions/d73a1925-0000-0000-0000-0000c5fe888e/resourceGroups/ContosoResourceGroup/providers/Microsoft.CognitiveServices/accounts/ContosoResource」であったのに対し、変更後は「/subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e/resourceGroups/ContosoResourceGroup/providers/Microsoft.CognitiveServices/accounts/ContosoResource」に更新されています。

この修正は、Azureポータルにおけるリソースの正確な識別を促進するためのものであり、ユーザーがリソースIDを確認する際に最新の情報にアクセスできるようにしています。他の部分は変更されておらず、文書全体の整合性が保たれています。このような更新により、ユーザーはリソース管理の精度を高めることが可能になります。

## articles/ai-services/language-service/summarization/region-support.md{#item-d74574}

<details>
<summary>Diff</summary>
````diff
@@ -22,28 +22,28 @@ Some summarization features are only available in limited regions. More regions
 |------------------|----------------------------------|-----------------------------------------------|
 |US Gov Virginia   |&#9989;                           |&#9989;                                        |
 |US Gov Arizona    |&#9989;                           |&#9989;                                        |
-|North Europe      |&#9989;                           |&#9989;                                        |
+|Australia East    |&#9989;                           |&#9989;                                        |
+|Canada Central    |&#9989;                           |&#9989;                                        |
+|Central US        |&#9989;                           |&#9989;                                        |
+|China North 3     |&#9989;                           |&#9989;                                        |
 |East US           |&#9989;                           |&#9989;                                        |
 |East US 2         |&#9989;                           |&#9989;                                        |
-|Central US        |&#9989;                           |&#9989;                                        |
+|France Central    |&#9989;                           |&#9989;                                        |
+|Italy North       |&#9989;                           |&#9989;                                        |
+|Japan East        |&#9989;                           |&#9989;                                        |
+|North Central US  |&#9989;                           |&#9989;                                        |
+|North Europe      |&#9989;                           |&#9989;                                        |
 |South Central US  |&#9989;                           |&#9989;                                        |
-|West US           |&#9989;                           |&#9989;                                        |
-|West US 2         |&#9989;                           |&#9989;                                        |
+|South UK          |&#9989;                           |&#9989;                                        |
+|Southeast Asia    |&#9989;                           |&#9989;                                        |
+|Switzerland North |&#9989;                           |&#9989;                                        |
 |USNat East        |&#9989;                           |&#9989;                                        |
 |USNat West        |&#9989;                           |&#9989;                                        |
 |USSec East        |&#9989;                           |&#9989;                                        |
 |USSec West        |&#9989;                           |&#9989;                                        |
-|South UK          |&#9989;                           |&#9989;                                        |
-|Southeast Asia    |&#9989;                           |&#9989;                                        |
-|Australia East    |&#9989;                           |&#9989;                                        |
-|France Central    |&#9989;                           |&#9989;                                        |
-|Japan East        |&#9989;                           |&#9989;                                        |
-|North Central US  |&#9989;                           |&#9989;                                        |
-|Central Sweden    |&#9989;                           |&#9989;                                        |
-|Switzerland North |&#9989;                           |&#9989;                                        |
 |West Europe       |&#9989;                           |&#9989;                                        |
-|Italy North       |&#9989;                           |&#9989;                                        |
-|China North 3     |&#9989;                           |&#9989;                                        |
+|West US           |&#9989;                           |&#9989;                                        |
+|West US 2         |&#9989;                           |&#9989;                                        |
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "地域サポート情報の更新"
}
```

### Explanation
この変更は、Markdownファイル「region-support.md」に対する小さな修正を示しています。具体的には、サマリ機能が利用可能な地域のリストが更新され、新たに複数の地域が追加されました。特に、オーストラリア東部、カナダ中央部、中央米国、中国北部3、フランス中央部、イタリア北部、日本東部、北米中央部、及び北ヨーロッパなどの地域が追加されています。

加えて、元々リストにあった地域のいくつかが削除されています。例えば、中央スウェーデンや中国北部3などの地域がリストから外れています。これにより、ユーザーが利用可能な地域の最新情報を簡単に把握できるようになっています。この更新は、Azureの地域サポートについての理解を深め、ユーザーがサービスを利用する際の参考となります。変更は全体的に地域サポートに関する情報の正確性を向上させることを目的としています。

## articles/ai-studio/concepts/content-filtering.md{#item-91b372}

<details>
<summary>Diff</summary>
````diff
@@ -84,7 +84,7 @@ The configurability feature allows customers to adjust the settings, separately
 | High              | Yes| Yes | Content detected at severity levels low and medium isn't filtered. Only content at severity level high is filtered. Requires approval<sup>1</sup>.|
 | No filters | If approved<sup>1</sup>| If approved<sup>1</sup>| No content is filtered regardless of severity level detected. Requires approval<sup>1</sup>.|
 
-<sup>1</sup> For Azure OpenAI models, only customers who have been approved for modified content filtering have full content filtering control, including configuring content filters at severity level high only or turning off content filters. Apply for modified content filters via this form: [Azure OpenAI Limited Access Review: Modified Content Filters and Abuse Monitoring (microsoft.com)](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xURE01NDY1OUhBRzQ3MkQxMUhZSE1ZUlJKTiQlQCN0PWcu)
+<sup>1</sup> For Azure OpenAI models, only customers who have been approved for modified content filtering have full content filtering control, including configuring content filters at severity level high only or turning off content filters. Apply for modified content filters via these forms: [Azure OpenAI Limited Access Review: Modified Content Filters](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUMlBQNkZMR0lFRldORTdVQzQ0TEI5Q1ExOSQlQCN0PWcu), and [Modified Abuse Monitoring](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUOE9MUTFMUlpBNk5IQlZWWkcyUEpWWEhGOCQlQCN0PWcu).
 
 Customers are responsible for ensuring that applications integrating Azure OpenAI comply with the [Code of Conduct](/legal/cognitive-services/openai/code-of-conduct?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext). 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタリングのリファレンスリンクの更新"
}
```

### Explanation
この変更は、Markdownファイル「content-filtering.md」に対する小規模な修正を示しており、主にリンク部分に関する更新が行われています。具体的には、Azure OpenAIモデルにおける修正済みコンテンツフィルタリングのリクエストを行う際のフォームのリンクが変更されています。

変更前は1つのリンクが示されていましたが、変更後は新しい形式のリンクが2つ追加されています。この更新により、ユーザーは修正済みコンテンツフィルタリングと修正済みの悪用監視に関する二つの異なる申請フォームにアクセスできるようになっています。これにより、情報をより適切に提供し、ユーザーが必要なリソースに簡単にアクセスできるような利便性が向上されています。全体として、この修正はコンテンツフィルタリングに関する理解を深めることに寄与します。


