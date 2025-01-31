---
date: '2025-01-31'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:62147e0...MicrosoftDocs:7db5cb6
summary: |-
  このコード差分は、Azure AIサービス関連のドキュメントに一連の変更を加えたものです。主なポイントは、新機能のサポート情報の追加と破壊的変更の明示です。特に、個人情報識別に関するエンティティ情報が削除され、DeepSeekモデルが新たに追加されたことが重要です。

  新機能としては、「Changelog and migration guide」エントリの再追加や、テキストPIIと対話型PII検出プレビューAPIの機能の強調、DeepSeekモデルに関する新しい情報が提供されています。一方、破壊的変更として、個人情報識別エンティティ情報が明確に削除され、非推奨のエンティティの扱いが整理されました。

  その他、移行ガイドの追加、新しいロール要件とセキュリティ設定の更新、コンテンツ安全性情報の追加が行われています。これらの変更はAzure AIサービスのドキュメントを明確化し、ユーザーが新しいサービス機能を効果的に利用できるようにすることを目的としています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:62147e0...MicrosoftDocs:7db5cb6){target="_blank"}

# ハイライト
このコード差分は、Azure AIサービス関連のドキュメントに対する一連の変更を含んでいます。主なポイントは、新機能のサポート情報の追加や破壊的変更（Deprecated）の表明です。特に、個人情報識別に関するエンティティ情報の削除と、DeepSeekモデルの新規追加が重要です。

## 新機能
- `toc.yml`では、「Changelog and migration guide」エントリが再追加。
- `overview.md`にテキストPIIおよび対話型PII検出プレビューAPIの機能が強調されました。
- `model-catalog-overview.md`と`region-availability-maas.md`では、DeepSeekモデルに関する新情報が追加。

## 破壊的変更
- `identification-entities.md`から44行の個人情報識別エンティティ情報が削除され、これによりDeprecatedなエンティティの扱いを明確化。

## その他の更新
- `changelog-release-history.md`での移行ガイドの追加と整理。
- `configure-managed-network.md`において、新しいロール要件とセキュリティ設定の追加。
- `deploy-models-deepseek.md`でのコンテンツ安全性情報の追加。

# 洞察
この変更は、Azure AIサービスにおけるドキュメントを明確化し、ユーザーが最新のサービス機能を正しく活用できるようにするためのものです。

まず、新しいDeepSeekモデルの導入は、AIモデル関連の可用性を拡大し、ユーザーに新しい選択肢を提供する意図が明確です。特に、地域可用性に関する情報が整理されて追加されたことは、運用を円滑に進めるための実用的なガイドとなるでしょう。

さらに、個人情報識別エンティティの削除は、セキュリティとプライバシーに配慮した措置です。これにより、ユーザーは非推奨のAPIバージョンを利用し続けるリスクを減少させることができます。

また、Azure AI Studioのドキュメントにおける構成およびセキュリティの向上は、企業ユーザーが本番環境での信頼性を高めるのに役立ちます。マネージドネットワークの設定ガイドやモデルデプロイガイドの更新は、セキュリティ上の配慮とコンテンツセーフティ機能の統合を意識したものです。

これらの改訂により、ユーザーはAIサービスの新機能を効果的に利用し、迅速な対応が必要な破壊的変更についても把握することが可能となりました。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [toc.yml](#item-81aa7b) | minor update | 目次の修正と更新 | modified | 4 | 4 | 8 | 
| [changelog-release-history.md](#item-dccdd3) | minor update | ドキュメントインテリジェンスの変更履歴の更新 | modified | 4 | 4 | 8 | 
| [identification-entities.md](#item-9bf762) | breaking change | 個人情報識別エンティティの情報削除 | modified | 0 | 44 | 44 | 
| [overview.md](#item-8a6932) | minor update | 個人情報識別の概要の軽微な更新 | modified | 2 | 2 | 4 | 
| [configure-managed-network.md](#item-dc9c50) | minor update | マネージドネットワークの設定ガイドの更新 | modified | 3 | 0 | 3 | 
| [deploy-models-deepseek.md](#item-7c33de) | minor update | DeepSeekモデルデプロイガイドの更新 | modified | 5 | 4 | 9 | 
| [model-catalog-overview.md](#item-278001) | minor update | モデルカタログ概要の更新 | modified | 1 | 0 | 1 | 
| [region-availability-maas.md](#item-35d79c) | minor update | MaaSの地域可用性に関する情報の追加 | modified | 6 | 0 | 6 | 


# Modified Contents
## articles/ai-services/document-intelligence/toc.yml{#item-81aa7b}

<details>
<summary>Diff</summary>
````diff
@@ -37,9 +37,6 @@ items:
     href: service-limits.md
   - name: Document Intelligence client libraries
     items:
-      - name: Changelog and migration guide
-        displayName: latest, update, beta, package, preview, version
-        href: changelog-release-history.md
       - name: "SDK targets: REST API v4.0 2024-11-30 latest (GA)"
         displayName: get started, installation, downloads, documentAnalysisClient, document analysis client, Azure AD, Azure Active Directory, identity, changelog, package, version,AzureKeyCredential, Azure key credential, key, endpoint
         href: sdk-overview-v4-0.md
@@ -52,7 +49,10 @@ items:
       - name:  "SDK targets: REST API v2.1 (GA)"
         displayName: get started, installation, downloads, formRecognizerClientClient, form recognizer client, Azure AD, Azure Active Directory, identity, changelog, package, version,AzureKeyCredential, Azure key credential, key, endpoint
         href: v21/sdk-overview-v2-1.md
-  - name: FAQ
+  - name: Changelog and migration guide
+    displayName: latest, update, beta, package, preview, version
+    href: changelog-release-history.md      
+  - name: Frequently asked questions (FAQ)
     displayName: storage, security, privacy, help, support, versions, development, migrate, migration, cognitive, applied, form recognizer, form, recognizer
     href: faq.yml
 - name: Prebuilt models
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次の修正と更新"
}
```

### Explanation
この変更では、`toc.yml`ファイルの内容が一部修正され、いくつかの項目が更新されています。具体的には、「Changelog and migration guide」というエントリが再追加され、その表示名とリンクが正しく設定されています。さらに、既存の「FAQ」セクションの名前が更新され、説明名が追加されました。これにより、ユーザーは情報をより簡単に見つけることができるようになります。この変更は4行の追加と4行の削除があり、合計で8行の変更が行われました。

## articles/ai-services/document-intelligence/versioning/changelog-release-history.md{#item-dccdd3}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: Document Intelligence changelog and release history
+title: Document Intelligence changelog, release history, and migration guide
 titleSuffix: Azure AI services
-description: A version-based description of Document Intelligence feature and capability releases, changes, enhancements,  and updates.
+description: A version-based description of Document Intelligence feature and capability releases, changes, enhancements, migration guidance, and updates.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
@@ -15,7 +15,7 @@ ms.author: lajanuar
 <!-- markdownlint-disable MD051 -->
 <!-- markdownlint-disable MD024 -->
 
-# SDK changelog and release history
+# SDK changelog, release history, and migration guide
 
 This reference article provides a version-based description of Document Intelligence feature and capability releases, changes, updates, and enhancements.
 
@@ -414,7 +414,7 @@ This release includes the following updates:
 This release includes the following updates:
 
 > [!IMPORTANT]
-> The `DocumentAnalysisClient` and `DocumentModelAdministrationClient` now target API v3.0 GA, released 2022-08-31. These clients are no longer supported by APIs 2020-06-30-preview or earlier.
+> The `DocumentAnalysisClient` and `DocumentModelAdministrationClient` now target API v3.0 GA, released 2022-08-31. Document Intelligence no longer supports clients from 2020-06-30-preview APIs or earlier.
 
 ### [**C#**](#tab/csharp)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスの変更履歴の更新"
}
```

### Explanation
この変更では、`changelog-release-history.md`ファイルの内容が一部修正され、新しい情報が加えられています。具体的には、ドキュメントのタイトルに「migration guide」を追加し、説明にも「migration guidance」を含めることで、移行ガイドの存在を明示しています。また、SDKの変更履歴セクションの見出しも更新され、一貫性を持たせています。最後に、`DocumentAnalysisClient`および`DocumentModelAdministrationClient`に関する注意書きがより明確に表現され、これらのクライアントが古いAPIをサポートしないことが強調されています。この変更は4行の追加と4行の削除があり、合計で8行の変更が行われました。

## articles/ai-services/language-service/personally-identifiable-information/includes/identification-entities.md{#item-9bf762}

<details>
<summary>Diff</summary>
````diff
@@ -370,30 +370,6 @@ The following entities are grouped and listed by country/region:
       
    :::column-end:::
 :::row-end:::
-:::row:::
-    :::column span="":::
-        **Entity**
-
-        Belgium national number V2
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        To get this entity category, add `BENationalNumberV2` to the `piiCategories` parameter. `BENationalNumberV2` will be returned in the API response if detected.
-      
-        Also returned with `domain=phi`.
-
-        This entity is deprecated
-
-    :::column-end:::
-    :::column span="":::
-      **Supported languages**
-
-      `fr`, `de`
-      
-   :::column-end:::
-:::row-end:::
 
 :::row:::
     :::column span="":::
@@ -1168,26 +1144,6 @@ The following entities are grouped and listed by country/region:
       
    :::column-end:::
 :::row-end:::
-:::row:::
-    :::column span="":::
- 
-        Ireland Personal Public Service (PPS) Number v2
-
-    :::column-end:::
-    :::column span="2":::
-
-        To get this entity category, add `IEPersonalPublicServiceNumberV2` to the `piiCategories` parameter. `IEPersonalPublicServiceNumberV2` will be returned in the API response if detected.
-
-        This entity is deprecated
-      
-    :::column-end:::
-    :::column span="":::
-      **Supported languages**
-
-      `en`
-      
-   :::column-end:::
-:::row-end:::
 
 ### Israel
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "個人情報識別エンティティの情報削除"
}
```

### Explanation
この変更では、`identification-entities.md`ファイルから44行が削除されました。具体的には、ベルギーの国家番号V2やアイルランドの個人公共サービス番号V2などの個人情報識別エンティティに関する詳細情報が削除されています。これにより、これらのエンティティが非推奨であることが反映され、APIレスポンスにおいてもこれらのカテゴリが返されないことが示唆されています。この変更は、区分されていた国ごとのエンティティリストに影響を与え、ユーザーにとっては重要な情報の欠落となるため、破壊的な変更と見なされます。

## articles/ai-services/language-service/personally-identifiable-information/overview.md{#item-8a6932}

<details>
<summary>Diff</summary>
````diff
@@ -18,11 +18,11 @@ PII detection is one of the features offered by [Azure AI Language](../overview.
 
 ## What's new
 
-The Text PII and Conversational PII detection preview API (version `2024-11-15-preview`) now supports the option to mask detected sensitive entities with a label beyond just redaction characters. Customers have the option to specify if personally identifiable information content such as names and phone numbers, i.e. `“John Doe received a call from 424-878-9192”`, are masked with a redaction character, i.e. `“******** received a call from ************”`, or masked with an entity label, i.e. `“[PERSON_1] received a call from [PHONENUMBER_1]”`. More on how to specify the redaction policy style for your outputs can be found in our [how-to guides](how-to-call.md). 
+The Text PII and Conversational PII detection preview API (version `2024-11-15-preview`) now supports the option to mask detected sensitive entities with a label beyond just redaction characters. Customers have the option to specify if personally identifiable information content such as names and phone numbers, i.e. `"John Doe received a call from 424-878-9192"`, are masked with a redaction character, i.e. `"******** received a call from ************"`, or masked with an entity label, i.e. `"[PERSON_1] received a call from [PHONENUMBER_1]"`. More on how to specify the redaction policy style for your outputs can be found in our [how-to guides](how-to-call.md). 
 
 The Conversational PII detection models (both version `2024-11-01-preview` and `GA`) have been updated to provide enhanced AI quality and accuracy. The numeric identifier entity type now also includes Drivers License and Medicare Beneficiary Identifier.
 
-As of June 2024, we now provide General Availability support for the Conversational PII service (English-language only). Customers can now redact transcripts, chats, and other text written in a conversational style (i.e. text with “um”s, “ah”s, multiple speakers, and the spelling out of words for more clarity) with better confidence in AI quality, Azure SLA support and production environment support, and enterprise-grade security in mind.
+As of June 2024, we now provide General Availability support for the Conversational PII service (English-language only). Customers can now redact transcripts, chats, and other text written in a conversational style (i.e. text with "um"s, "ah"s, multiple speakers, and the spelling out of words for more clarity) with better confidence in AI quality, Azure SLA support and production environment support, and enterprise-grade security in mind.
 
 > [!TIP]
 > Try out PII detection [in Azure AI Foundry portal](https://ai.azure.com/explore/language), where you can [utilize a currently existing Language Studio resource or create a new Azure AI Foundry resource](../../../ai-studio/ai-services/connect-ai-services.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "個人情報識別の概要の軽微な更新"
}
```

### Explanation
この変更では、`overview.md`ファイルの内容が軽微に更新され、2行の追加と2行の削除が行われました。主な更新点は、テキストPII（個人情報）および対話型PII検出プレビューAPI（バージョン`2024-11-15-preview`）が、検出された敏感なエンティティを単なる赤色のマスク文字以上のラベルでマスクするオプションをサポートすることを強調しています。具体例を使用して、名前や電話番号がどのようにマスクされるかが示されています。また、対話型PIIサービスの一般提供（GA）のサポートが2024年6月から始まったことが明確にされ、エンタープライズグレードのセキュリティやAI品質の向上が強調されています。この更新は、ユーザーに対して最新の機能とサポート状況を提供する目的で行われています。

## articles/ai-studio/how-to/configure-managed-network.md{#item-dc9c50}

<details>
<summary>Diff</summary>
````diff
@@ -845,6 +845,9 @@ When you create a private endpoint for hub dependency resources, such as Azure S
 
 A private endpoint is automatically created for a connection if the target resource is an Azure resource listed previously. A valid target ID is expected for the private endpoint. A valid target ID for the connection can be the Azure Resource Manager ID of a parent resource. The target ID is also expected in the target of the connection or in `metadata.resourceid`. For more on connections, see [How to add a new connection in Azure AI Foundry portal](connections-add.md).
 
+> [!IMPORTANT]
+> As of March 31st 2025, the Azure AI Enterprise Network Connection Approver role must be assigned to the Azure AI Foundry hub's managed identity to approve private endpoints to securely access your Azure resources from the managed virtual network. This does not impact existing resources with approved private endpoints as the role is correctly assigned by the service. For new resources, please ensure the role is assigned to the hub's managed identity. For Azure Data Factory, Azure Databricks, and Azure Function Apps, the Contributor role should instead be assigned to your hub's managed identity. This role assignment is applicable to both User-assigned identity and System-assigned identity workspaces. 
+
 ## Select an Azure Firewall version for allowed only approved outbound (Preview)
 
 An Azure Firewall is deployed if an FQDN outbound rule is created while in the _allow only approved outbound_ mode. Charges for the Azure Firewall are included in your billing. By default, a __Standard__ version of AzureFirewall is created. Optionally, you can select to use a __Basic__ version. You can change the firewall version used as needed. To figure out which version is best for you, visit [Choose the right Azure Firewall version](/azure/firewall/choose-firewall-sku).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マネージドネットワークの設定ガイドの更新"
}
```

### Explanation
この変更では、`configure-managed-network.md`ファイルに3行が追加されました。主な内容は、Azure AI Foundryハブのマネージドアイデンティティに対して、2025年3月31日以降にプライベートエンドポイントを承認するためには「Azure AI Enterprise Network Connection Approver」ロールを割り当てる必要があるという重要な情報です。この変更は、新しいリソースを作成する際に適用されますが、すでに承認されたプライベートエンドポイントに影響はありません。また、Azure Data Factory、Azure Databricks、Azure Function Appsの場合、ハブのマネージドアイデンティティには「Contributor」ロールを代わりに割り当てるべきであることが説明されています。これに加えて、承認されたアウトバウンド接続のみを許可するためのAzure Firewallバージョンの選択に関する新しいセクションが追加され、ユーザーが自身のニーズに最も適したファイアウォールバージョンを選択できるように導いています。

## articles/ai-studio/how-to/deploy-models-deepseek.md{#item-7c33de}

<details>
<summary>Diff</summary>
````diff
@@ -21,6 +21,7 @@ zone_pivot_groups: azure-ai-model-catalog-samples-chat
 In this article, you learn about DeepSeek-R1 and how to use them.
 DeepSeek-R1 excels at reasoning tasks using a step-by-step training process, such as language, scientific reasoning, and coding tasks. It features 671B total parameters with 37B active parameters, and 128k context length.
 
+[!INCLUDE [models-preview](../includes/models-preview.md)]
 
 
 ::: zone pivot="programming-language-python"
@@ -240,7 +241,7 @@ print_stream(result)
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -507,7 +508,7 @@ for await (const event of sses) {
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -800,7 +801,7 @@ StreamMessageAsync(client).GetAwaiter().GetResult();
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -1086,7 +1087,7 @@ The last message in the stream has `finish_reason` set, indicating the reason fo
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DeepSeekモデルデプロイガイドの更新"
}
```

### Explanation
この変更では、`deploy-models-deepseek.md`ファイルが更新され、5行が追加され、4行が削除される形で合計9行の変更が加えられました。主に、Azure AIモデル推論APIがサポートする「Azure AIコンテンツ安全性」に関する情報が強調されています。この更新により、コンテンツフィルタリングシステムがプレビューとして機能する旨が明記され、潜在的に有害なコンテンツに対して検出および対処を行うことがより明確になりました。

また、各セクションにおいて「コンテンツ安全性」の適用に関する重要情報を繰り返し記載することで、その機能の重要性を強調しています。これにより、ユーザーは有害なコンテンツを防ぐための具体的な対策方法を理解しやすくなっています。

## articles/ai-studio/how-to/model-catalog-overview.md{#item-278001}

<details>
<summary>Diff</summary>
````diff
@@ -79,6 +79,7 @@ Model | Managed compute | Serverless API (pay-per-token)
 --|--|--
 AI21 family models | Not available | Jamba-1.5-Mini <br> Jamba-1.5-Large
 Cohere family models | Not available | Cohere-command-r-plus-08-2024 <br> Cohere-command-r-08-2024 <br> Cohere-command-r-plus <br> Cohere-command-r <br> Cohere-embed-v3-english <br> Cohere-embed-v3-multilingual <br> Cohere-rerank-v3-english <br> Cohere-rerank-v3-multilingual
+DeepSeek models from Microsoft | Not available | DeepSeek-R1
 Gretel | Not available | Gretel-Navigator
 Healthcare AI family Models | MedImageParse<BR>  MedImageInsight<BR>  CxrReportGen<BR>  Virchow<BR>  Virchow2<BR>  Prism<BR>  BiomedCLIP-PubMedBERT<BR>  microsoft-llava-med-v1.5<BR>  m42-health-llama3-med4<BR>  biomistral-biomistral-7b<BR>  microsoft-biogpt-large-pub<BR>  microsoft-biomednlp-pub<BR>  stanford-crfm-biomedlm<BR>  medicalai-clinicalbert<BR>  microsoft-biogpt<BR>  microsoft-biogpt-large<BR>  microsoft-biomednlp-pub<BR> | Not Available
 JAIS | Not available | jais-30b-chat
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルカタログ概要の更新"
}
```

### Explanation
この変更では、`model-catalog-overview.md`ファイルが更新され、DeepSeekモデルに関する情報が新たに追加されました。具体的には、MicrosoftのDeepSeekモデルが「サーバーレスAPI（支払いはトークン単位）」のカテゴリに「DeepSeek-R1」として追加され、一部のモデルの利用状況がより明確に示されるようになりました。

これにより、ユーザーはDeepSeekモデルを含むさまざまなAIモデルに対する概要をより理解しやすくなり、利用可能なリソースの選択肢が増えたことが強調されています。この小さな追加が、Kaggleやデータサイエンスのワークフローにおけるモデル選択の際に役立つことを目的としています。

## articles/ai-studio/includes/region-availability-maas.md{#item-35d79c}

<details>
<summary>Diff</summary>
````diff
@@ -24,6 +24,12 @@ Cohere Rerank v3 - Multilingual   |  [Microsoft Managed countries/regions](/part
 Cohere Embed v3 - English    |  [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar   |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3    | Not available       |
 Cohere Embed v3 -  Multilingual    |  [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions) <br> Japan <br> Qatar   |East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3    | Not available       |
 
+### DeepSeek models from Microsoft
+
+| Model | Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
+|---------|---------|---------|---------|
+DeepSeek-R1                       | Not applicable | East US <br> East US 2 <br> North Central US <br> South Central US <br> West US <br> West US 3  | Not available       |
+
 
 ### Gretel models
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "MaaSの地域可用性に関する情報の追加"
}
```

### Explanation
この変更では、`region-availability-maas.md`ファイルが更新され、MicrosoftのDeepSeekモデルに関する情報が新たに追加されました。具体的には、DeepSeek-R1モデルに関するテーブルが挿入され、利用可能な地域、デプロイメント用のハブ／プロジェクト地域、ファインチューニング用の地域が整理されて記載されています。

DeepSeekモデルは、地域可用性に関して「適用不可」であることが明記され、デプロイメントにおいては「East US」や「West US」などの地域での利用が可能であることが示されています。このアップデートにより、DeepSeekモデルの可用性についての理解が深まり、ユーザーがモデルを利用する際の地域選択に役立つ情報が提供されました。


