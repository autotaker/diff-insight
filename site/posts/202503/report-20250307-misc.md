---
date: '2025-03-07'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:31c2d64...MicrosoftDocs:4d90f76
summary: このコード差分は、Azure AIサービスのドキュメントに対する様々な更新と修正を含んでおり、新機能の追加や既存ドキュメントの正確性と可読性の向上を目的としています。新たにネイティブドキュメントサポートの概要やテキスト要約APIの新しいドキュメントが追加されました。また、PII関連のドキュメントのリネームと修正、要約APIに関するドキュメントの微調整も行われました。この更新は、Azure
  AI Languageサービスの機能に対するドキュメントの質を向上させ、ユーザーがより使いやすくなるように工夫されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:31c2d64...MicrosoftDocs:4d90f76){target="_blank"}

<format>
# Highlights
このコード差分は、Azure AIサービスのドキュメントに対する様々な更新と修正を含んでおり、新しい機能の追加や、既存ドキュメントの正確性と可読性の向上を目的としています。
新機能には、ネイティブドキュメントサポートの概要の追加や、テキスト要約APIの新しいドキュメントが含まれます。
その他の更新としては、PII（個人識別情報）関連のドキュメントのリネームと修正、要約APIに関するドキュメントの微調整が行われました。

## New features
- Azure AI 言語向けのネイティブドキュメントサポートの概要の追加。

## Breaking changes
- カスタムセンチメント分析（プレビュー）のリタイア延期情報が整理され、関連の通知文が簡略化されました。

## Other updates
- マネージドアイデンティティ、SASトークン、PII関連のドキュメントの修正。
- ドキュメント要約API、会話要約機能に関するガイドの更新。
- 目次（TOC）の整理とリンクの調整。

# Insights
この更新は、Azure AI Languageサービスのさまざまな機能に対するドキュメントの質を向上させることを目的としています。特に、新しい機能に関する情報が追加され、既存のドキュメントがより正確で分かりやすくなるように工夫されています。

新しいナティブドキュメントサポートの概要は、ユーザーがテキストデータをAzureのAIサービスを使って直接処理するための実用的な手引きとして機能します。この追加により、ユーザーは複雑なテキスト前処理を必要とせず、APIを効果的に利用できるでしょう。

さらに、要約機能関連のドキュメントの更新は、Azureが既存の機能をどのようにアップデートし、ユーザーエクスペリエンスを向上させるかに焦点を当てています。テキストや会話データの要約に関する説明が整理され、ユーザーがこれらの機能をより簡単に活用できるよう配慮されています。

個人情報保護（PII）に関するドキュメントの変更は、セキュリティとプライバシーへの配慮がいかに重要視されているかを示しています。新しい用語やリンクの整理により、ユーザーが必要な情報を迅速に取得し、適切にPIIを管理する手助けをします。

総じて、このドキュメントの更新は、Azure AIユーザーにとってさらなる利便性と使いやすさを提供し、最新の技術適用を促進する重要な改善であるといえます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [managed-identities.md](#item-ddd66a) | minor update | マネージドアイデンティティのサポートに関するドキュメントの更新 | modified | 6 | 6 | 12 | 
| [overview.md](#item-a490e5) | new feature | Azure AI 言語向けのネイティブドキュメントサポートの概要を追加 | added | 76 | 0 | 76 | 
| [shared-access-signatures.md](#item-01eef1) | minor update | SASトークンに関するドキュメントの修正 | modified | 8 | 10 | 18 | 
| [overview.md](#item-f138b4) | minor update | Azure AI 言語サービスの概要ドキュメントの修正 | modified | 29 | 29 | 58 | 
| [redact-conversation-pii.md](#item-0d6332) | minor update | 会話からの個人情報の検出と削除に関するドキュメントのリネームと修正 | renamed | 75 | 79 | 154 | 
| [redact-document-pii.md](#item-5509ee) | minor update | ネイティブドキュメントから個人情報を特定・抽出するドキュメントのリネームと修正 | renamed | 20 | 183 | 203 | 
| [redact-text-pii.md](#item-9e48af) | minor update | テキストからの個人情報特定・抽出方法に関するドキュメントのリネームと修正 | renamed | 18 | 19 | 37 | 
| [overview.md](#item-8a6932) | minor update | Azure AI Languageの個人識別情報(PII)検出に関する概要の更新 | modified | 78 | 24 | 102 | 
| [conversation-summarization.md](#item-9ff946) | minor update | 会話要約機能に関するドキュメントの更新 | modified | 29 | 31 | 60 | 
| [document-summarization.md](#item-da1a14) | minor update | 文書要約APIに関するドキュメントの大幅な更新 | modified | 256 | 136 | 392 | 
| [text-summarization.md](#item-8a6034) | new feature | テキスト要約APIの利用方法に関する新規ドキュメントの追加 | added | 348 | 0 | 348 | 
| [overview.md](#item-844139) | minor update | サマリー機能に関する概要ドキュメントの調整 | modified | 26 | 25 | 51 | 
| [toc.yml](#item-12f1f0) | minor update | TOCの更新: PII関連のガイドと要約APIのリンクの整理 | modified | 14 | 10 | 24 | 
| [whats-new.md](#item-69b272) | minor update | 最新情報ドキュメントの更新 | modified | 5 | 5 | 10 | 


# Modified Contents
## articles/ai-services/language-service/native-document-support/managed-identities.md{#item-ddd66a}

<details>
<summary>Diff</summary>
````diff
@@ -6,15 +6,15 @@ ms.topic: how-to
 manager: nitinme
 ms.author: lajanuar
 author: laujan
-ms.date: 11/21/2024
+ms.date: 03/05/2025
 ---
 
 
 # Managed identities for Language resources
 
-Managed identities for Azure resources are service principals that create a Microsoft Entra identity and specific permissions for Azure managed resources. Managed identities are a safer way to grant access to storage data and replace the requirement for you to include shared access signature tokens (SAS) with your [source and target container URLs](use-native-documents.md#create-azure-blob-storage-containers).
+Managed identities for Azure resources are service principals that create a Microsoft Entra identity and specific permissions for Azure managed resources. Managed identities are a safer way to grant access to storage data and replace the requirement for you to include shared access signature tokens (SAS) with your source and target container URLs.
 
-   :::image type="content" source="media/managed-identity-flow.png" alt-text="Screenshot of managed identity flow (RBAC).":::
+   :::image type="content" source="media/managed-identity-flow.png" alt-text="Screenshot of managed identity flow (`RBAC`).":::
 
 * You can use managed identities to grant access to any resource that supports Microsoft Entra authentication, including your own applications.
 
@@ -24,7 +24,7 @@ Managed identities for Azure resources are service principals that create a Micr
 
 > [!IMPORTANT]
 >
-> * When using managed identities, don't include a SAS token URL with your HTTP requests—your requests will fail. Using managed identities replaces the requirement for you to include shared access signature tokens (SAS) with your [source and target container URLs](use-native-documents.md#create-azure-blob-storage-containers).
+> * When using managed identities, don't include a SAS token URL with your HTTP requests. Using managed identities replaces the requirement for you to include shared access signature tokens (SAS) with your source and target container URLs.
 >
 > * To use managed identities for Language operations, you must [create your Language resource](https://ms.portal.azure.com/#create/Microsoft.CognitiveServicesTextAnalytics) in a specific geographic Azure region such as **East US**. If your Language resource region is set to **Global**, then you can't use managed identity authentication. You can, however, still use [Shared Access Signature (SAS) tokens](shared-access-signatures.md).
 >
@@ -65,7 +65,7 @@ To get started, you need the following resources:
 
 ## Managed identity assignments
 
-There are two types of managed identities: **system-assigned** and **user-assigned**.  Currently, Document Translation supports **system-assigned managed identity**:
+There are two types of managed identities: **system-assigned** and **user-assigned**. Currently, Document Translation supports **system-assigned managed identity**:
 
 * A system-assigned managed identity is **enabled** directly on a service instance. It isn't enabled by default; you must go to your resource and update the identity setting.
 
@@ -135,4 +135,4 @@ You must grant the Language resource access to your storage account before it ca
 ## Next steps
 
 > [!div class="nextstepaction"]
-> [Get started with native document support](use-native-documents.md#include-native-documents-with-an-http-request)
+> [Native document support](overview.md#native-document-support-for-azure-ai-language-preview)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マネージドアイデンティティのサポートに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azureのマネージドアイデンティティに関するドキュメント内での軽微な更新を含んでいます。主な変更点は、日付の更新やテキストの明瞭化です。具体的には、ドキュメントのメタデータである「ms.date」が2024年11月21日から2025年3月5日に変更されました。また、文中のSASトークンに関する説明が修正され、内容がスムーズに読めるように改善されています。

さらに、画像のaltテキストが変更され、"RBAC"がバッククォートで囲まれた形に修正され、用語の明確さが向上しています。全体的に、これらの変更は文書の正確性と可読性を向上させることを目的としています。

## articles/ai-services/language-service/native-document-support/overview.md{#item-a490e5}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,76 @@
+---
+title: Native document support for Azure AI Language (preview)
+titleSuffix: Azure AI services
+description: How to use native document with Azure AI Languages Personally Identifiable Information and Summarization capabilities.
+author: laujan
+manager: nitinme
+ms.service: azure-ai-language
+ms.custom:
+  - ignite-2024
+ms.topic: how-to
+ms.date: 02/19/2025
+ms.author: lajanuar
+---
+
+<!-- markdownlint-disable MD033 -->
+<!-- markdownlint-disable MD051 -->
+<!-- markdownlint-disable MD024 -->
+<!-- markdownlint-disable MD036 -->
+<!-- markdownlint-disable MD049 -->
+<!-- markdownlint-disable MD001 -->
+
+# Native document support for Azure AI Language (preview)
+
+> [!IMPORTANT]
+>
+> * Azure AI Language public preview releases provide early access to features that are in active development.
+> * Features, approaches, and processes can change, before General Availability (GA), based on user feedback.
+
+Azure AI Language is a cloud-based service that applies Natural Language Processing (NLP) features to text-based data. The native document support capability enables you to send API requests asynchronously, using an HTTP POST request body to send your data and HTTP GET request query string to retrieve the status results. Your processed documents are located in your Azure Blob Storage target container.
+
+A native document refers to the file format used to create the original document such as Microsoft Word (docx) or a portable document file (pdf). Native document support eliminates the need for text preprocessing before using Azure AI Language resource capabilities. Currently, native document support is available for the following capabilities:
+
+* [Personally Identifiable Information (PII)](../personally-identifiable-information/overview.md). The PII detection feature can identify, categorize, and redact sensitive information in unstructured text. The `PiiEntityRecognition` API supports native document processing.
+
+* [Document summarization](../summarization/overview.md). Document summarization uses natural language processing to generate extractive (salient sentence extraction) or abstractive (contextual word extraction) summaries for documents. Both `AbstractiveSummarization` and `ExtractiveSummarization` APIs support native document processing.
+
+## Supported document formats
+
+ Applications use native file formats to create, save, or open native documents. Currently **PII** and **Document summarization** capabilities supports the following native document formats:
+
+|File type|File extension|Description|
+|---------|--------------|-----------|
+|Text| `.txt`|An unformatted text document.|
+|Adobe PDF| `.pdf`|A portable document file formatted document.|
+|Microsoft Word| `.docx`|A Microsoft Word document file.|
+
+## Input guidelines
+
+***Supported file formats***
+
+|Type|support and limitations|
+|---|---|
+|**PDFs**| Fully scanned PDFs aren't supported.|
+|**Text within images**| Digital images with embedded text aren't supported.|
+|**Digital tables**| Tables in scanned documents aren't supported.|
+
+***Document Size***
+
+|Attribute|Input limit|
+|---|---|
+|**Total number of documents per request** |**≤ 20**|
+|**Total content size per request**| **≤ 10 MB**|
+
+## Request headers and parameters
+
+|parameter  |Description  |
+|---------|---------|
+|`-X POST <endpoint>`     | Specifies your Language resource endpoint for accessing the API.        |
+|`--header Content-Type: application/json`     | The content type for sending JSON data.          |
+|`--header "Ocp-Apim-Subscription-Key:<key>`    | Specifies the Language resource key for accessing the API.        |
+|`-data`     | The JSON file containing the data you want to pass with your request.         |
+
+## Related content
+
+> [!div class="nextstepaction"]
+> [PII detection overview](../personally-identifiable-information/overview.md "Learn more about Personally Identifiable Information detection.") [Document Summarization overview](../summarization/overview.md "Learn more about automatic document summarization.")
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure AI 言語向けのネイティブドキュメントサポートの概要を追加"
}
```

### Explanation
この変更は、新たに「ネイティブドキュメントサポートに関する概要」ドキュメントを追加するものであり、Azure AI Languageサービスの機能に関する詳細情報を提供します。このドキュメントでは、ネイティブドキュメントサポートの利用方法や、対象となるファイルフォーマット、APIリクエスト方法について説明されています。

具体的には、Azure AI Languageは自然言語処理を用いてテキストデータを処理できるクラウドベースのサービスであり、ネイティブドキュメントサポートを利用することで、ユーザーはテキスト前処理なしにAPIリクエストを送信できることが強調されています。また、個人情報の検出（PII）や文書要約に関する機能がネイティブドキュメント形式でサポートされていることも明記されています。

ドキュメントには、サポートされるファイル形式、入力ガイドライン、要求のヘッダーやパラメーターに関する具体的な情報も含まれており、ユーザーがこれらの機能を効果的に活用できるような内容になっています。全体として、この追加はユーザーに対する技術的なリソースの提供と、新機能の利用促進を目的としています。

## articles/ai-services/language-service/native-document-support/shared-access-signatures.md{#item-01eef1}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ ms.topic: how-to
 manager: nitinme
 ms.author: lajanuar
 author: laujan
-ms.date: 11/21/2024
+ms.date: 03/05/2025
 ---
 
 # SAS tokens for your storage containers
@@ -19,17 +19,15 @@ Learn to create user delegation, shared access signature (SAS) tokens, using the
 >
 > [Role-based access control (managed identities)](../concepts/role-based-access-control.md) provide an alternate method for granting access to your storage data without the need to include SAS tokens with your HTTP requests.
 >
-> * You can use managed identities to grant access to any resource that supports Microsoft Entra authentication, including your own applications.
+> * Using managed identities grants access to any resource that supports Microsoft Entra authentication, including your own applications.
 > * Using managed identities replaces the requirement for you to include shared access signature tokens (SAS) with your source and target URLs.
-> * There's no added cost to use managed identities in Azure.
+> * Using managed identities doesn't require an added cost in Azure.
 
 At a high level, here's how SAS tokens work:
 
 * Your application submits the SAS token to Azure Storage as part of a REST API request.
 
-* If the storage service verifies that the SAS is valid, the request is authorized.
-
-* If the SAS token is deemed invalid, the request is declined, and the error code 403 (Forbidden) is returned.
+* The storage service verifies that the SAS is valid and then the request is authorized. If the SAS token is deemed invalid, the request is declined, and the error code 403 (Forbidden) is returned.
 
 Azure Blob Storage offers three resource types:
 
@@ -41,7 +39,7 @@ Azure Blob Storage offers three resource types:
 >
 > * SAS tokens are used to grant permissions to storage resources, and should be protected in the same manner as an account key.
 >
-> * Operations that use SAS tokens should be performed only over an HTTPS connection, and SAS URIs should only be distributed on a secure connection such as HTTPS.
+> * Operations that use SAS tokens should be performed only over an HTTPS connection, and `SAS URI`s should only be distributed on a secure connection such as HTTPS.
 
 ## Prerequisites
 
@@ -80,9 +78,9 @@ Workflow: **Your storage account** → **containers** → **your container** →
     * Consider setting a longer duration period for the time you're using your storage account for Language Service operations.
     * The value of the expiry time is determined by whether you're using an **Account key** or **User delegation key** **Signing method**:
        * **Account key**: No imposed maximum time limit; however, best practices recommended that you configure an expiration policy to limit the interval and minimize compromise. [Configure an expiration policy for shared access signatures](/azure/storage/common/sas-expiration-policy).
-       * **User delegation key**: The value for the expiry time is a maximum of seven days from the creation of the SAS token. The SAS is invalid after the user delegation key expires, so a SAS with an expiry time of greater than seven days will still only be valid for seven days. For more information,*see* [Use Microsoft Entra credentials to secure a SAS](/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli#use-azure-ad-credentials-to-secure-a-sas).
+       * **User delegation key**: The value for the expiry time is a maximum of seven days from the creation of the SAS token. The SAS is invalid after the user delegation key expires, so a SAS with an expiry time of greater than seven days will still only be valid for seven days. For more information, *see* [Use Microsoft Entra credentials to secure a SAS](/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli#use-azure-ad-credentials-to-secure-a-sas).
 
-1. The **Allowed IP addresses** field is optional and specifies an IP address or a range of IP addresses from which to accept requests. If the request IP address doesn't match the IP address or address range specified on the SAS token, authorization fails. The IP address or a range of IP addresses must be public IPs, not private. For more information,*see*, [**Specify an IP address or IP range**](/rest/api/storageservices/create-account-sas#specify-an-ip-address-or-ip-range).
+1. The **Allowed IP addresses** field is optional and specifies an IP address or a range of IP addresses from which to accept requests. If the request IP address doesn't match the IP address or address range specified on the SAS token, authorization fails. The IP address or a range of IP addresses must be public IPs, not private. For more information, *see*, [**Specify an IP address or IP range**](/rest/api/storageservices/create-account-sas#specify-an-ip-address-or-ip-range).
 
 1. The **Allowed protocols** field is optional and specifies the protocol permitted for a request made with the SAS. The default value is HTTPS.
 
@@ -130,5 +128,5 @@ That's it! You learned how to create SAS tokens to authorize how clients access
 ## Next steps
 
 > [!div class="nextstepaction"]
-> [Learn more about native document support](use-native-documents.md "Learn how to process and analyze native documents.") [Learn more about granting access with SAS ](/azure/storage/common/storage-sas-overview "Grant limited access to Azure Storage resources using shared access SAS.")
+> [Learn more about native document support](overview.md "Learn how to process and analyze native documents.") [Learn more about granting access with SAS ](/azure/storage/common/storage-sas-overview "Grant limited access to Azure Storage resources using shared access SAS.")
 >
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SASトークンに関するドキュメントの修正"
}
```

### Explanation
この変更は、AzureのSAS（Shared Access Signature）トークンに関するドキュメントの軽微な更新を含んでいます。主な変更点として、更新日が2024年11月21日から2025年3月5日に変更されました。また、記述の明瞭さを向上させるためのテキストの修正が行われています。

具体的には、マネージドアイデンティティに関する説明が文を整えて明確化され、コストに関する内容も微調整されています。さらに、SASトークンの説明において、認証プロセスの流れが整理され、ステップごとの説明が簡潔になりました。

また、関連コンテンツのリンクが微細に変更され、「ネイティブドキュメントサポート」へのリンクが新しい概要ページに更新されています。これらの修正は、ドキュメントの可読性や正確性を向上させることを目的としており、ユーザーがSASトークンをより理解しやすくなるような技術的背景を提供しています。

## articles/ai-services/language-service/overview.md{#item-f138b4}

<details>
<summary>Diff</summary>
````diff
@@ -7,41 +7,41 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 02/10/2025
+ms.date: 03/05/2025
 ms.author: jboback
 ---
 
 # What is Azure AI Language?
 
-Azure AI Language is a cloud-based service that provides Natural Language Processing (NLP) features for understanding and analyzing text. Use this service to help build intelligent applications using the web-based Language Studio, REST APIs, and client libraries. 
+Azure AI Language is a cloud-based service that provides Natural Language Processing (NLP) features for understanding and analyzing text. Use this service to help build intelligent applications using the web-based Language Studio, REST APIs, and client libraries.
 
 ## Available features
 
-This Language service unifies the following previously available Azure AI services: Text Analytics, QnA Maker, and LUIS. If you need to migrate from these services, see [the migration section](#migrate-from-text-analytics-qna-maker-or-language-understanding-luis) below.
+This Language service unifies the following previously available Azure AI services: Text Analytics, QnA Maker, and LUIS. If you need to migrate from these services, see [the migration section](#migrate-from-text-analytics-qna-maker-or-language-understanding-luis).
 
 The Language service also provides several new features as well, which can either be:
 
-* Preconfigured, which means the AI models that the feature uses are not customizable. You just send your data, and use the feature's output in your applications.
-* Customizable, which means you'll train an AI model using our tools to fit your data specifically.
+* Preconfigured, which means the AI models that the feature uses aren't customizable. You just send your data, and use the feature's output in your applications.
+* Customizable, which means you train an AI model using our tools to fit your data specifically.
 
 > [!TIP]
-> Unsure which feature to use? See [Which Language service feature should I use?](#which-language-service-feature-should-i-use) to help you decide.
+> Unsure which feature to use? See [Which Language service feature should I use](#which-language-service-feature-should-i-use) to help you decide.
 
-[**Azure AI Foundry**](https://ai.azure.com) enables you to use most of the below service features without needing to write code.
+[**Azure AI Foundry**](https://ai.azure.com) enables you to use most of the following service features without needing to write code.
 
 ### Named Entity Recognition (NER)
 
 :::row:::
    :::column span="":::
-      :::image type="content" source="media/overview/named-entity-recognition.png" alt-text="A screenshot of named entity recognition in Azure AI Foundry."  lightbox="media/overview/named-entity-recognition.png":::
+      :::image type="content" source="media/overview/named-entity-recognition.png" alt-text="A screenshot of named entity recognition in Azure AI Foundry."lightbox="media/overview/named-entity-recognition.png":::
    :::column-end:::
    :::column span="":::
-      [Named entity recognition](./named-entity-recognition/overview.md) identifies different entries in text and categorizes them into pre-defined types.
+      [Named entity recognition](./named-entity-recognition/overview.md) identifies different entries in text and categorizes them into predefined types.
 
    :::column-end:::
 :::row-end:::
 
-### Personally identifying (PII) and health (PHI) information detection
+### Personal and health data information detection
 
 :::row:::
    :::column span="":::
@@ -73,7 +73,7 @@ The Language service also provides several new features as well, which can eithe
       :::image type="content" source="media/overview/sentiment-analysis.png" alt-text="A screenshot of sentiment analysis in Azure AI Foundry." lightbox="media/overview/sentiment-analysis.png":::
    :::column-end:::
    :::column span="":::
-      [Sentiment analysis and opinion mining](./sentiment-opinion-mining/overview.md) are preconfigured features that help you find out what people think of your brand or topic by mining text for clues about positive or negative sentiment, and can associate them with specific aspects of the text.
+      [Sentiment analysis and opinion mining](./sentiment-opinion-mining/overview.md) preconfigured features that help you understand public perception of your brand or topic. These features analyze text to identify positive or negative sentiments and can link them to specific elements within the text.
 
    :::column-end:::
 :::row-end:::
@@ -88,7 +88,7 @@ The Language service also provides several new features as well, which can eithe
    :::column-end:::
    :::column span="":::
       [Summarization](./summarization/overview.md) condenses information for text and conversations (chat and transcripts).
-      Text summarization generates a summary, supporting two approaches: Extractive summarization produces a summary by extracting salient sentences within the document along with the positioning information of these sentences, and abstractive summarization, which generates a summary with concise, coherent sentences or words that aren't verbatim extract sentences from the original document.  
+      Text summarization generates a summary, supporting two approaches: Extractive summarization creates a summary by selecting key sentences from the document and preserving their original positions. In contrast, abstractive summarization generates a summary by producing new, concise, and coherent sentences or phrases that aren't directly copied from the original document.
 Conversation summarization recaps and segments long meetings into timestamped chapters. Call center summarization summarizes customer issues and resolution.
    :::column-end:::
 :::row-end:::
@@ -111,7 +111,7 @@ Conversation summarization recaps and segments long meetings into timestamped ch
       :::image type="content" source="media/studio-examples/entity-linking.png" alt-text="A screenshot of an entity linking example." lightbox="media/studio-examples/entity-linking.png":::
    :::column-end:::
    :::column span="":::
-      [Entity linking](./entity-linking/overview.md) is a preconfigured feature that disambiguates the identity of entities (words or phrases) found in unstructured text and returns links to Wikipedia. 
+      [Entity linking](./entity-linking/overview.md) is a preconfigured feature that disambiguates the identity of entities (words or phrases) found in unstructured text and returns links to Wikipedia.
    :::column-end:::
 :::row-end:::
 
@@ -145,7 +145,7 @@ Conversation summarization recaps and segments long meetings into timestamped ch
       :::image type="content" source="media/studio-examples/custom-named-entity-recognition.png" alt-text="A screenshot of a custom NER example." lightbox="media/studio-examples/custom-named-entity-recognition.png":::
    :::column-end:::
    :::column span="":::
-      [Custom NER](custom-named-entity-recognition/overview.md) enables you to build custom AI models to extract custom entity categories (labels for words or phrases), using unstructured text that you provide. 
+      [Custom NER](custom-named-entity-recognition/overview.md) enables you to build custom AI models to extract custom entity categories (labels for words or phrases), using unstructured text that you provide.
    :::column-end:::
 :::row-end:::
 
@@ -180,48 +180,48 @@ Conversation summarization recaps and segments long meetings into timestamped ch
       :::image type="content" source="media/studio-examples/question-answering.png" alt-text="A screenshot of a question answering example." lightbox="media/studio-examples/question-answering.png":::
    :::column-end:::
    :::column span="":::
-      [Question answering](./question-answering/overview.md) is a custom feature that finds the most appropriate answer for inputs from your users, and is commonly used to build conversational client applications, such as social media applications, chat bots, and speech-enabled desktop applications. 
+      [Question answering](./question-answering/overview.md) is a custom feature that identifies the most suitable answer for user inputs. This feature is typically utilized to develop conversational client applications, including social media platforms, chat bots, and speech-enabled desktop applications.
 
    :::column-end:::
 :::row-end:::
 
 ## Which Language service feature should I use?
 
-This section will help you decide which Language service feature you should use for your application:
+This section helps you decide which Language service feature you should use for your application:
 
 |What do you want to do?  |Document format  |Your best solution  | Is this solution customizable?* |
 |---------|---------|---------|---------|
-| Detect and/or redact sensitive information such as PII and PHI. | Unstructured text, <br> transcribed conversations | [PII detection](./personally-identifiable-information/overview.md) | |
+| Detect and/or redact sensitive information such as `PII` and `PHI`. | Unstructured text, <br> transcribed conversations | [PII detection](./personally-identifiable-information/overview.md) | |
 | Extract categories of information without creating a custom model.     | Unstructured text         | The [preconfigured NER feature](./named-entity-recognition/overview.md) |       |
 | Extract categories of information using a model specific to your data. | Unstructured text | [Custom NER](./custom-named-entity-recognition/overview.md) | ✓ |
 |Extract main topics and important phrases.     | Unstructured text        | [Key phrase extraction](./key-phrase-extraction/overview.md) |   |
 | Determine the sentiment and opinions expressed in text. | Unstructured text | [Sentiment analysis and opinion mining](./sentiment-opinion-mining/overview.md) |  |
-| Summarize long chunks of text or conversations. | Unstructured text, <br> transcribed conversations. | [Summarization](./summarization/overview.md) | | 
-| Disambiguate entities and get links to Wikipedia. | Unstructured text | [Entity linking](./entity-linking/overview.md) | | 
+| Summarize long chunks of text or conversations. | Unstructured text, <br> transcribed conversations. | [Summarization](./summarization/overview.md) | |
+| Disambiguate entities and get links to Wikipedia. | Unstructured text | [Entity linking](./entity-linking/overview.md) | |
 | Classify documents into one or more categories. | Unstructured text | [Custom text classification](./custom-text-classification/overview.md) | ✓|
 | Extract medical information from clinical/medical documents, without building a model. | Unstructured text | [Text analytics for health](./text-analytics-for-health/overview.md) | |
 | Build a conversational application that responds to user inputs. | Unstructured user inputs | [Question answering](./question-answering/overview.md) | ✓ |
-| Detect the language that a text was written in. | Unstructured text | [Language detection](./language-detection/overview.md) | | 
+| Detect the language that a text was written in. | Unstructured text | [Language detection](./language-detection/overview.md) | |
 | Predict the intention of user inputs and extract information from them. | Unstructured user inputs | [Conversational language understanding](./conversational-language-understanding/overview.md) | ✓ |
-| Connect apps from conversational language understanding, LUIS, and question answering. | Unstructured user inputs | [Orchestration workflow](./orchestration-workflow/overview.md) | ✓ | 
+| Connect apps from conversational language understanding, LUIS, and question answering. | Unstructured user inputs | [Orchestration workflow](./orchestration-workflow/overview.md) | ✓ |
 
-\* If a feature is customizable, you can train an AI model using our tools to fit your data specifically. Otherwise a feature is preconfigured, meaning the AI models it uses cannot be changed. You just send your data, and use the feature's output in your applications.
+\* If a feature is customizable, you can train an AI model using our tools to fit your data specifically. Otherwise a feature is preconfigured, meaning the AI models it uses can't be changed. You just send your data, and use the feature's output in your applications.
 
 ## Migrate from Text Analytics, QnA Maker, or Language Understanding (LUIS)
 
-Azure AI Language unifies three individual language services in Azure AI services - Text Analytics, QnA Maker, and Language Understanding (LUIS). If you have been using these three services, you can easily migrate to the new Azure AI Language. For instructions see [Migrating to Azure AI Language](concepts/migrate.md).  
+Azure AI Language unifies three individual language services in Azure AI services - Text Analytics, QnA Maker, and Language Understanding (LUIS). If you have been using these three services, you can easily migrate to the new Azure AI Language. For instructions see [Migrating to Azure AI Language](concepts/migrate.md).
 
 ## Tutorials
 
-After you've had a chance to get started with the Language service, try our tutorials that show you how to solve various scenarios.
+After you get started with the Language service quickstarts, try our tutorials that show you how to solve various scenarios.
 
 * [Extract key phrases from text stored in Power BI](key-phrase-extraction/tutorials/integrate-power-bi.md)
-* [Use Power Automate to sort information in Microsoft Excel](named-entity-recognition/tutorials/extract-excel-information.md) 
+* [Use Power Automate to sort information in Microsoft Excel](named-entity-recognition/tutorials/extract-excel-information.md)
 * [Use Flask to translate text, analyze sentiment, and synthesize speech](/training/modules/python-flask-build-ai-web-app/)
 * [Use Azure AI services in canvas apps](/powerapps/maker/canvas-apps/cognitive-services-api?context=/azure/ai-services/language-service/context/context)
 * [Create an FAQ Bot](question-answering/tutorials/bot-service.md)
 
-## Additional code samples
+## Code samples
 
 You can find more code samples on GitHub for the following languages:
 
@@ -230,7 +230,7 @@ You can find more code samples on GitHub for the following languages:
 * [JavaScript](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/textanalytics/ai-text-analytics/samples)
 * [Python](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/textanalytics/azure-ai-textanalytics/samples)
 
-## Deploy on premises using Docker containers 
+## Deploy on premises using Docker containers
 Use Language service containers to deploy API features on-premises. These Docker containers enable you to bring the service closer to your data for compliance, security, or other operational reasons. The Language service offers the following containers:
 
 * [Sentiment analysis](sentiment-opinion-mining/how-to/use-containers.md)
@@ -240,9 +240,9 @@ Use Language service containers to deploy API features on-premises. These Docker
 * [Text Analytics for health](text-analytics-for-health/how-to/use-containers.md)
 * [Summarization](summarization/how-to/use-containers.md)
 
-## Responsible AI 
+## Responsible AI
 
-An AI system includes not only the technology, but also the people who will use it, the people who will be affected by it, and the environment in which it is deployed. Read the following articles to learn about responsible AI use and deployment in your systems:
+An AI system includes not only the technology, but also the people who use it, the people affected by it, and the deployment environment. Read the following articles to learn about responsible AI use and deployment in your systems:
 
 * [Transparency note for the Language service](/legal/cognitive-services/text-analytics/transparency-note)
 * [Integration and responsible use](/legal/cognitive-services/text-analytics/guidance-integration-responsible-use)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI 言語サービスの概要ドキュメントの修正"
}
```

### Explanation
この変更は、Azure AI言語サービスの概要ドキュメントに対する軽微な更新を含んでいます。主な変更点は、更新日が2025年2月10日から2025年3月5日に変更されたこと、文の表現を改善して読みやすくするためにいくつかの箇所で文言を修正したことです。

具体的には、提供される機能の説明や、ユーザーのためのヒントセクションの文が改善されており、理解しやすさが向上しています。また、サンプルコードやチュートリアルセクションに関する構成も見直され、より明確に情報が提示されています。

さらに、内容の一貫性を高めるために、いくつかの表現が変更され、特に専門用語やリンク先への記載において、整合性を持たせる努力がなされています。全体として、この更新はユーザーがサービスをより効果的に活用できるようにサポートすることを目的としています。

## articles/ai-services/language-service/personally-identifiable-information/how-to/redact-conversation-pii.md{#item-0d6332}

<details>
<summary>Diff</summary>
````diff
@@ -1,94 +1,90 @@
 ---
-title: How to detect Personally Identifiable Information (PII) in conversations.
+title: Identify and extract Personally Identifying Information (PII) from conversations
 titleSuffix: Azure AI services
-description: This article shows you how to extract PII from chat and spoken transcripts and redact identifiable information.
+description: This article shows you how to detect and redact Personally Identifying Information (PII) from speech, chat, and spoken-word transcriptions and call transcripts.
 #services: cognitive-services
 author: jboback
 manager: nitinme
 ms.service: azure-ai-language
-ms.custom:
-  - ignite-2024
 ms.topic: how-to
-ms.date: 11/04/2024
-ms.author: jboback
-ms.reviewer: bidishac
+ms.date: 03/05/2025
+ms.author: lajanuar
+ms.custom: language-service-pii
 ---
 
+# Detect and redact Personally Identifying Information in conversations
 
-# How to detect and redact Personally Identifying Information (PII) in conversations
-
-The Conversational PII feature can evaluate conversations to extract sensitive information (PII) in the content across several pre-defined categories and redact them. This API operates on both transcribed text (referenced as transcripts) and chats.
-For transcripts, the API also enables redaction of audio segments, which contains the PII information by providing the audio timing information for those audio segments.
+Azure AI Language conversation PII API analyzes audio discourse to identify and redact sensitive information (PII) using various predefined categories. This API works on both transcribed text (referred to as transcripts) and chats. For transcripts, it also facilitates the redaction of audio segments containing PII by providing the timing information for those segments.
 
 ## Determine how to process the data (optional)
 
 ### Specify the PII detection model
 
-By default, this feature uses the latest available AI model on your input. You can also configure your API requests to use a specific [model version](../concepts/model-lifecycle.md).
+By default, this feature uses the latest available AI model on your input. You can also configure your API requests to use a specific [model version](../../concepts/model-lifecycle.md).
 
 ### Language support
 
-See the [PII Language Support page](language-support.md) for more details. Currently the conversational PII GA model only supports the English language. The preview model and API support the [same list languages](../concepts/language-support.md) as the other Language services.
+For more information, *see* the [PII Language Support page](../language-support.md). Currently the conversational PII GA model only supports the English language. The preview model and API support the [same list languages](../../concepts/language-support.md) as the other Language services.
 
 ### Region support
 
 The conversational PII API supports all Azure regions supported by the Language service.
 
 ## Submitting data
 
-You can submit the input to the API as list of conversation items. Analysis is performed upon receipt of the request. Because the API is asynchronous, there may be a delay between sending an API request, and receiving the results. For information on the size and number of requests you can send per minute and second, see the data limits below.
+You can submit the input to the API as list of conversation items. Analysis is performed upon receipt of the request. Because the API is asynchronous, there may be a delay between sending an API request, and receiving the results. For information on the size and number of requests you can send per minute and second, see the following data limits.
 
-When using the async feature, the API results are available for 24 hours from the time the request was ingested, and is indicated in the response. After this time period, the results are purged and are no longer available for retrieval.
+When you use the async feature, the API results are available for 24 hours from the time the request was ingested, and is indicated in the response. After this time period, the results are purged and are no longer available for retrieval.
 
 When you submit data to conversational PII, you can send one conversation (chat or spoken) per request.
 
-The API attempts to detect all the [defined entity categories](concepts/conversations-entity-categories.md) for a given conversation input. If you want to specify which entities are detected and returned, use the optional `piiCategories` parameter with the appropriate entity categories.
+The API attempts to detect all the [defined entity categories](../concepts/conversations-entity-categories.md) for a given conversation input. If you want to specify which entities are detected and returned, use the optional `piiCategories` parameter with the appropriate entity categories.
 
-For spoken transcripts, the entities detected are returned on the `redactionSource` parameter value provided. Currently, the supported values for `redactionSource` are `text`, `lexical`, `itn`, and `maskedItn` (which maps to Speech to text REST API's `display`\\`displayText`, `lexical`, `itn` and `maskedItn` format respectively). Additionally, for the spoken transcript input, this API also provides audio timing information to empower audio redaction. For using the audioRedaction feature, use the optional `includeAudioRedaction` flag with `true` value. The audio redaction is performed based on the lexical input format.
+For spoken transcripts, the entities detected are returned on the `redactionSource` parameter value provided. Currently, the supported values for `redactionSource` are `text`, `lexical`, `itn`, and `maskedItn` (which maps to Speech to text REST API's `display`\\`displayText`, `lexical`, `itn`, and `maskedItn` format respectively). Additionally, for the spoken transcript input, this API also provides audio timing information to empower audio redaction. For using the audioRedaction feature, use the optional `includeAudioRedaction` flag with `true` value. The audio redaction is performed based on the lexical input format.
 
 > [!NOTE]
 > Conversation PII now supports 40,000 characters as document size.
 
 
 ## Getting PII results
 
-When you get results from PII detection, you can stream the results to an application or save the output to a file on the local system. The API response includes [recognized entities](concepts/conversations-entity-categories.md), including their categories and subcategories, and confidence scores. The text string with the PII entities redacted is also returned.
+When you get results from PII detection, you can stream the results to an application or save the output to a file on the local system. The API response includes [recognized entities](../concepts/conversations-entity-categories.md), including their categories and subcategories, and confidence scores. The text string with the PII entities redacted is also returned.
 
 ## Examples
 
 # [Client libraries (Azure SDK)](#tab/client-libraries)
 
 1. Go to your resource overview page in the [Azure portal](https://portal.azure.com/#home)
 
-2. From the menu on the left side, select **Keys and Endpoint**. You'll need one of the keys and the endpoint to authenticate your API requests.
+2. From the menu on the left side, select **Keys and Endpoint**. You need one of the keys and the endpoint to authenticate your API requests.
 
 3. Download and install the client library package for your language of choice:
-    
+
     |Language  |Package version  |
     |---------|---------|
     |.NET     | [1.0.0](https://www.nuget.org/packages/Azure.AI.Language.Conversations/1.0.0)        |
     |Python     | [1.0.0](https://pypi.org/project/azure-ai-language-conversations/1.1.0b2)         |
-    
-4. See the following reference documentation for more information on the client, and return object:
-    
+
+4. For more information on the client and return object, *see* the following reference documentation:
+
     * [C#](/dotnet/api/azure.ai.language.conversations)
     * [Python](/python/api/azure-ai-language-conversations/azure.ai.language.conversations.aio)
-    
+
 # [REST API](#tab/rest-api)
 
 ## Redaction Policy (version 2024-11-15-preview only)
 
-In version 2024-11-15-preview, you're able to define the `redactionPolicy` parameter to reflect the redaction policy to be used when redacting the document in the response. The policy field supports 3 policy types:
+In version 2024-11-15-preview, you're able to define the `redactionPolicy` parameter to reflect the redaction policy to be used when redacting the document in the response. The policy field supports three policy types:
 
-- `noMask` 
-- `characterMask` (default) 
-- `entityMask` 
+- `noMask`
+- `characterMask` (default)
+- `entityMask`
 
-The `noMask` policy allows the user to return the response without the `redactedText` field. 
+The `noMask` policy allows the user to return the response without the `redactedText` field.
 
-The `characterMask` policy allows the `redactedText` to be masked with a character, preserving the length and offset of the original text. This is the existing behavior.
+The `characterMask` policy allows the `redactedText` to be masked with a character, preserving the length and offset of the original text. This behavior is the existing expectation.
 
-There is also an optional field called `redactionCharacter` where you can input the character to be used in redaction if you're using the `characterMask` policy 
+There's also an optional field called `redactionCharacter` where you can input the character to be used in redaction if you're using the `characterMask` policy
 
 The `entityMask` policy allows you to mask the detected PII entity text with the detected entity type
 
@@ -100,63 +96,63 @@ curl -i -X POST https://your-language-endpoint-here/language/analyze-conversatio
 -H "Ocp-Apim-Subscription-Key: your-key-here" \
 -d \
 '
-{ 
-    "displayName": "Analyze conversations from xxx", 
-    "analysisInput": { 
-        "conversations": [ 
-            { 
-                "id": "23611680-c4eb-4705-adef-4aa1c17507b5", 
-                "language": "en", 
-                "modality": "text", 
-                "conversationItems": [ 
-                    { 
-                        "participantId": "agent_1", 
-                        "id": "1", 
-                        "text": "Good morning." 
-                    }, 
-                    { 
-                        "participantId": "agent_1", 
-                        "id": "2", 
-                        "text": "Can I have your name?" 
-                    }, 
-                    { 
-                        "participantId": "customer_1", 
-                        "id": "3", 
-                        "text": "Sure that is John Doe." 
-                    } 
-                ] 
-            } 
-        ] 
-    }, 
-    "tasks": [ 
-        { 
-            "taskName": "analyze 1", 
-            "kind": "ConversationalPIITask", 
-            "parameters": { 
-                "modelVersion": "2023-04-15-preview", 
-                “redactionCharacter” 
-                "redactionPolicy": { 
-                    "policyKind": "characterMask", 
-                    //characterMask|entityMask|noMask 
-                    "redactionCharacter": "*" 
-                } 
-            } 
-        } 
-    ] 
-} 
+{
+    "displayName": "Analyze conversations from xxx",
+    "analysisInput": {
+        "conversations": [
+            {
+                "id": "23611680-c4eb-4705-adef-4aa1c17507b5",
+                "language": "en",
+                "modality": "text",
+                "conversationItems": [
+                    {
+                        "participantId": "agent_1",
+                        "id": "1",
+                        "text": "Good morning."
+                    },
+                    {
+                        "participantId": "agent_1",
+                        "id": "2",
+                        "text": "Can I have your name?"
+                    },
+                    {
+                        "participantId": "customer_1",
+                        "id": "3",
+                        "text": "Sure that is John Doe."
+                    }
+                ]
+            }
+        ]
+    },
+    "tasks": [
+        {
+            "taskName": "analyze 1",
+            "kind": "ConversationalPIITask",
+            "parameters": {
+                "modelVersion": "2023-04-15-preview",
+                "redactionCharacter"
+                "redactionPolicy": {
+                    "policyKind": "characterMask",
+                    //characterMask|entityMask|noMask
+                    "redactionCharacter": "*"
+                }
+            }
+        }
+    ]
+}
 `
 ```
 
 ## Submit transcripts using speech to text
 
-Use the following example if you have conversations transcribed using the Speech service's [speech to text](../../Speech-Service/speech-to-text.md) feature:
+Use the following example if you have conversations transcribed using the Speech service's [speech to text](../../../Speech-Service/speech-to-text.md) feature:
 
 ```bash
 curl -i -X POST https://your-language-endpoint-here/language/analyze-conversations/jobs?api-version=2024-05-01 \
 -H "Content-Type: application/json" \
 -H "Ocp-Apim-Subscription-Key: your-key-here" \
 -d \
-' 
+'
 {
     "displayName": "Analyze conversations from xxx",
     "analysisInput": {
@@ -287,7 +283,7 @@ curl -i -X POST https://your-language-endpoint-here/language/analyze-conversatio
 -H "Content-Type: application/json" \
 -H "Ocp-Apim-Subscription-Key: your-key-here" \
 -d \
-' 
+'
 {
     "displayName": "Analyze conversations from xxx",
     "analysisInput": {
@@ -350,4 +346,4 @@ curl -X GET    https://your-language-endpoint/language/analyze-conversations/job
 
 ## Service and data limits
 
-[!INCLUDE [service limits article](../includes/service-limits-link.md)]
+[!INCLUDE [service limits article](../../includes/service-limits-link.md)]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "会話からの個人情報の検出と削除に関するドキュメントのリネームと修正"
}
```

### Explanation
この変更は、「会話からの個人情報を検出して削除する方法」に関するドキュメントのタイトルを変更し、内容の一部を更新したものです。もともとのタイトルは「会話における個人情報の検出方法」で、新しいタイトルは「会話からの個人情報を特定して抽出する」となっています。

ドキュメントの内容には、個人を特定できる情報（PII）の検出と削除に関する詳細な手順が含まれています。具体的には、音声、チャット、そして音声転写された内容からのPIIの検出および赤actionに関する説明が更新され、より明確かつ具体的な表現が使われています。

追加された内容では、APIの使用方法や言語サポートについての情報が強化され、ユーザーが迅速に理解できるよう配慮されています。また、現在のモデルや、APIの入力フォーマット、エラー処理に関する情報も明確に記載されています。

この変更全体は、ユーザーがAzure AIの会話PII機能をより効果的に利用できるように、ドキュメントを整備したことを示しています。

## articles/ai-services/language-service/personally-identifiable-information/how-to/redact-document-pii.md{#item-5509ee}

<details>
<summary>Diff</summary>
````diff
@@ -1,38 +1,31 @@
 ---
-title: Native document support for Azure AI Language (preview)
+title: Identify and extract Personally Identifying Information (PII) from native documents
 titleSuffix: Azure AI services
-description: How to use native document with Azure AI Languages Personally Identifiable Information and Summarization capabilities.
-author: laujan
+description: This article shows you how to redact Personally Identifying Information (PII) from native documents.
+#services: cognitive-services
+author: jboback
 manager: nitinme
 ms.service: azure-ai-language
-ms.custom:
-  - ignite-2024
 ms.topic: how-to
-ms.date: 11/19/2024
+ms.date: 03/05/2025
 ms.author: lajanuar
+ms.custom: language-service-pii
 ---
 
-<!-- markdownlint-disable MD033 -->
-<!-- markdownlint-disable MD051 -->
-<!-- markdownlint-disable MD024 -->
-<!-- markdownlint-disable MD036 -->
-<!-- markdownlint-disable MD049 -->
-<!-- markdownlint-disable MD001 -->
-
-# Native document support for Azure AI Language (preview)
+# Detect and redact Personally Identifying Information in native documents (preview)
 
 > [!IMPORTANT]
 >
 > * Azure AI Language public preview releases provide early access to features that are in active development.
-> * Features, approaches, and processes may change, prior to General Availability (GA), based on user feedback.
+> * Features, approaches, and processes may change, before General Availability (GA), based on user feedback.
 
 Azure AI Language is a cloud-based service that applies Natural Language Processing (NLP) features to text-based data. The native document support capability enables you to send API requests asynchronously, using an HTTP POST request body to send your data and HTTP GET request query string to retrieve the status results. Your processed documents are located in your Azure Blob Storage target container.
 
 A native document refers to the file format used to create the original document such as Microsoft Word (docx) or a portable document file (pdf). Native document support eliminates the need for text preprocessing before using Azure AI Language resource capabilities. Currently, native document support is available for the following capabilities:
 
-* [Personally Identifiable Information (PII)](../personally-identifiable-information/overview.md). The PII detection feature can identify, categorize, and redact sensitive information in unstructured text. The `PiiEntityRecognition` API supports native document processing.
+* [Personally Identifiable Information (PII)](../../personally-identifiable-information/overview.md). The PII detection feature can identify, categorize, and redact sensitive information in unstructured text. The `PiiEntityRecognition` API supports native document processing.
 
-* [Document summarization](../summarization/overview.md). Document summarization uses natural language processing to generate extractive (salient sentence extraction) or abstractive (contextual word extraction) summaries for documents. Both `AbstractiveSummarization` and `ExtractiveSummarization` APIs support native document processing.
+* [Document summarization](../../summarization/overview.md). Document summarization uses natural language processing to generate extractive (salient sentence extraction) or abstractive (contextual word extraction) summaries for documents. Both `AbstractiveSummarization` and `ExtractiveSummarization` APIs support native document processing.
 
 ## Supported document formats
 
@@ -68,7 +61,7 @@ A native document refers to the file format used to create the original document
 * For this project, we use the cURL command line tool to make REST API calls.
 
     > [!NOTE]
-    > The cURL package is pre-installed on most Windows 10 and Windows 11 and most macOS and Linux distributions. You can check the package version with the following commands:
+    > The cURL package is preinstalled on most Windows 10 and Windows 11 and most macOS and Linux distributions. You can check the package version with the following commands:
     > Windows: `curl.exe -V`
     > macOS `curl -V`
     > Linux: `curl --version`
@@ -91,9 +84,9 @@ A native document refers to the file format used to create the original document
 
   1. **Subscription**. Select one of your available Azure subscriptions.
 
-  1. **Resource Group**. You can create a new resource group or add your resource to a pre-existing resource group that shares the same lifecycle, permissions, and policies.
+  1. **Resource Group**. You can create a new resource group or add your resource to a preexisting resource group that shares the same lifecycle, permissions, and policies.
 
-  1. **Resource Region**. Choose **Global** unless your business or application requires a specific region. If you're planning on using a [system-assigned managed identity (RBAC)](../concepts/role-based-access-control.md) for authentication, choose a **geographic** region like **West US**.
+  1. **Resource Region**. Choose **Global** unless your business or application requires a specific region. If you're planning on using a [system-assigned managed identity](../../concepts/role-based-access-control.md) for authentication, choose a **geographic** region like **West US**.
 
   1. **Name**. Enter the name you chose for your resource. The name you choose must be unique within Azure.
 
@@ -126,13 +119,13 @@ Requests to the Language service require a read-only key and custom endpoint to
 
 Your Language resource needs granted access to your storage account before it can create, read, or delete blobs. There are two primary methods you can use to grant access to your storage data:
 
-* [**Shared access signature (SAS) tokens**](shared-access-signatures.md). User delegation SAS tokens are secured with Microsoft Entra credentials. SAS tokens provide secure, delegated access to resources in your Azure storage account.
+* [**Shared access signature (SAS) tokens**](../../native-document-support/shared-access-signatures.md). User delegation SAS tokens are secured with Microsoft Entra credentials. SAS tokens provide secure, delegated access to resources in your Azure storage account.
 
-* [**Managed identity role-based access control (RBAC)**](managed-identities.md). Managed identities for Azure resources are service principals that create a Microsoft Entra identity and specific permissions for Azure managed resources.
+* [**Managed identity role-based access control (RBAC)**](../../native-document-support/managed-identities.md). Managed identities for Azure resources are service principals that create a Microsoft Entra identity and specific permissions for Azure managed resources.
 
 For this project, we authenticate access to the `source location` and `target location` URLs with Shared Access Signature (SAS) tokens appended as query strings. Each token is assigned to a specific blob (file).
 
-:::image type="content" source="media/sas-url-token.png" alt-text="Screenshot of a storage url with SAS token appended.":::
+:::image type="content" source="../../native-document-support/media/sas-url-token.png" alt-text="Screenshot of a storage url with SAS token appended.":::
 
 * Your **source** container or blob must designate **read** and **list** access.
 * Your **target** container or blob must designate **write** and **list** access.
@@ -152,8 +145,6 @@ For this project, we authenticate access to the `source location` and `target lo
 
 The following cURL commands are executed from a BASH shell. Edit these commands with your own resource name, resource key, and JSON values. Try analyzing native documents by selecting the `Personally Identifiable Information (PII)` or `Document Summarization` code sample project:
 
-### [Personally Identifiable Information (PII)](#tab/pii)
-
 ### PII Sample document
 
 For this quickstart, you need a **source document** uploaded to your **source container**. You can download our [Microsoft Word sample document](https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/Language/native-document-pii.docx) or [Adobe PDF](https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl//Language/native-document-pii.pdf) for this project. The source language is English.
@@ -248,7 +239,7 @@ For this quickstart, you need a **source document** uploaded to your **source co
 
 You receive a 202 (Success) response that includes a read-only Operation-Location header. The value of this header contains a **jobId** that can be queried to get the status of the asynchronous operation and retrieve the results using a **GET** request:
 
-  :::image type="content" source="media/operation-location-result-id.png" alt-text="Screenshot showing the operation-location value in the POST response.":::
+  :::image type="content" source="../../native-document-support/media/operation-location-result-id.png" alt-text="Screenshot showing the operation-location value in the POST response.":::
 
 ### Get analyze results (GET request)
 
@@ -330,160 +321,6 @@ You receive a 200 (Success) response with JSON output. The **status** field indi
 }
 ```
 
-### [Document Summarization](#tab/summarization)
-
-### Summarization sample document
-
-For this project, you need a **source document** uploaded to your **source container**. You can download our [Microsoft Word sample document](https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/Language/native-document-summarization.docx) or [Adobe PDF](https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/Language/native-document-summarization.pdf) for this quickstart. The source language is English.
-
-### Build the POST request
-
-1. Using your preferred editor or IDE, create a new directory for your app named `native-document`.
-1. Create a new json file called **document-summarization.json** in your **native-document** directory.
-
-1. Copy and paste the Document Summarization **request sample** into your `document-summarization.json` file. Replace **`{your-source-container-SAS-URL}`** and **`{your-target-container-SAS-URL}`** with values from your Azure portal Storage account containers instance:
-
-  ***Request sample***
-
-  ```json
-  {
-  "tasks": [
-    {
-      "kind": "ExtractiveSummarization",
-      "parameters": {
-        "sentenceCount": 6
-      }
-    }
-  ],
-  "analysisInput": {
-    "documents": [
-      {
-        "source": {
-          "location": "{your-source-blob-SAS-URL}"
-        },
-        "targets": {
-          "location": "{your-target-container-SAS-URL}"
-        }
-      }
-    ]
-  }
-}
-```
-
-### Run the POST request
-
-Before you run the **POST** request, replace `{your-language-resource-endpoint}` and `{your-key}` with the endpoint value from your Azure portal Language resource instance.
-
-  > [!IMPORTANT]
-  > Remember to remove the key from your code when you're done, and never post it publicly. For production, use a secure way of storing and accessing your credentials like [Azure Key Vault](/azure/key-vault/general/overview). For more information, *see* Azure AI services [security](/azure/ai-services/security-features).
-
-  ***PowerShell***
-
-  ```powershell
-   cmd /c curl "{your-language-resource-endpoint}/language/analyze-documents/jobs?api-version=2024-11-15-preview" -i -X POST --header "Content-Type: application/json" --header "Ocp-Apim-Subscription-Key: {your-key}" --data "@document-summarization.json"
-  ```
-
-  ***command prompt / terminal***
-
-  ```bash
-  curl -v -X POST "{your-language-resource-endpoint}/language/analyze-documents/jobs?api-version=2024-11-15-preview" --header "Content-Type: application/json" --header "Ocp-Apim-Subscription-Key: {your-key}" --data "@document-summarization.json"
-  ```
-
-Here's a sample response:
-
-   ```http
-   HTTP/1.1 202 Accepted
-   Content-Length: 0
-   operation-location: https://{your-language-resource-endpoint}/language/analyze-documents/jobs/f1cc29ff-9738-42ea-afa5-98d2d3cabf94?api-version=2024-11-15-preview
-   apim-request-id: e7d6fa0c-0efd-416a-8b1e-1cd9287f5f81
-   x-ms-region: West US 2
-   Date: Thu, 25 Jan 2024 15:12:32 GMT
-   ```
-
-### POST response (jobId)
-
-You receive a 202 (Success) response that includes a read-only Operation-Location header. The value of this header contains a jobId that can be queried to get the status of the asynchronous operation and retrieve the results using a GET request:
-
-  :::image type="content" source="media/operation-location-result-id.png" alt-text="Screenshot showing the operation-location value in the POST response.":::
-
-### Get analyze results (GET request)
-
-1. After your successful **POST** request, poll the operation-location header returned in the POST request to view the processed data.
-
-1. Here's the structure of the **GET** request:
-
-   ```bash
-   GET {cognitive-service-endpoint}/language/analyze-documents/jobs/{jobId}?api-version=2024-11-15-preview
-   ```
-
-1. Before you run the command, make these changes:
-
-    * Replace {**jobId**} with the Operation-Location header from the POST response.
-
-    * Replace {**your-language-resource-endpoint**} and {**your-key**} with the values from your Language service instance in the Azure portal.
-
-### Get request
-
-```powershell
-    cmd /c curl "{your-language-resource-endpoint}/language/analyze-documents/jobs/{jobId}?api-version=2024-11-15-preview" -i -X GET --header "Content-Type: application/json" --header "Ocp-Apim-Subscription-Key: {your-key}"
-```
-
-```bash
-    curl -v -X GET "{your-language-resource-endpoint}/language/analyze-documents/jobs/{jobId}?api-version=2024-11-15-preview" --header "Content-Type: application/json" --header "Ocp-Apim-Subscription-Key: {your-key}"
-```
-
-#### Examine the response
-
-You receive a 200 (Success) response with JSON output. The **status** field indicates the result of the operation. If the operation isn't complete, the value of **status** is "running" or "notStarted", and you should call the API again, either manually or through a script. We recommend an interval of one second or more between calls.
-
-#### Sample response
-
-```json
-{
-  "jobId": "f1cc29ff-9738-42ea-afa5-98d2d3cabf94",
-  "lastUpdatedDateTime": "2024-01-24T13:17:58Z",
-  "createdDateTime": "2024-01-24T13:17:47Z",
-  "expirationDateTime": "2024-01-25T13:17:47Z",
-  "status": "succeeded",
-  "errors": [],
-  "tasks": {
-    "completed": 1,
-    "failed": 0,
-    "inProgress": 0,
-    "total": 1,
-    "items": [
-      {
-        "kind": "ExtractiveSummarizationLROResults",
-        "lastUpdateDateTime": "2024-01-24T13:17:58.33934Z",
-        "status": "succeeded",
-        "results": {
-          "documents": [
-            {
-              "id": "doc_0",
-              "source": {
-                "kind": "AzureBlob",
-                "location": "https://myaccount.blob.core.windows.net/sample-input/input.pdf"
-              },
-              "targets": [
-                {
-                  "kind": "AzureBlob",
-                  "location": "https://myaccount.blob.core.windows.net/sample-output/df6611a3-fe74-44f8-b8d4-58ac7491cb13/ExtractiveSummarization-0001/input.result.json"
-                }
-              ],
-              "warnings": []
-            }
-          ],
-          "errors": [],
-          "modelVersion": "2023-02-01-preview"
-        }
-      }
-    ]
-  }
-}
-```
-
----
-
 ***Upon successful completion***:
 
 * The analyzed documents can be found in your target container.
@@ -494,10 +331,10 @@ You receive a 200 (Success) response with JSON output. The **status** field indi
 
 If you want to clean up and remove an Azure AI services subscription, you can delete the resource or resource group. Deleting the resource group also deletes any other resources associated with it.
 
-* [Azure portal](../../multi-service-resource.md?pivots=azportal#clean-up-resources)
-* [Azure CLI](../../multi-service-resource.md?pivots=azcli#clean-up-resources)
+* [Azure portal](../../../multi-service-resource.md?pivots=azportal#clean-up-resources)
+* [Azure CLI](../../../multi-service-resource.md?pivots=azcli#clean-up-resources)
 
 ## Next steps
 
 > [!div class="nextstepaction"]
-> [PII detection overview](../personally-identifiable-information/overview.md "Learn more about Personally Identifiable Information detection.") [Document Summarization overview](../summarization/overview.md "Learn more about automatic document summarization.")
+> [PII detection overview](../overview.md "Learn more about Personally Identifiable Information detection.")
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ネイティブドキュメントから個人情報を特定・抽出するドキュメントのリネームと修正"
}
```

### Explanation
この変更は、「ネイティブドキュメントを使用する」方法に関するドキュメントのタイトルを変更し、内容を更新したものです。もともとのタイトルは「Azure AI Languageのネイティブドキュメントサポート (プレビュー)」であり、新しいタイトルは「ネイティブドキュメントから個人情報を特定・抽出する」となっています。

ドキュメントの内容は、ネイティブドキュメントから個人識別情報（PII）を削除する方法に関する具体的な手順を提供することを目的としています。性に関する情報を特定し、カテゴライズして赤actionする機能について詳しく説明しており、APIの利用方法や対応フォーマットについても強調されています。

また、内容の一部には、指定された文書フォーマット（例：Microsoft WordやPDF）でネイティブドキュメントをサポートすることから、Azure AI Languageの機能を効率的に活用できる点が明記されています。他のセクションでは、cURLコマンドを使用してREST APIを呼び出すための具体的な手順や注意事項が更新されており、特に認証方法についての説明が明確になっています。

全体的に、この変更はユーザーがAzure AIの機能をより効果的に活用できるようにドキュメントを整理し、理解を促進することを目的としています。

## articles/ai-services/language-service/personally-identifiable-information/how-to/redact-text-pii.md{#item-9e48af}

<details>
<summary>Diff</summary>
````diff
@@ -1,36 +1,35 @@
 ---
-title: How to detect Personally Identifiable Information (PII)
+title: Identify and extract Personally Identifying Information (PII) from text
 titleSuffix: Azure AI services
-description: This article will show you how to extract PII and health information (PHI) from text and detect identifiable information.
+description: This article shows you how to identify, extract and redact Personally Identifying Information (PII) from text.
 #services: cognitive-services
 author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 11/04/2024
-ms.author: jboback
-ms.custom: language-service-pii, ignite-2024
+ms.date: 03/05/2025
+ms.author: lajanuar
+ms.custom: language-service-pii
 ---
 
+# Detect and redact Personally Identifying Information in text
 
-# How to detect and redact Personally Identifying Information (PII)
-
-The PII feature can evaluate unstructured text, extract, and redact sensitive information (PII) and health information (PHI) in text across several [predefined categories](concepts/entity-categories.md).
+Azure AI Language is a cloud-based service that applies Natural Language Processing (NLP) features to text-based data. The PII feature can evaluate unstructured text, extract, and redact sensitive information (PII) and health information (PHI) in text across several [predefined categories](../concepts/entity-categories.md).
 
 
 ## Development options
 
-[!INCLUDE [development options](./includes/development-options.md)]
+[!INCLUDE [development options](../includes/development-options.md)]
 
 ## Determine how to process the data (optional)
 
 ### Specify the PII detection model
 
-By default, this feature uses the latest available AI model on your text. You can also configure your API requests to use a specific [model version](../concepts/model-lifecycle.md).
+By default, this feature uses the latest available AI model on your text. You can also configure your API requests to use a specific [model version](../../concepts/model-lifecycle.md).
 
 ### Input languages
 
-When you submit input text to be processed, you can specify which of [the supported languages](language-support.md) they're written in. If you don't specify a language, extraction defaults to English. The API may return offsets in the response to support different [multilingual and emoji encodings](../concepts/multilingual-emoji-support.md). 
+When you submit input text to be processed, you can specify which of [the supported languages](../language-support.md) they're written in. If you don't specify a language, extraction defaults to English. The API may return offsets in the response to support different [multilingual and emoji encodings](../../concepts/multilingual-emoji-support.md). 
 
 ### Redaction Policy (version 2024-11-5-preview only)
 In version `2024-11-5-preview`, you're able to define the `redactionPolicy` parameter to reflect the redaction policy to be used when redacting text. The policy field supports three policy types:
@@ -39,23 +38,23 @@ In version `2024-11-5-preview`, you're able to define the `redactionPolicy` para
 - `MaskWithCharacter` (default) 
 - `MaskWithEntityType` 
 
-The `DoNotRedact` policy allows the user to return the response without the `redactedText` field, that is, “John Doe received a call from 424-878-9192”. 
+The `DoNotRedact` policy allows the user to return the response without the `redactedText` field, that is, "John Doe received a call from 424-878-9192". 
 
-The `MaskWithRedactionCharacter` policy allows the `redactedText` to be masked with a character (such as "*"), preserving the length and offset of the original text, that is, “******** received a call from ************”. This is the existing behavior.
+The `MaskWithRedactionCharacter` policy allows the `redactedText` to be masked with a character (such as "*"), preserving the length and offset of the original text, that is, "******** received a call from ************". This is the existing behavior.
 
 There's also an optional field called `redactionCharacter` where you can input the character to be used in redaction if you're using the `MaskWithCharacter` policy 
 
-The `MaskWithEntityType` policy allows you to mask the detected PII entity text with the detected entity type, that is, “[PERSON_1] received a call from [PHONENUMBER_1]”. 
+The `MaskWithEntityType` policy allows you to mask the detected PII entity text with the detected entity type, that is, "[PERSON_1] received a call from [PHONENUMBER_1]". 
 
 ## Submitting data
 
 Analysis is performed upon receipt of the request. Using the PII detection feature synchronously is stateless. No data is stored in your account, and results are returned immediately in the response.
 
-[!INCLUDE [asynchronous-result-availability](../includes/async-result-availability.md)]
+[!INCLUDE [asynchronous-result-availability](../../includes/async-result-availability.md)]
 
 ## Select which entities to be returned
 
-The API attempts to detect the [defined entity categories](concepts/entity-categories.md) for a given input text language. If you want to specify which entities are detected and returned, use the optional `piiCategories` parameter with the appropriate entity categories. This parameter can also let you detect entities that aren't enabled by default for your input text language. The following example would detect only `Person`. You can specify one or more [entity types](concepts/entity-categories.md) to be returned.
+The API attempts to detect the [defined entity categories](../concepts/entity-categories.md) for a given input text language. If you want to specify which entities are detected and returned, use the optional `piiCategories` parameter with the appropriate entity categories. This parameter can also let you detect entities that aren't enabled by default for your input text language. The following example would detect only `Person`. You can specify one or more [entity types](../concepts/entity-categories.md) to be returned.
 
 > [!TIP]
 > If you don't include `default` when specifying entity categories, The API only returns the entity categories you specify.
@@ -130,12 +129,12 @@ The API attempts to detect the [defined entity categories](concepts/entity-categ
 
 ## Getting PII results
 
-When you get results from PII detection, you can stream the results to an application or save the output to a file on the local system. The API response includes [recognized entities](concepts/entity-categories.md), including their categories and subcategories, and confidence scores. The text string with the PII entities redacted is also returned.
+When you get results from PII detection, you can stream the results to an application or save the output to a file on the local system. The API response includes [recognized entities](../concepts/entity-categories.md), including their categories and subcategories, and confidence scores. The text string with the PII entities redacted is also returned.
 
 ## Service and data limits
 
-[!INCLUDE [service limits article](../includes/service-limits-link.md)]
+[!INCLUDE [service limits article](../../includes/service-limits-link.md)]
 
 ## Next steps
 
-[Personally Identifying Information (PII) overview](overview.md)
+[Personally Identifying Information (PII) overview](../overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキストからの個人情報特定・抽出方法に関するドキュメントのリネームと修正"
}
```

### Explanation
この変更は、「個人識別情報（PII）の検出方法」に関するドキュメントのタイトルを更新し、内容を修正したものです。元のタイトルは「個人識別情報（PII）を検出する方法」で、新しいタイトルは「テキストからの個人識別情報（PII）を特定・抽出する」となっています。

ドキュメントには、テキストから個人情報を特定、抽出、赤actionする方法についての詳細が含まれています。特に、本記事では自然言語処理（NLP）的手法を用いて非構造化テキストを評価し、PIIや健康情報（PHI）を抽出・削除する機能が強調されています。

内容の更新には、PII検出モデルの指定、処理言語、データの送信方法に関するオプション、赤actionポリシーなどの情報が含まれ、よりユーザーが理解しやすくなっている点が目立ちます。また、非同期結果の可用性についての詳細も載せられており、AIを使ったテキスト処理の実際の利用シーンでの設計や配慮が反映されています。

全体として、この改訂はAzureのAI機能を使用する際の実用的なガイドを提供し、ユーザーがそのプロセスをより効果的に理解し、順応できるような内容となっています。

## articles/ai-services/language-service/personally-identifiable-information/overview.md{#item-8a6932}

<details>
<summary>Diff</summary>
````diff
@@ -7,52 +7,108 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 09/27/2024
+ms.date: 03/05/2025
 ms.author: jboback
-ms.custom: language-service-pii, build-2024, ignite-2024
+ms.custom: language-service-pii
 ---
 
-# What is Personally Identifiable Information (PII) detection in Azure AI Language?
+# What is Azure AI Language Personally Identifiable Information (PII) detection?
 
-PII detection is one of the features offered by [Azure AI Language](../overview.md), a collection of machine learning and AI algorithms in the cloud for developing intelligent applications that involve written language. The PII detection feature can **identify, categorize, and redact** sensitive information in unstructured text. For example: phone numbers, email addresses, and forms of identification. Azure AI Language supports general text PII redaction, as well as [Conversational PII](how-to-call-for-conversations.md), a specialized model for handling speech transcriptions and the more informal, conversational tone of meeting and call transcripts. The service also supports [Native Document PII redaction](#native-document-support), where the input and output are structured document files.
+Azure AI Language Personally Identifiable Information (PII) detection is a feature offered by [Azure AI Language](../overview.md). The PII detection service is a cloud-based API that utilizes machine learning and AI algorithms to help you develop intelligent applications with advanced natural language understanding. Azure AI Language PII detection uses Named Entity Recognition (NER) to **identify and redact** sensitive information from input data. The service classifies sensitive personal data into predefined categories. These categories include phone numbers, email addresses, and identification documents. This classification helps to efficiently detect and eliminate such information.
+
+> [!TIP]
+> Try PII detection [in Azure AI Foundry portal](https://ai.azure.com/explore/language). There you can [utilize a currently existing Language Studio resource or create a new Azure AI Foundry resource](../../../ai-studio/ai-services/connect-ai-services.md).
 
 ## What's new
 
-The Text PII and Conversational PII detection preview API (version `2024-11-15-preview`) now supports the option to mask detected sensitive entities with a label beyond just redaction characters. Customers have the option to specify if personally identifiable information content such as names and phone numbers, i.e. `"John Doe received a call from 424-878-9192"`, are masked with a redaction character, i.e. `"******** received a call from ************"`, or masked with an entity label, i.e. `"[PERSON_1] received a call from [PHONENUMBER_1]"`. More on how to specify the redaction policy style for your outputs can be found in our [how-to guides](how-to-call.md). 
+The Text PII and Conversational PII detection preview API (version `2024-11-15-preview`) now supports the option to mask detected sensitive entities with a label beyond just redaction characters. Customers can specify if personal data content such as names and phone numbers, that is, `"John Doe received a call from 424-878-9192"`, are masked with a redaction character, that is, `"******** received a call from ************"`, or masked with an entity label, that is, `"[PERSON_1] received a call from [PHONENUMBER_1]"`. More on how to specify the redaction policy style for your outputs can be found in our [how-to guides](how-to-call.md). 
 
-The Conversational PII detection models (both version `2024-11-01-preview` and `GA`) have been updated to provide enhanced AI quality and accuracy. The numeric identifier entity type now also includes Drivers License and Medicare Beneficiary Identifier.
+The Conversational PII detection models (both version `2024-11-01-preview` and `GA`) are updated to provide enhanced AI quality and accuracy. The numeric identifier entity type now also includes Drivers License and Medicare Beneficiary Identifier.
 
-As of June 2024, we now provide General Availability support for the Conversational PII service (English-language only). Customers can now redact transcripts, chats, and other text written in a conversational style (i.e. text with "um"s, "ah"s, multiple speakers, and the spelling out of words for more clarity) with better confidence in AI quality, Azure SLA support and production environment support, and enterprise-grade security in mind.
+As of June 2024, we now provide General Availability support for the Conversational PII service (English-language only). Customers can now redact transcripts, chats, and other text written in a conversational style (that is, text with `um`s, `ah`s, multiple speakers, and the spelling out of words for more clarity) with better confidence in AI quality, Azure `SLA` support and production environment support, and enterprise-grade security in mind.
+
+## Capabilities
+
+ Currently, PII support is available for the following capabilities:
+
+* [General text PII detection](how-to/redact-text-pii.md) for processing sensitive information (PII) and health information (PHI) in unstructured text across several [predefined categories](concepts/entity-categories.md).
+* [Conversation PII detection](how-to/redact-conversation-pii.md), a specialized model designed to handle speech transcriptions and the informal, conversational tone found in meeting and call transcripts. 
+* [Native Document PII detection](how-to/redact-document-pii.md) for processing structured document files.
 
-> [!TIP]
-> Try out PII detection [in Azure AI Foundry portal](https://ai.azure.com/explore/language), where you can [utilize a currently existing Language Studio resource or create a new Azure AI Foundry resource](../../../ai-studio/ai-services/connect-ai-services.md)
 
-* [**Quickstarts**](quickstart.md) are getting-started instructions to guide you through making requests to the service.
-* [**How-to guides**](how-to-call.md) contain instructions for using the service in more specific or customized ways.
-* The [**conceptual articles**](concepts/entity-categories.md) provide in-depth explanations of the service's functionality and features.
+### [Text PII](#tab/text-pii)
+
+Azure AI Language is a cloud-based service that applies Natural Language Processing (NLP) features to detect categories of personal information (PII) in text-based data. This documentation contains the following types:
+
+* **[Quickstarts](quickstart.md)** are getting-started instructions to guide you through making requests to the service.
+* **[How-to guides](how-to/redact-text-pii.md)** contain instructions for using the service in more specific or customized ways.
 
 [!INCLUDE [Typical workflow for pre-configured language features](../includes/overview-typical-workflow.md)]
 
-## Native document support
+### Key features for text PII
 
-A native document refers to the file format used to create the original document such as Microsoft Word (docx) or a portable document file (pdf). Native document support eliminates the need for text preprocessing prior to using Azure AI Language resource capabilities.  Currently, native document support is available for the [**PiiEntityRecognition**](../personally-identifiable-information/concepts/entity-categories.md) capability.
+Azure AI Language offers named entity recognition to identify and categorize information within your text. The feature detects PII categories including names, organizations, addresses, phone numbers, financial account numbers or codes, and government identification numbers. A subset of this PII is protected health information (PHI). By specifying domain=phi in your request, only PHI entities are returned.
 
- Currently **PII** supports the following native document formats:
+### [Conversation PII](#tab/conversation-pii)
 
-|File type|File extension|Description|
-|---------|--------------|-----------|
-|Text| `.txt`|An unformatted text document.|
-|Adobe PDF| `.pdf`       |A portable document file formatted document.|
-|Microsoft Word|`.docx`|A Microsoft Word document file.|
+The Azure AI Language conversation PII API processes audio conversations to detect and remove sensitive information (PII) based on a set of predefined categories. This documentation contains the following types:
+
+* **[Quickstarts](quickstart.md)** are getting-started instructions to guide you through making requests to the service.
+* **[How-to guides](how-to/redact-conversation-pii.md)** contain instructions for using the service in more specific or customized ways.
+
+### Key features for conversation PII
+
+Conversation PII uses natural language processing techniques to identify and categorize information within conversations. This feature supports both natural chat transcripts and transcribed transcripts from phone calls. For a chat or call, there are different kinds of important information, scattered over long text or transcripts.
 
-For more information, *see* [**Use native documents for language processing**](../native-document-support/use-native-documents.md)
+### [Native document PII](#tab/native-document-pii)
+
+The native document support feature allows you to send API requests asynchronously. You can use an HTTP POST request body to transmit your data and an HTTP GET request query string to check the status of your requests. Your processed documents are stored in your designated Azure Blob Storage container. This documentation contains the following types:
+
+* **[Quickstarts](quickstart.md)** are getting-started instructions to guide you through making requests to the service.
+* **[How-to guides](how-to/redact-document-pii.md)** contain instructions for using the service in more specific or customized ways.
+
+### Key features for native document PII
+
+Document PII uses natural language processing techniques to identify and categorize information within documents.
+
+---
 
 ## Get started with PII detection
 
 [!INCLUDE [development options](./includes/development-options.md)]
 
 [!INCLUDE [Developer reference](../includes/reference-samples-text-analytics.md)]
 
+## Input requirements and service limits
+
+### [Text PII](#tab/text-pii)
+
+* Text PII takes text for analysis. For more information, see [Data and service limits](../concepts/data-limits.md) in the how-to guide.
+* PII works with various written languages. For more information, see [language support](language-support.md?tabs=text-summarization). You can specify in which [supported languages](../concepts/language-support.md) your source text is written. If you don't specify a language, the extraction defaults to English. The API may return offsets in the response to support different [multilingual and emoji encodings](../concepts/multilingual-emoji-support.md). 
+
+### [Conversation PII](#tab/conversation-pii)
+
+* Conversation PII takes structured text for analysis. For more information, see [data and service limits](../concepts/data-limits.md).
+* Conversation summarization works with various spoken languages. For more information, see [language support](language-support.md?tabs=conversation-summarization).
+* [!INCLUDE [service limits article](../includes/service-limits-link.md)]
+
+### [Native document PII](#tab/native-document-pii)
+
+* Native document PII takes text for analysis. For more information, see [Data and service limits](../concepts/data-limits.md) in the how-to guide.
+* Native document PII works with various written languages. For more information, see [language support](language-support.md?tabs=document-summarization).
+
+A native document refers to the file format used to create the original document such as Microsoft Word (docx) or a portable document file (pdf). Native document support eliminates the need for text preprocessing before using Azure AI Language resource capabilities. Currently, native document support is available for the [**PiiEntityRecognition**](../personally-identifiable-information/concepts/entity-categories.md) capability.
+
+ Currently **PII** supports the following native document formats:
+
+|File type|File extension|Description|
+|---------|--------------|-----------|
+|Text| `.txt`|An unformatted text document.|
+|Adobe PDF| `.pdf`       |A portable document file formatted document.|
+|Microsoft Word|`.docx`|A Microsoft Word document file.|
+
+---
+
 ## Responsible AI
 
 An AI system includes not only the technology, but also the people who use it, the people affected by it, and the deployment environment. Read the [transparency note for PII](/legal/cognitive-services/language-service/transparency-note-personally-identifiable-information?context=/azure/ai-services/language-service/context/context) to learn about responsible AI use and deployment in your systems. For more information, see the following articles:
@@ -63,13 +119,11 @@ An AI system includes not only the technology, but also the people who use it, t
 
 * **Apply sensitivity labels** - For example, based on the results from the PII service, a public sensitivity label might be applied to documents where no PII entities are detected. For documents where US addresses and phone numbers are recognized, a confidential label might be applied. A highly confidential label might be used for documents where bank routing numbers are recognized.
 * **Redact some categories of personal information from documents that get wider circulation** - For example, if customer contact records are accessible to frontline support representatives, the company can redact the customer's personal information besides their name from the version of the customer history to preserve the customer's privacy.
-* **Redact personal information in order to reduce unconscious bias** - For example, during a company's resume review process, they can block name, address and phone number to help reduce unconscious gender or other biases.
+* **Redact personal information in order to reduce unconscious bias** - For example, during a company's resume review process, they can block name, address, and phone number to help reduce unconscious gender or other biases.
 * **Replace personal information in source data for machine learning to reduce unfairness** – For example, if you want to remove names that might reveal gender when training a machine learning model, you could use the service to identify them and you could replace them with generic placeholders for model training.
 * **Remove personal information from call center transcription** – For example, if you want to remove names or other PII data that happen between the agent and the customer in a call center scenario. You could use the service to identify and remove them.
 * **Data cleaning for data science** - PII can be used to make the data ready for data scientists and engineers to be able to use these data to train their machine learning models. Redacting the data to make sure that customer data isn't exposed.
 
-
-
 ## Next steps
 
 There are two ways to get started using the entity linking feature:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Languageの個人識別情報(PII)検出に関する概要の更新"
}
```

### Explanation
この変更は、Azure AI Languageの個人識別情報（PII）検出機能に関する概要文書の内容を更新したものです。新しいタイトルは「Azure AI Languageの個人識別情報（PII）検出」で、文書全体にわたって詳細が追加され、情報が整理されています。

ドキュメントでは、Azure AI LanguageのPII検出サービスが、機械学習とAIアルゴリズムを用いてテキストに含まれる敏感情報を特定し、分類し、削除する機能について詳しく説明されています。具体的な例として、電話番号やメールアドレス、身分証明書の情報などが挙げられ、これらの情報を効率的に検出・排除するためのプリデファインドカテゴリーが利用されています。

新機能として、検出された敏感情報をマスキングする際に、単なる削除キャラクターに加えてラベルでのマスキングも選択できるようになったことが紹介されています。また、会話形式のテキスト（チャットやトランスクリプト）に対するPII検出モデルの改良についても言及され、従来のAPIの改善点が強調されています。

さらに、テキストPII、会話PII、ネイティブドキュメントPIIについて、それぞれの機能や特性が明確に整理され、各機能に対する「クイックスタート」や「ハウツーガイド」も提供されています。これにより、ユーザーは各機能をより適切に利用できるようになります。

この更新は、Azure AI LanguageのPII検出機能の理解を深め、ユーザーが効果的に利用するための情報を提供することを目的としています。

## articles/ai-services/language-service/summarization/how-to/conversation-summarization.md{#item-9ff946}

<details>
<summary>Diff</summary>
````diff
@@ -7,12 +7,10 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 11/21/2024
+ms.date: 03/05/2025
 ms.author: jboback
 ms.custom:
-  - language-service-summarization
-  - ignite-2023
-  - build-2024
+  - language-service-pii
 ---
 
 # How to use conversation summarization
@@ -21,9 +19,9 @@ ms.custom:
 
 ## Conversation summarization aspects
 
-- Chapter title and narrative (general conversation) are designed to summarize a conversation into chapter titles, and a summarization of the conversation's contents. This summarization aspect works on conversations with any number of parties. 
+- **Chapter title and narrative (general conversation)** are designed to summarize a conversation into chapter titles, and a summarization of the conversation's contents. This summarization aspect works on conversations with any number of parties. 
 
-- Issue and resolution (call center focused) is designed to summarize text chat logs between customers and customer-service agents. This feature is capable of providing both issues and resolutions present in these logs, which occur between two parties.
+- **Issues and resolutions (call center focused)** are designed to summarize text chat logs between customers and customer-service agents. This feature is capable of providing both issues and resolutions present in these logs, which occur between two parties.
 
 - **Narrative** is designed to summarize the narrative of a conversation.
 
@@ -33,7 +31,7 @@ ms.custom:
 
 :::image type="content" source="../media/conversation-summary-diagram.svg" alt-text="A diagram for sending data to the conversation summarization issues and resolution feature.":::
 
-The AI models used by the API are provided by the service, you just have to send content for analysis.
+The AI models used by the API are provided by the service. You just have to send content for analysis.
 
 For easier navigation, here are links to the corresponding sections for each service:
 
@@ -50,11 +48,11 @@ The conversation summarization API uses natural language processing techniques t
 
 There's another feature in Azure AI Language named [text summarization](../overview.md?tabs=text-summarization) that is more suitable to summarize documents into concise summaries. When you're deciding between text summarization and conversation summarization, consider the following points:
 * Input format: Conversation summarization can operate on both chat text and speech transcripts, which have speakers and their utterances. Text summarization operates using simple text, or Word, PDF, or PowerPoint formats.
-* Purpose of summarization: for example, conversation issue and resolution summarization returns a reason and the resolution for a chat between a customer and a customer service agent.
+* Purpose of summarization: for example, `conversation issue and resolution summarization` returns a reason and the resolution for a chat between a customer and a customer service agent.
 
 ## Submitting data
 
-You submit documents to the API as strings of text. Analysis is performed upon receipt of the request. Because the API is [asynchronous](../../concepts/use-asynchronously.md), there might be a delay between sending an API request and receiving the results.  For information on the size and number of requests you can send per minute and second, see the data limits below.
+You submit documents to the API as strings of text. Analysis is performed upon receipt of the request. Because the API is [asynchronous](../../concepts/use-asynchronously.md), there might be a delay between sending an API request and receiving the results. For information on the size and number of requests you can send per minute and second, see the following data limits.
 
 When you use this feature, the API results are available for 24 hours from the time the request was ingested, and is indicated in the response. After this time period, the results are purged and are no longer available for retrieval.
 
@@ -66,7 +64,7 @@ You can use conversation issue and resolution summarization to get summaries as
 
 ### Get summaries from speech transcriptions 
 
-Conversation issue and resolution summarization also enables you to get summaries from speech transcripts by using the [Speech service's speech to text feature](../../../Speech-Service/call-center-overview.md). The following example shows a short conversation that you might include in your API requests.
+The `conversation issue and resolution summarization` also enables you to get summaries from speech transcripts by using the [Speech service's speech to text feature](../../../Speech-Service/call-center-overview.md). The following example shows a short conversation that you might include in your API requests.
 
 ```json
 "conversations":[
@@ -100,9 +98,9 @@ Conversation issue and resolution summarization also enables you to get summarie
 
 ### Get chapter titles
 
-Conversation chapter title summarization lets you get chapter titles from input conversations. A guided example scenario is provided below:
+Conversation chapter title summarization lets you get chapter titles from input conversations. A guided example scenario follows:
 
-1. Copy the command below into a text editor. The BASH example uses the `\` line continuation character. If your console or terminal uses a different line continuation character, use that character.
+1. Copy the following command into a text editor. The BASH example uses the `\` line continuation character. If your console or terminal uses a different line continuation character, use that character.
 
 ```bash
 curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-conversations/jobs?api-version=2023-11-15-preview \
@@ -117,19 +115,19 @@ curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-conve
       {
         "conversationItems": [
           {
-            "text": "Hello, you’re chatting with Rene. How may I help you?",
+            "text": "Hello, you're chatting with Rene. How may I help you?",
             "id": "1",
             "role": "Agent",
             "participantId": "Agent_1"
           },
           {
-            "text": "Hi, I tried to set up wifi connection for Smart Brew 300 espresso machine, but it didn’t work.",
+            "text": "Hi, I tried to set up wifi connection for Smart Brew 300 espresso machine, but it didn't work.",
             "id": "2",
             "role": "Customer",
             "participantId": "Customer_1"
           },
           {
-            "text": "I’m sorry to hear that. Let’s see what we can do to fix this issue. Could you please try the following steps for me? First, could you push the wifi connection button, hold for 3 seconds, then let me know if the power light is slowly blinking on and off every second?",
+            "text": "I'm sorry to hear that. Let's see what we can do to fix this issue. Could you please try the following steps for me? First, could you push the wifi connection button, hold for 3 seconds, then let me know if the power light is slowly blinking on and off every second?",
             "id": "3",
             "role": "Agent",
             "participantId": "Agent_1"
@@ -153,7 +151,7 @@ curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-conve
             "participantId": "Customer_1"
           },
           {
-            "text": "I’m very sorry to hear that. Let me see if there’s another way to fix the issue. Please hold on for a minute.",
+            "text": "I'm very sorry to hear that. Let me see if there's another way to fix the issue. Please hold on for a minute.",
             "id": "7",
             "role": "Agent",
             "participantId": "Agent_1"
@@ -286,9 +284,9 @@ For long conversation, the model might segment it into multiple cohesive parts,
 
  ### Get narrative summarization
 
-Conversation summarization also lets you get narrative summaries from input conversations. A guided example scenario is provided below:
+Conversation summarization also lets you get narrative summaries from input conversations. A guided example scenario is provided:
 
-1. Copy the command below into a text editor. The BASH example uses the `\` line continuation character. If your console or terminal uses a different line continuation character, use that character.
+1. Copy the following command into a text editor. The BASH example uses the `\` line continuation character. If your console or terminal uses a different line continuation character, use that character.
 
 ```bash
 curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-conversations/jobs?api-version=2023-11-15-preview \
@@ -303,19 +301,19 @@ curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-conve
       {
         "conversationItems": [
           {
-            "text": "Hello, you’re chatting with Rene. How may I help you?",
+            "text": "Hello, you're chatting with Rene. How may I help you?",
             "id": "1",
             "role": "Agent",
             "participantId": "Agent_1"
           },
           {
-            "text": "Hi, I tried to set up wifi connection for Smart Brew 300 espresso machine, but it didn’t work.",
+            "text": "Hi, I tried to set up wifi connection for Smart Brew 300 espresso machine, but it didn't work.",
             "id": "2",
             "role": "Customer",
             "participantId": "Customer_1"
           },
           {
-            "text": "I’m sorry to hear that. Let’s see what we can do to fix this issue. Could you please try the following steps for me? First, could you push the wifi connection button, hold for 3 seconds, then let me know if the power light is slowly blinking on and off every second?",
+            "text": "I'm sorry to hear that. Let's see what we can do to fix this issue. Could you please try the following steps for me? First, could you push the wifi connection button, hold for 3 seconds, then let me know if the power light is slowly blinking on and off every second?",
             "id": "3",
             "role": "Agent",
             "participantId": "Agent_1"
@@ -339,7 +337,7 @@ curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-conve
             "participantId": "Customer_1"
           },
           {
-            "text": "I’m very sorry to hear that. Let me see if there’s another way to fix the issue. Please hold on for a minute.",
+            "text": "I'm very sorry to hear that. Let me see if there's another way to fix the issue. Please hold on for a minute.",
             "id": "7",
             "role": "Agent",
             "participantId": "Agent_1"
@@ -445,9 +443,9 @@ For long conversation, the model might segment it into multiple cohesive parts,
 
  ### Get recap and follow-up task summarization
 
-Conversation summarization also lets you get recaps and follow-up tasks from input conversations. A guided example scenario is provided below:
+Conversation summarization also lets you get recaps and follow-up tasks from input conversations. A guided example scenario is provided:
 
-1. Copy the command below into a text editor. The BASH example uses the `\` line continuation character. If your console or terminal uses a different line continuation character, use that character.
+1. Copy the following command into a text editor. The BASH example uses the `\` line continuation character. If your console or terminal uses a different line continuation character, use that character.
 
 ```bash
 curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-conversations/jobs?api-version=2023-11-15-preview \
@@ -462,19 +460,19 @@ curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-conve
       {
         "conversationItems": [
           {
-            "text": "Hello, you’re chatting with Rene. How may I help you?",
+            "text": "Hello, you're chatting with Rene. How may I help you?",
             "id": "1",
             "role": "Agent",
             "participantId": "Agent_1"
           },
           {
-            "text": "Hi, I tried to set up wifi connection for Smart Brew 300 espresso machine, but it didn’t work.",
+            "text": "Hi, I tried to set up wifi connection for Smart Brew 300 espresso machine, but it didn't work.",
             "id": "2",
             "role": "Customer",
             "participantId": "Customer_1"
           },
           {
-            "text": "I’m sorry to hear that. Let’s see what we can do to fix this issue. Could you please try the following steps for me? First, could you push the wifi connection button, hold for 3 seconds, then let me know if the power light is slowly blinking on and off every second?",
+            "text": "I'm sorry to hear that. Let's see what we can do to fix this issue. Could you please try the following steps for me? First, could you push the wifi connection button, hold for 3 seconds, then let me know if the power light is slowly blinking on and off every second?",
             "id": "3",
             "role": "Agent",
             "participantId": "Agent_1"
@@ -498,7 +496,7 @@ curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-conve
             "participantId": "Customer_1"
           },
           {
-            "text": "I’m very sorry to hear that. Let me see if there’s another way to fix the issue. Please hold on for a minute.",
+            "text": "I'm very sorry to hear that. Let me see if there's another way to fix the issue. Please hold on for a minute.",
             "id": "7",
             "role": "Agent",
             "participantId": "Agent_1"
@@ -645,17 +643,17 @@ For long conversation, the model might segment it into multiple cohesive parts,
 
 ## Getting conversation issue and resolution summarization results
 
-The following text is an example of content you might submit for conversation issue and resolution summarization. This is only an example, the API can accept longer input text. See [data limits](../../concepts/data-limits.md) for more information.
+The following text is an example of content you might submit for conversation issue and resolution summarization. It's only an example. The API can accept longer input text. For more information, *see* [data limits](../../concepts/data-limits.md).
  
 **Agent**: "*Hello, how can I help you*?"
 
 **Customer**: "*How can I upgrade my Contoso subscription? I've been trying the entire day.*"
 
 **Agent**: "*Press the upgrade button then sign in and follow the instructions.*"
 
-Summarization is performed upon receipt of the request by creating a job for the API backend. If the job succeeded, the output of the API will be returned. The output is available for retrieval for 24 hours. After this time, the output is purged. Due to multilingual and emoji support, the response might contain text offsets. See [how to process offsets](../../concepts/multilingual-emoji-support.md) for more information.
+Summarization is performed upon receipt of the request by creating a job for the API backend. If the job succeeded, the output of the API is returned. The output is available for retrieval for 24 hours. After this time, the output is purged. Due to multilingual and emoji support, the response might contain text offsets. For more information, *see* [how to process offsets](../../concepts/multilingual-emoji-support.md).
 
-In the above example, the API might return the following summarized sentences:
+In the previous example, the API might return this summarized sentences output:
 
 | Summarized text                                                           | Aspect     |
 |---------------------------------------------------------------------------|------------|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "会話要約機能に関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Languageの会話要約機能に関するドキュメントを更新したものであり、内容の明確化や情報の整理が行われています。具体的には、定義や機能の説明を強調するためにレイアウトの微調整がなされています。

主な変更点は以下の通りです：

1. **日付の更新**: 文書の日付が「2024年11月21日」から「2025年3月5日」に更新されました。

2. **要約項目の明確化**: 要約機能の説明がより明確になり、特に「章タイトルとナラティブ」や「課題と解決策」の節における構文が整えられています。これにより、各機能がどのような場合に使用されるかが分かりやすくなりました。

3. **構文の改善**: 一部の文章において、文字の使い方や表現が一貫するように改善され、全体的に読みやすさが向上しました。

4. **APIの使用に関する情報の追加**: APIへ送信する際のデータフォーマットや結果の取り扱いに関する情報も整理され、より具体的なガイドラインが提供されるようになりました。

5. **サンプルコードの統一**: コードの例が一貫した形式で表示されるようになり、特にテキスト処理に関する説明が明確にされています。

これらの改訂は、会話要約機能を利用する際のユーザー体験を向上させ、明確で効果的なサポートを提供することを意図しています。ユーザーが当該機能を容易に理解し、利用できるようになっています。

## articles/ai-services/language-service/summarization/how-to/document-summarization.md{#item-da1a14}

<details>
<summary>Diff</summary>
````diff
@@ -1,50 +1,136 @@
 ---
-title: Summarize text with the extractive summarization API
+title: Summarize native documents with the extractive summarization API
 titleSuffix: Azure AI services
-description: This article shows you how to summarize text with the extractive summarization API.
+description: This article shows you how to summarize native documents with the extractive summarization API.
 #services: cognitive-services
-author: jboback
+author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 10/21/2024
-ms.author: jboback
+ms.date: 03/05/2025
+ms.author: lajanuar
 ms.custom:
   - language-service-summarization
-  - ignite-2023
-  - build-2024
 ---
 
-# How to use text summarization
+# How to use native document summarization (preview)
 
-Text summarization is designed to shorten content that users consider too long to read. Both extractive and abstractive summarization condense articles, papers, or documents to key sentences.
+> [!IMPORTANT]
+>
+> * Azure AI Language public preview releases provide early access to features that are in active development.
+> * Features, approaches, and processes may change, before General Availability (GA), based on user feedback.
 
-**Extractive summarization**: Produces a summary by extracting sentences that collectively represent the most important or relevant information within the original content.
+Azure AI Language is a cloud-based service that applies Natural Language Processing (NLP) features to text-based data. Document summarization uses natural language processing to generate extractive (salient sentence extraction) or abstractive (contextual word extraction) summaries for documents. Both `AbstractiveSummarization` and `ExtractiveSummarization` APIs support native document processing. A native document refers to the file format used to create the original document such as Microsoft Word (docx) or a portable document file (pdf). Native document support eliminates the need for text preprocessing before using Azure AI Language resource capabilities. The native document support capability enables you to send API requests asynchronously, using an HTTP POST request body to send your data and HTTP GET request query string to retrieve the status results. Your processed documents are located in your Azure Blob Storage target container.
 
-**Abstractive summarization**: Produces a summary by generating summarized sentences from the document that capture the main idea.
+## Supported document formats
 
-**Query-focused summarization**: Allows you to use a query when summarizing.
+ Applications use native file formats to create, save, or open native documents. Currently **PII** and **Document summarization** capabilities supports the following native document formats:
 
-Each of these capabilities are able to summarize around specific items of interest when specified.
+|File type|File extension|Description|
+|---------|--------------|-----------|
+|Text| `.txt`|An unformatted text document.|
+|Adobe PDF| `.pdf`|A portable document file formatted document.|
+|Microsoft Word| `.docx`|A Microsoft Word document file.|
 
-The AI models used by the API are provided by the service, you just have to send content for analysis.
+## Input guidelines
 
-For easier navigation, here are links to the corresponding sections for each service:
+***Supported file formats***
 
-|Aspect       |Section                                                            |
-|-------------|-------------------------------------------------------------------|
-|Extractive   |[Extractive Summarization](#try-text-extractive-summarization) |
-|Abstractive  |[Abstractive Summarization](#try-text-abstractive-summarization)|
-|Query-focused|[Query-focused Summarization](#query-based-summarization)          |
+|Type|support and limitations|
+|---|---|
+|**PDFs**| Fully scanned PDFs aren't supported.|
+|**Text within images**| Digital images with embedded text aren't supported.|
+|**Digital tables**| Tables in scanned documents aren't supported.|
 
+***Document Size***
 
-## Features
+|Attribute|Input limit|
+|---|---|
+|**Total number of documents per request** |**≤ 20**|
+|**Total content size per request**| **≤ 10 MB**|
+
+## Include native documents with an HTTP request
+
+***Let's get started:***
+
+* For this project, we use the cURL command line tool to make REST API calls.
+
+    > [!NOTE]
+    > The cURL package is preinstalled on most Windows 10 and Windows 11 and most macOS and Linux distributions. You can check the package version with the following commands:
+    > Windows: `curl.exe -V`
+    > macOS `curl -V`
+    > Linux: `curl --version`
+
+* If cURL isn't installed, here are installation links for your platform:
+
+  * [Windows](https://curl.haxx.se/windows/).
+  * [Mac or Linux](https://learn2torials.com/thread/how-to-install-curl-on-mac-or-linux-(ubuntu)-or-windows).
+
+* An active [**Azure account**](https://azure.microsoft.com/free/cognitive-services/). If you don't have one, you can [**create a free account**](https://azure.microsoft.com/free/).
+
+* An [**Azure Blob Storage account**](https://portal.azure.com/#create/Microsoft.StorageAccount-ARM). You also need to [create containers](#create-azure-blob-storage-containers) in your Azure Blob Storage account for your source and target files:
+
+  * **Source container**. This container is where you upload your native files for analysis (required).
+  * **Target container**. This container is where your analyzed files are stored (required).
+
+* A [**single-service Language resource**](https://ms.portal.azure.com/#create/Microsoft.CognitiveServicesTextAnalytics) (**not** a multi-service Azure AI services resource):
+
+  **Complete the Language resource project and instance details fields as follows:**
+
+  1. **Subscription**. Select one of your available Azure subscriptions.
+
+  1. **Resource Group**. You can create a new resource group or add your resource to a preexisting resource group that shares the same lifecycle, permissions, and policies.
+
+  1. **Resource Region**. Choose **Global** unless your business or application requires a specific region. If you're planning on using a [system-assigned managed identity](../../concepts/role-based-access-control.md) for authentication, choose a **geographic** region like **West US**.
+
+  1. **Name**. Enter the name you chose for your resource. The name you choose must be unique within Azure.
+
+  1. **Pricing tier**. You can use the free pricing tier (`Free F0`) to try the service, and upgrade later to a paid tier for production.
+
+  1. Select **Review + Create**.
+
+  1. Review the service terms and select **Create** to deploy your resource.
+
+  1. After your resource successfully deploys, select **Go to resource**.
+
+### Retrieve your key and language service endpoint
+
+Requests to the Language service require a read-only key and custom endpoint to authenticate access.
+
+1. If you created a new resource, after it deploys, select **Go to resource**. If you have an existing language service resource, navigate directly to your resource page.
+
+1. In the left rail, under *Resource Management*, select **Keys and Endpoint**.
+
+1. You can copy and paste your **`key`** and your **`language service instance endpoint`** into the code samples to authenticate your request to the Language service. Only one key is necessary to make an API call.
+
+## Create Azure Blob Storage containers
+
+[**Create containers**](/azure/storage/blobs/storage-quickstart-blobs-portal#create-a-container) in your [**Azure Blob Storage account**](https://portal.azure.com/#create/Microsoft.StorageAccount-ARM) for source and target files.
+
+* **Source container**. This container is where you upload your native files for analysis (required).
+* **Target container**. This container is where your analyzed files are stored (required).
+
+### **Authentication**
+
+Your Language resource needs granted access to your storage account before it can create, read, or delete blobs. There are two primary methods you can use to grant access to your storage data:
+
+* [**Shared access signature (SAS) tokens**](../../native-document-support/shared-access-signatures.md). User delegation SAS tokens are secured with Microsoft Entra credentials. SAS tokens provide secure, delegated access to resources in your Azure storage account.
+
+* [**Managed identity role-based access control (RBAC)**](../../native-document-support/managed-identities.md). Managed identities for Azure resources are service principals that create a Microsoft Entra identity and specific permissions for Azure managed resources.
+
+For this project, we authenticate access to the `source location` and `target location` URLs with Shared Access Signature (SAS) tokens appended as query strings. Each token is assigned to a specific blob (file).
+
+:::image type="content" source="../../native-document-support/media/sas-url-token.png" alt-text="Screenshot of a storage url with SAS token appended.":::
+
+* Your **source** container or blob must designate **read** and **list** access.
+* Your **target** container or blob must designate **write** and **list** access.
 
 The extractive summarization API uses natural language processing techniques to locate key sentences in an unstructured text document. These sentences collectively convey the main idea of the document.
 
 Extractive summarization returns a rank score as a part of the system response along with extracted sentences and their position in the original documents. A rank score is an indicator of how relevant a sentence is determined to be, to the main idea of a document. The model gives a score between 0 and 1 (inclusive) to each sentence and returns the highest scored sentences per request. For example, if you request a three-sentence summary, the service returns the three highest scored sentences.
 
-There's another feature in Azure AI Language, [key phrase extraction](./../../key-phrase-extraction/how-to/call-api.md), that can extract key information. When deciding between key phrase extraction and extractive summarization, consider the following:
+There's another feature in Azure AI Language, [key phrase extraction](./../../key-phrase-extraction/how-to/call-api.md), that can extract key information. To decide between key phrase extraction and extractive summarization, here are helpful considerations:
+
 * Key phrase extraction returns phrases while extractive summarization returns sentences.
 * Extractive summarization returns sentences together with a rank score, and top ranked sentences are returned per request.
 * Extractive summarization also returns the following positional information:
@@ -63,13 +149,13 @@ When you use this feature, the API results are available for 24 hours from the t
 
 When you get results from language detection, you can stream the results to an application or save the output to a file on the local system.
 
-The following is an example of content you might submit for summarization, which is extracted using the Microsoft blog article [A holistic representation toward integrative AI](https://www.microsoft.com/research/blog/a-holistic-representation-toward-integrative-ai/). This article is only an example, the API can accept longer input text. See the data limits section for more information.
+Here's an example of content you might submit for summarization, which is extracted using the Microsoft blog article [A holistic representation toward integrative AI](https://www.microsoft.com/research/blog/a-holistic-representation-toward-integrative-ai/). This article is only an example. The API can accept longer input text. For more information, *see* [data and service limits](../overview.md#input-requirements-and-service-limits).
  
-*"At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there’s magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we have achieved human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."*
+*"At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there's magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we have achieved human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."*
 
-The text summarization API request is processed upon receipt of the request by creating a job for the API backend. If the job succeeded, the output of the API is returned. The output is available for retrieval for 24 hours. After this time, the output is purged. Due to multilingual and emoji support, the response might contain text offsets. See [how to process offsets](../../concepts/multilingual-emoji-support.md) for more information.
+The text summarization API request is processed upon receipt of the request by creating a job for the API backend. If the job succeeded, the output of the API is returned. The output is available for retrieval for 24 hours. After this time, the output is purged. Due to multilingual and emoji support, the response might contain text offsets. For more information, *see* [how to process offsets](../../concepts/multilingual-emoji-support.md).
 
-When you use the above example, the API might return the following summarized sentences:
+When you use the preceding example, the API might return these summarized sentences:
 
 **Extractive summarization**:
 - "At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding."
@@ -96,7 +182,7 @@ You can also use the `sortby` parameter to specify in what order the extracted s
 
 The following example gets you started with text abstractive summarization:
 
-1. Copy the command below into a text editor. The BASH example uses the `\` line continuation character. If your console or terminal uses a different line continuation character, use that character instead.
+1. Copy the following command into a text editor. The BASH example uses the `\` line continuation character. If your console or terminal uses a different line continuation character, use that character instead.
 
 ```bash
 curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-text/jobs?api-version=2023-04-01 \
@@ -111,7 +197,7 @@ curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-text/
       {
         "id": "1",
         "language": "en",
-        "text": "At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there’s magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we have achieved human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."
+        "text": "At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there's magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we have achieved human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."
       }
     ]
   },
@@ -197,146 +283,180 @@ curl -X GET https://<your-language-resource-endpoint>/language/analyze-text/jobs
 
 |parameter  |Description  |
 |---------|---------|
-|`-X POST <endpoint>`     | Specifies your endpoint for accessing the API.        |
-|`-H Content-Type: application/json`     | The content type for sending JSON data.          |
-|`-H "Ocp-Apim-Subscription-Key:<key>`    | Specifies the key for accessing the API.        |
-|`-d <documents>`     | The JSON containing the documents you want to send.         |
+|`-X POST <endpoint>`     | Specifies your Language resource endpoint for accessing the API.        |
+|`--header Content-Type: application/json`     | The content type for sending JSON data.          |
+|`--header "Ocp-Apim-Subscription-Key:<key>`    | Specifies the Language resource key for accessing the API.        |
+|`-data`     | The JSON file containing the data you want to pass with your request.         |
 
-The following cURL commands are executed from a BASH shell. Edit these commands with your own resource name, resource key, and JSON values.
+The following cURL commands are executed from a BASH shell. Edit these commands with your own resource name, resource key, and JSON values. Try analyzing native documents by selecting the `Personally Identifiable Information (PII)` or `Document Summarization` code sample project:
 
-## Query based summarization
+### Summarization sample document
 
-The query-based text summarization API is an extension to the existing text summarization API.
+For this project, you need a **source document** uploaded to your **source container**. You can download our [Microsoft Word sample document](https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/Language/native-document-summarization.docx) or [Adobe PDF](https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/Language/native-document-summarization.pdf) for this quickstart. The source language is English.
 
-The biggest difference is a new `query` field in the request body (under `tasks` > `parameters` > `query`).
+### Build the POST request
 
-> [!TIP]
-> Query based summarization has some differentiation in the utilization of length control based on the type of query based summarization you're using:
-> - Query based extractive summarization supports length control by specifying sentenceCount.
-> - Query based abstractive summarization doesn't support length control.
+1. Using your preferred editor or IDE, create a new directory for your app named `native-document`.
+1. Create a new json file called **document-summarization.json** in your **native-document** directory.
 
-Below is an example request:
+1. Copy and paste the Document Summarization **request sample** into your `document-summarization.json` file. Replace **`{your-source-container-SAS-URL}`** and **`{your-target-container-SAS-URL}`** with values from your Azure portal Storage account containers instance:
 
-```bash
-curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-text/jobs?api-version=2023-11-15-preview \
--H "Content-Type: application/json" \
--H "Ocp-Apim-Subscription-Key: <your-language-resource-key>" \
--d \
-' 
-{
-  "displayName": "Text Extractive Summarization Task Example",
-  "analysisInput": {
-    "documents": [
-      {
-        "id": "1",
-        "language": "en",
-        "text": "At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there’s magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we have achieved human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."
-      }
-    ]
-  },
-"tasks": [
+  ***Request sample***
+
+```json
+  {
+  "tasks": [
     {
-      "kind": "AbstractiveSummarization",
-      "taskName": "Query-based Abstractive Summarization",
-      "parameters": {
-          "query": "XYZ-code",
-          "summaryLength": "short"
-      }
-    },    {
       "kind": "ExtractiveSummarization",
-      "taskName": "Query_based Extractive Summarization",
       "parameters": {
-          "query": "XYZ-code"
+        "sentenceCount": 6
       }
     }
-  ]
+  ],
+  "analysisInput": {
+    "documents": [
+      {
+        "source": {
+          "location": "{your-source-blob-SAS-URL}"
+        },
+        "targets": {
+          "location": "{your-target-container-SAS-URL}"
+        }
+      }
+    ]
+  }
 }
-'
+
 ```
 
-### Summary length control
+### Run the POST request
+
+Before you run the **POST** request, replace `{your-language-resource-endpoint}` and `{your-key}` with the endpoint value from your Azure portal Language resource instance.
+
+  > [!IMPORTANT]
+  > Remember to remove the key from your code when you're done, and never post it publicly. For production, use a secure way of storing and accessing your credentials like [Azure Key Vault](/azure/key-vault/general/overview). For more information, *see* Azure AI services [security](/azure/ai-services/security-features).
 
-#### Using the summaryLength parameter in abstractive summarization
+  ***PowerShell***
 
-If you don't specify `summaryLength`, the model determines the summary length.
+  ```powershell
+   cmd /c curl "{your-language-resource-endpoint}/language/analyze-documents/jobs?api-version=2024-11-15-preview" -i -X POST --header "Content-Type: application/json" --header "Ocp-Apim-Subscription-Key: {your-key}" --data "@document-summarization.json"
+  ```
 
-For the `summaryLength` parameter, three values are accepted:
-* oneSentence: Generates a summary of mostly 1 sentence, with around 80 tokens.
-* short: Generates a summary of mostly 2-3 sentences, with around 120 tokens.
-* medium: Generates a summary of mostly 4-6 sentences, with around 170 tokens.
-* long: Generates a summary of mostly over 7 sentences, with around 210 tokens.
+  ***command prompt / terminal***
 
-Below is an example request:
+  ```bash
+  curl -v -X POST "{your-language-resource-endpoint}/language/analyze-documents/jobs?api-version=2024-11-15-preview" --header "Content-Type: application/json" --header "Ocp-Apim-Subscription-Key: {your-key}" --data "@document-summarization.json"
+  ```
+
+#### Sample response:
+
+   ```http
+   HTTP/1.1 202 Accepted
+   Content-Length: 0
+   operation-location: https://{your-language-resource-endpoint}/language/analyze-documents/jobs/f1cc29ff-9738-42ea-afa5-98d2d3cabf94?api-version=2024-11-15-preview
+   apim-request-id: e7d6fa0c-0efd-416a-8b1e-1cd9287f5f81
+   x-ms-region: West US 2
+   Date: Thu, 25 Jan 2024 15:12:32 GMT
+   ```
+
+### POST response (jobId)
+
+You receive a 202 (Success) response that includes a read-only Operation-Location header. The value of this header contains a jobId that can be queried to get the status of the asynchronous operation and retrieve the results using a GET request:
+
+  :::image type="content" source="../../native-document-support/media/operation-location-result-id.png" alt-text="Screenshot showing the operation-location value in the POST response.":::
+
+## Get analyze results (GET request)
+
+1. After your successful **POST** request, poll the operation-location header returned in the POST request to view the processed data.
+
+1. Here's the structure of the **GET** request:
+
+   ```bash
+   GET {cognitive-service-endpoint}/language/analyze-documents/jobs/{jobId}?api-version=2024-11-15-preview
+   ```
+
+1. Before you run the command, make these changes:
+
+    * Replace {**jobId**} with the Operation-Location header from the POST response.
+
+    * Replace {**your-language-resource-endpoint**} and {**your-key**} with the values from your Language service instance in the Azure portal.
+
+## Get request
+
+```powershell
+    cmd /c curl "{your-language-resource-endpoint}/language/analyze-documents/jobs/{jobId}?api-version=2024-11-15-preview" -i -X GET --header "Content-Type: application/json" --header "Ocp-Apim-Subscription-Key: {your-key}"
+```
 
 ```bash
-curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-text/jobs?api-version=2023-04-01 \
--H "Content-Type: application/json" \
--H "Ocp-Apim-Subscription-Key: <your-language-resource-key>" \
--d \
-' 
-{
-  "displayName": "Text Abstractive Summarization Task Example",
-  "analysisInput": {
-    "documents": [
-      {
-        "id": "1",
-        "language": "en",
-        "text": "At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there’s magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we have achieved human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."
-      }
-    ]
-  },
-  "tasks": [
-    {
-      "kind": "AbstractiveSummarization",
-      "taskName": "Length controlled Abstractive Summarization",
-          "parameters": {
-          "sentenceLength": "short"
-      }
-    }
-  ]
-}
-'
+    curl -v -X GET "{your-language-resource-endpoint}/language/analyze-documents/jobs/{jobId}?api-version=2024-11-15-preview" --header "Content-Type: application/json" --header "Ocp-Apim-Subscription-Key: {your-key}"
 ```
 
-#### Using the sentenceCount parameter in extractive summarization
-For the `sentenceCount` parameter, you can input a value 1-20 to indicate the desired number of output sentences.
+#### Examine the response
 
-Below is an example request:
+You receive a 200 (Success) response with JSON output. The **status** field indicates the result of the operation. If the operation isn't complete, the value of **status** is "running" or "notStarted", and you should call the API again, either manually or through a script. We recommend an interval of one second or more between calls.
 
-```bash
-curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-text/jobs?api-version=2023-11-15-preview \
--H "Content-Type: application/json" \
--H "Ocp-Apim-Subscription-Key: <your-language-resource-key>" \
--d \
-' 
+#### Sample response
+
+```json
 {
-  "displayName": "Text Extractive Summarization Task Example",
-  "analysisInput": {
-    "documents": [
+  "jobId": "f1cc29ff-9738-42ea-afa5-98d2d3cabf94",
+  "lastUpdatedDateTime": "2024-01-24T13:17:58Z",
+  "createdDateTime": "2024-01-24T13:17:47Z",
+  "expirationDateTime": "2024-01-25T13:17:47Z",
+  "status": "succeeded",
+  "errors": [],
+  "tasks": {
+    "completed": 1,
+    "failed": 0,
+    "inProgress": 0,
+    "total": 1,
+    "items": [
       {
-        "id": "1",
-        "language": "en",
-        "text": "At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there’s magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we have achieved human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."
+        "kind": "ExtractiveSummarizationLROResults",
+        "lastUpdateDateTime": "2024-01-24T13:17:58.33934Z",
+        "status": "succeeded",
+        "results": {
+          "documents": [
+            {
+              "id": "doc_0",
+              "source": {
+                "kind": "AzureBlob",
+                "location": "https://myaccount.blob.core.windows.net/sample-input/input.pdf"
+              },
+              "targets": [
+                {
+                  "kind": "AzureBlob",
+                  "location": "https://myaccount.blob.core.windows.net/sample-output/df6611a3-fe74-44f8-b8d4-58ac7491cb13/ExtractiveSummarization-0001/input.result.json"
+                }
+              ],
+              "warnings": []
+            }
+          ],
+          "errors": [],
+          "modelVersion": "2023-02-01-preview"
+        }
       }
     ]
-  },
-"tasks": [
-    {
-      "kind": "ExtractiveSummarization",
-      "taskName": "Length controlled Extractive Summarization",
-      "parameters": {
-          "sentenceCount": "5"
-      }
-    }
-  ]
+  }
 }
-'
 ```
 
-## Service and data limits
+***Upon successful completion***:
+
+* The analyzed documents can be found in your target container.
+* The successful POST method returns a `202 Accepted` response code indicating that the service created the batch request.
+* The POST request also returned response headers including `Operation-Location` that provides a value used in subsequent GET requests.
+
+## Clean up resources
+
+If you want to clean up and remove an Azure AI services subscription, you can delete the resource or resource group. Deleting the resource group also deletes any other resources associated with it.
+
+* [Azure portal](../../../multi-service-resource.md?pivots=azportal#clean-up-resources)
+* [Azure CLI](../../../multi-service-resource.md?pivots=azcli#clean-up-resources)
+
+## Next steps
 
-[!INCLUDE [service limits article](../../includes/service-limits-link.md)]
+> [!div class="nextstepaction"]
+> [Document summarization overview](../overview.md "Learn more about native document summarization.")
 
-## See also
 
-* [Summarization overview](../overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書要約APIに関するドキュメントの大幅な更新"
}
```

### Explanation
この変更は、Azure AI Languageの文書要約APIに関するドキュメントを大幅に更新したものであり、特にネイティブドキュメント処理の機能や利用方法に焦点を当てています。主な変更点は以下の通りです：

1. **新しいタイトルと説明**: 文書要約のタイトルが「サマリー テキストからネイティブ ドキュメントを要約する」に変更され、説明文もインテンションに合わせて更新されました。

2. **機能の拡充**: 文書要約機能が、抽出的要約と要約生成の両方をサポートするように明確に説明されています。具体的には、ネイティブ形式の文書（Microsoft WordやPDF）を直接扱えることが強調されています。

3. **サポートされるファイル形式の明示**: サポートされるファイル形式（.txt、.pdf、.docx）が表形式で整理され、新たに非対応フォーマットや制約（スキャンされたPDFやデジタルテーブルの非サポート）が明示されています。

4. **APIリクエストに関する詳細なガイド**: APIへのHTTPリクエスト作成手順が詳細に示されており、cURLコマンドを使用した具体例が提供されています。

5. **エラーハンドリングと応答処理の更新**: APIからの応答の処理方法や、ジョブIDを使用した結果の取得方法が説明されています。成功した際の応答の構造も明確にされており、ユーザーが結果を取得するための手順が容易になっています。

6. **クリーンアップの手順が追加**: リソースを整理するための手順も追加され、Azure AIサービスのサブスクリプションを削除する方法が示されています。

これらの更新により、ユーザーは文書要約APIの機能を理解しやすくなり、利便性が向上しています。このドキュメントは、実際のアプリケーションで文書要約を利用するための実用的なガイドとして機能します。

## articles/ai-services/language-service/summarization/how-to/text-summarization.md{#item-8a6034}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,348 @@
+---
+title: Summarize text with the extractive summarization API
+titleSuffix: Azure AI services
+description: This article shows you how to summarize text with the extractive summarization API.
+#services: cognitive-services
+author: jboback
+manager: nitinme
+ms.service: azure-ai-language
+ms.topic: how-to
+ms.date: 03/05/2025
+ms.author: jboback
+ms.custom:
+  - language-service-summarization
+  - ignite-2023
+  - build-2024
+---
+
+# How to use text summarization
+
+Text summarization is designed to shorten content that users consider too long to read. Both extractive and abstractive summarization condense articles, papers, or documents to key sentences.
+
+**Extractive summarization**: Produces a summary by extracting sentences that collectively represent the most important or relevant information within the original content.
+
+**Abstractive summarization**: Produces a summary by generating summarized sentences from the document that capture the main idea.
+
+**Query-focused summarization**: Allows you to use a query when summarizing.
+
+Each of these capabilities is able to summarize around specific items of interest when specified.
+
+The AI models used by the API are provided by the service. You just have to send content for analysis.
+
+For easier navigation, here are links to the corresponding sections for each service:
+
+|Aspect       |Section                                                            |
+|-------------|-------------------------------------------------------------------|
+|Extractive   |[Extractive Summarization](#try-text-extractive-summarization) |
+|Abstractive  |[Abstractive Summarization](#try-text-abstractive-summarization)|
+|Query-focused|[Query-focused Summarization](#query-based-summarization)          |
+
+
+## Features
+
+> [!TIP]
+> If you want to start using these features, you can follow the [quickstart article](../quickstart.md) to get started. You can also make example requests using [Language Studio](../../language-studio.md) without needing to write code.
+
+The extractive summarization API uses natural language processing techniques to locate key sentences in an unstructured text document. These sentences collectively convey the main idea of the document.
+
+Extractive summarization returns a rank score as a part of the system response along with extracted sentences and their position in the original documents. A rank score is an indicator of how relevant a sentence is determined to be, to the main idea of a document. The model gives a score between 0 and 1 (inclusive) to each sentence and returns the highest scored sentences per request. For example, if you request a three-sentence summary, the service returns the three highest scored sentences.
+
+There's another feature in Azure AI Language, [key phrase extraction](./../../key-phrase-extraction/how-to/call-api.md), that can extract key information. When deciding between key phrase extraction and extractive summarization, consider these factors:
+
+* Key phrase extraction returns phrases while extractive summarization returns sentences.
+* Extractive summarization returns sentences together with a rank score, and top ranked sentences are returned per request.
+* Extractive summarization also returns the following positional information:
+    * Offset: The start position of each extracted sentence.
+    * Length: The length of each extracted sentence.
+
+## Determine how to process the data (optional)
+
+### Submitting data
+
+You submit documents to the API as strings of text. Analysis is performed upon receipt of the request. Because the API is [asynchronous](../../concepts/use-asynchronously.md), there might be a delay between sending an API request, and receiving the results.
+
+When you use this feature, the API results are available for 24 hours from the time the request was ingested, and is indicated in the response. After this time period, the results are purged and are no longer available for retrieval.
+
+### Getting text summarization results
+
+When you get results from language detection, you can stream the results to an application or save the output to a file on the local system.
+
+To follow is an example of content you might submit for summarization, which is extracted using the Microsoft blog article [A holistic representation toward integrative AI](https://www.microsoft.com/research/blog/a-holistic-representation-toward-integrative-ai/). This article is only an example. The API can accept longer input text. For more information, *see* [data and service limits](../overview.md#input-requirements-and-service-limits)
+ 
+*"At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there's magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we have achieved human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."*
+
+The text summarization API request is processed upon receipt of the request by creating a job for the API backend. If the job succeeded, the output of the API is returned. The output is available for retrieval for 24 hours. After this time, the output is purged. Due to multilingual and emoji support, the response might contain text offsets. For more information, *see* [how to process offsets](../../concepts/multilingual-emoji-support.md).
+
+When you use the preceding example, the API might return these summarized sentences:
+
+**Extractive summarization**:
+
+- "At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding."
+- "We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages."
+- "The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today."
+
+**Abstractive summarization**:
+- "Microsoft is taking a more holistic, human-centric approach to learning and understanding. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. Over the past five years, we have achieved human performance on benchmarks in."
+
+### Try text extractive summarization
+
+You can use text extractive summarization to get summaries of articles, papers, or documents. To see an example, see the [quickstart article](../quickstart.md).
+
+You can use the `sentenceCount` parameter to guide how many sentences are returned, with `3` being the default. The range is from 1 to 20.
+
+You can also use the `sortby` parameter to specify in what order the extracted sentences are returned - either `Offset` or `Rank`, with `Offset` being the default. 
+
+|parameter value  |Description  |
+|---------|---------|
+|Rank    | Order sentences according to their relevance to the input document, as decided by the service.        |
+|Offset    | Keeps the original order in which the sentences appear in the input document.        |
+
+### Try text abstractive summarization
+
+The following example gets you started with text abstractive summarization:
+
+1. Copy the following command into a text editor. The BASH example uses the `\` line continuation character. If your console or terminal uses a different line continuation character, use that character instead.
+
+```bash
+curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-text/jobs?api-version=2023-04-01 \
+-H "Content-Type: application/json" \
+-H "Ocp-Apim-Subscription-Key: <your-language-resource-key>" \
+-d \
+' 
+{
+  "displayName": "Text Abstractive Summarization Task Example",
+  "analysisInput": {
+    "documents": [
+      {
+        "id": "1",
+        "language": "en",
+        "text": "At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there's magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we have achieved human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."
+      }
+    ]
+  },
+  "tasks": [
+    {
+      "kind": "AbstractiveSummarization",
+      "taskName": "Text Abstractive Summarization Task 1",
+    }
+  ]
+}
+'
+```
+
+2. Make the following changes in the command where needed:
+    - Replace the value `your-language-resource-key` with your key.
+    - Replace the first part of the request URL `your-language-resource-endpoint` with your endpoint URL.
+
+3. Open a command prompt window (for example: BASH).
+
+4. Paste the command from the text editor into the command prompt window, then run the command.
+
+5. Get the `operation-location` from the response header. The value looks similar to the following URL:
+
+```http
+https://<your-language-resource-endpoint>/language/analyze-text/jobs/12345678-1234-1234-1234-12345678?api-version=2022-10-01-preview
+```
+
+6. To get the results of the request, use the following cURL command. Be sure to replace `<my-job-id>` with the numerical ID value you received from the previous `operation-location` response header:
+
+```bash
+curl -X GET https://<your-language-resource-endpoint>/language/analyze-text/jobs/<my-job-id>?api-version=2022-10-01-preview \
+-H "Content-Type: application/json" \
+-H "Ocp-Apim-Subscription-Key: <your-language-resource-key>"
+```
+
+### Abstractive text summarization example JSON response
+
+```json
+{
+    "jobId": "cd6418fe-db86-4350-aec1-f0d7c91442a6",
+    "lastUpdateDateTime": "2022-09-08T16:45:14Z",
+    "createdDateTime": "2022-09-08T16:44:53Z",
+    "expirationDateTime": "2022-09-09T16:44:53Z",
+    "status": "succeeded",
+    "errors": [],
+    "displayName": "Text Abstractive Summarization Task Example",
+    "tasks": {
+        "completed": 1,
+        "failed": 0,
+        "inProgress": 0,
+        "total": 1,
+        "items": [
+            {
+                "kind": "AbstractiveSummarizationLROResults",
+                "taskName": "Text Abstractive Summarization Task 1",
+                "lastUpdateDateTime": "2022-09-08T16:45:14.0717206Z",
+                "status": "succeeded",
+                "results": {
+                    "documents": [
+                        {
+                            "summaries": [
+                                {
+                                    "text": "Microsoft is taking a more holistic, human-centric approach to AI. We've developed a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We've achieved human performance on benchmarks in conversational speech recognition, machine translation, ...... and image captions.",
+                                    "contexts": [
+                                        {
+                                            "offset": 0,
+                                            "length": 247
+                                        }
+                                    ]
+                                }
+                            ],
+                            "id": "1"
+                        }
+                    ],
+                    "errors": [],
+                    "modelVersion": "latest"
+                }
+            }
+        ]
+    }
+}
+```
+
+|parameter  |Description  |
+|---------|---------|
+|`-X POST <endpoint>`     | Specifies your endpoint for accessing the API.        |
+|`-H Content-Type: application/json`     | The content type for sending JSON data.          |
+|`-H "Ocp-Apim-Subscription-Key:<key>`    | Specifies the key for accessing the API.        |
+|`-d <documents>`     | The JSON containing the documents you want to send.         |
+
+The following cURL commands are executed from a BASH shell. Edit these commands with your own resource name, resource key, and JSON values.
+
+## Query based summarization
+
+The query-based text summarization API is an extension to the existing text summarization API.
+
+The biggest difference is a new `query` field in the request body (under `tasks` > `parameters` > `query`).
+
+> [!TIP]
+> Query based summarization has some differentiation in the utilization of length control based on the type of query based summarization you're using:
+> - Query based extractive summarization supports length control by specifying sentenceCount.
+> - Query based abstractive summarization doesn't support length control.
+
+Here's an example request:
+
+```bash
+curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-text/jobs?api-version=2023-11-15-preview \
+-H "Content-Type: application/json" \
+-H "Ocp-Apim-Subscription-Key: <your-language-resource-key>" \
+-d \
+' 
+{
+  "displayName": "Text Extractive Summarization Task Example",
+  "analysisInput": {
+    "documents": [
+      {
+        "id": "1",
+        "language": "en",
+        "text": "At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there's magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we have achieved human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."
+      }
+    ]
+  },
+"tasks": [
+    {
+      "kind": "AbstractiveSummarization",
+      "taskName": "Query-based Abstractive Summarization",
+      "parameters": {
+          "query": "XYZ-code",
+          "summaryLength": "short"
+      }
+    },    {
+      "kind": "ExtractiveSummarization",
+      "taskName": "Query_based Extractive Summarization",
+      "parameters": {
+          "query": "XYZ-code"
+      }
+    }
+  ]
+}
+'
+```
+
+### Summary length control
+
+#### Using the summaryLength parameter in abstractive summarization
+
+If you don't specify `summaryLength`, the model determines the summary length.
+
+For the `summaryLength` parameter, three values are accepted:
+
+* oneSentence: Generates a summary of mostly one sentence, with around 80 tokens.
+* short: Generates a summary of mostly two to three sentences, with around 120 tokens.
+* medium: Generates a summary of mostly four to six sentences, with around 170 tokens.
+* long: Generates a summary of mostly over seven sentences, with around 210 tokens.
+
+Here's is an example request:
+
+```bash
+curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-text/jobs?api-version=2023-04-01 \
+-H "Content-Type: application/json" \
+-H "Ocp-Apim-Subscription-Key: <your-language-resource-key>" \
+-d \
+' 
+{
+  "displayName": "Text Abstractive Summarization Task Example",
+  "analysisInput": {
+    "documents": [
+      {
+        "id": "1",
+        "language": "en",
+        "text": "At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there's magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we have achieved human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."
+      }
+    ]
+  },
+  "tasks": [
+    {
+      "kind": "AbstractiveSummarization",
+      "taskName": "Length controlled Abstractive Summarization",
+          "parameters": {
+          "sentenceLength": "short"
+      }
+    }
+  ]
+}
+'
+```
+
+#### Using the sentenceCount parameter in extractive summarization
+For the `sentenceCount` parameter, you can input a value 1-20 to indicate the desired number of output sentences.
+
+Here's is an example request:
+
+```bash
+curl -i -X POST https://<your-language-resource-endpoint>/language/analyze-text/jobs?api-version=2023-11-15-preview \
+-H "Content-Type: application/json" \
+-H "Ocp-Apim-Subscription-Key: <your-language-resource-key>" \
+-d \
+' 
+{
+  "displayName": "Text Extractive Summarization Task Example",
+  "analysisInput": {
+    "documents": [
+      {
+        "id": "1",
+        "language": "en",
+        "text": "At Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there's magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code enables us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pretrained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we have achieved human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."
+      }
+    ]
+  },
+"tasks": [
+    {
+      "kind": "ExtractiveSummarization",
+      "taskName": "Length controlled Extractive Summarization",
+      "parameters": {
+          "sentenceCount": "5"
+      }
+    }
+  ]
+}
+'
+```
+
+## Service and data limits
+
+[!INCLUDE [service limits article](../../includes/service-limits-link.md)]
+
+## See also
+
+* [Summarization overview](../overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "テキスト要約APIの利用方法に関する新規ドキュメントの追加"
}
```

### Explanation
この変更は、Azure AI Languageのテキスト要約APIに関する新しいドキュメントが追加されたもので、テキスト要約の機能を網羅的に説明しています。具体的な内容は以下の通りです：

1. **ドキュメントの構成**: 新たに作成された文書には、テキスト要約APIの説明が含まれ、抽出的要約、生成的要約、クエリベースの要約など、異なる要約方法の詳細が紹介されています。

2. **抽出的および生成的要約の説明**: 
   - **抽出的要約**は、原文から重要な文を抽出して要約を生成する方法。
   - **生成的要約**は、文書の主題を捉えた新しい文を生成する方法が説明されています。

3. **クエリに基づく要約**: ユーザーが指定したクエリに対して要約を行う機能についても触れられています。

4. **APIの利用方法**: APIへのリクエスト方法や、非同期処理の特性、結果の取得方法が詳細に説明されています。特に、入力データのフォーマットや結果の保持期間が明記されています。

5. **具体的なコード例**: テキスト要約APIのリクエストに関する具体的なcURLコマンド例が提供されており、実際にAPIを呼び出す手順が示されているため、ユーザーがすぐに実装に取り掛かれるようになっています。

6. **サンプル文書の提供**: サンプルとして、Microsoftのブログ記事から引用されたテキストを使用し、それに基づいた要約の実行結果が示されています。

この新しいドキュメントは、ユーザーがテキスト要約APIを効果的に利用するための実用的なガイドとなっており、特に技術者や開発者にとって有益なリソースです。

## articles/ai-services/language-service/summarization/overview.md{#item-844139}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 02/17/2025
+ms.date: 03/05/2025
 ms.author: jboback
 ms.custom: language-service-summarization, build-2024, ignite-2024
 ---
@@ -16,35 +16,37 @@ ms.custom: language-service-summarization, build-2024, ignite-2024
 
 [!INCLUDE [availability](includes/regional-availability.md)]
 
-Summarization is one feature offered by [Azure AI Language](../overview.md), which is a combination of generative Large Language models and task-optimized encoder models that offer summarization solutions with higher quality, cost efficiency, and lower latency.
+Summarization is a feature offered by [Azure AI Language](../overview.md), a combination of generative Large Language models and task-optimized encoder models that offer summarization solutions with higher quality, cost efficiency, and lower latency.
 Use this article to learn more about this feature, and how to use it in your applications.
 
-Out of the box, the service provides summarization solutions for three types of genre, plain texts, conversations, and native documents. Text summarization only accepts plain text blocks, and conversation summarization accept conversational input, including various speech audio signals in order for the model to effectively segment and summarize, and native document can directly summarize for documents in their native formats, such as Words, PDF, etc. 
+Out of the box, the service provides summarization solutions for three types of genre, plain texts, conversations, and native documents. Text summarization only accepts plain text blocks. Conversation summarization accepts conversational input, including various speech audio signals. Native document summarization accepts documents in their native formats, such as Word, PDF, or plain text. For more information, *see* [Supported document formats](../native-document-support/overview.md#supported-document-formats).
 
 > [!TIP]
-> Try out Summarization [in Azure AI Foundry portal](https://ai.azure.com/explore/language), where you can [utilize a currently existing Language Studio resource or create a new Azure AI Foundry resource](../../../ai-studio/ai-services/connect-ai-services.md) in order to use this service. 
+> Try out Summarization [in Azure AI Foundry portal](https://ai.azure.com/explore/language). There you can [utilize a currently existing Language Studio resource or create a new Azure AI Foundry resource](../../../ai-studio/ai-services/connect-ai-services.md) in order to use this service.
+
+## Capabilities
 
 # [Text summarization](#tab/text-summarization)
 
 This documentation contains the following article types:
 
 * **[Quickstarts](quickstart.md?pivots=rest-api&tabs=text-summarization)** are getting-started instructions to guide you through making requests to the service.
-* **[How-to guides](how-to/document-summarization.md)** contain instructions for using the service in more specific or customized ways.
+* **[How-to guides](how-to/text-summarization.md)** contain instructions for using the service in more specific or customized ways.
 
-These features are designed to shorten content that could be considered too long to read.
+[!INCLUDE [Typical workflow for pre-configured language features](../includes/overview-typical-workflow.md)]
 
 ## Key features for text summarization
 
-Text summarization uses natural language processing techniques to generate a summary for plain texts, which can be from a document or a conversation, or any texts. There are two approaches of summarization this API provides:
+Text summarization uses natural language processing techniques to generate a summary for plain texts, which can be from a document, conversation, or any texts. There are two approaches of summarization this API provides:
 
-* [**Extractive summarization**](how-to/document-summarization.md#try-text-extractive-summarization): Produces a summary by extracting salient sentences within the document, together the positioning information of these sentences. 
+* [**Extractive summarization**](how-to/text-summarization.md#try-text-extractive-summarization): Produces a summary by extracting salient sentences within the source text, together the positioning information of these sentences.
 
-  * Multiple extracted sentences: These sentences collectively convey the main idea of the document. They're original sentences extracted from the input document's content.
+  * Multiple extracted sentences: These sentences collectively convey the main idea of the input text. They're original sentences extracted from the input text content.
   * Rank score: The rank score indicates how relevant a sentence is to the main topic. Text summarization ranks extracted sentences, and you can determine whether they're returned in the order they appear, or according to their rank.
  For example, if you request a three-sentence summary extractive summarization returns the three highest scored sentences.
   * Positional information: The start position and length of extracted sentences.
 
-* [**Abstractive summarization**](how-to/document-summarization.md#try-text-abstractive-summarization): Generates a summary with concise, coherent sentences or words that aren't verbatim extract sentences from the original document.
+* [**Abstractive summarization**](how-to/text-summarization.md#try-text-abstractive-summarization): Generates a summary with concise, coherent sentences or words that aren't verbatim extract sentences from the original source.
   * Summary texts: Abstractive summarization returns a summary for each contextual input range. A long input can be segmented so multiple groups of summary texts can be returned with their contextual input range.
   * Contextual input range: The range within the input that was used to generate the summary text.
 
@@ -54,7 +56,7 @@ As an example, consider the following paragraph of text:
 
 The text summarization API request is processed upon receipt of the request by creating a job for the API backend. If the job succeeded, the output of the API is returned. The output is available for retrieval for 24 hours. After this time, the output is purged. Due to multilingual and emoji support, the response can contain text offsets. For more information, see [how to process offsets](../concepts/multilingual-emoji-support.md).
 
-If we use the above example, the API might return these summaries:
+If we use the preceding example, the API might return these summaries:
 
 **Extractive summarization**:
 - "At Microsoft, we are on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding."
@@ -82,21 +84,21 @@ Conversation summarization supports the following features:
 
 As an example, consider the following example conversation:
 
-**Agent**: "*Hello, you're chatting with Rene. How may I help you?*" 
+**Agent**: "*Hello, you're chatting with Rene. How may I help you?*"
 
-**Customer**: "*Hi, I tried to set up wifi connection for Smart Brew 300 espresso machine, but it didn't work.*" 
+**Customer**: "*Hi, I tried to set up wifi connection for Smart Brew 300 espresso machine, but it didn't work.*"
 
-**Agent**: "*I'm sorry to hear that. Let's see what we can do to fix this issue. Could you push the wifi connection button, hold for 3 seconds, then let me know if the power light is slowly blinking?*" 
+**Agent**: "*I'm sorry to hear that. Let's see what we can do to fix this issue. Could you push the wifi connection button, hold for 3 seconds, then let me know if the power light is slowly blinking?*"
 
-**Customer**: "*Yes, I pushed the wifi connection button, and now the power light is slowly blinking.*" 
+**Customer**: "*Yes, I pushed the wifi connection button, and now the power light is slowly blinking.*"
 
-**Agent**: "*Great. Thank you! Now, please check in your Contoso Coffee app. Does it prompt to ask you to connect with the machine?*" 
+**Agent**: "*Great. Thank you! Now, please check in your Contoso Coffee app. Does it prompt to ask you to connect with the machine?*"
 
-**Customer**: "*No. Nothing happened.*" 
+**Customer**: "*No. Nothing happened.*"
 
-**Agent**: "*I see. Thanks. Let's try if a factory reset can solve the issue. Could you please press and hold the center button for 5 seconds to start the factory reset.*"  
+**Agent**: "*I see. Thanks. Let's try if a factory reset can solve the issue. Could you please press and hold the center button for 5 seconds to start the factory reset.*"
 
-**Customer**: *"I've tried the factory reset and followed the above steps again, but it still didn't work."* 
+**Customer**: *"I've tried the factory reset and followed the above steps again, but it still didn't work."*
 
 **Agent**: "*I'm very sorry to hear that. Let me see if there's another way to fix the issue. Please hold on for a minute.*"
 
@@ -115,12 +117,11 @@ Conversation summarization feature would simplify the text as follows:
 This documentation contains the following article types:
 
 * **[Quickstarts](quickstart.md?pivots=rest-api&tabs=document-summarization)** are getting-started instructions to guide you through making requests to the service.
-* **[How-to guides](how-to/document-summarization.md)** contain instructions for using the service in more specific or customized ways.
+* **[How-to guides](../native-document-support/overview.md)** contain instructions for using the service in more specific or customized ways.
 
-Document summarization uses natural language processing techniques to generate a summary for documents. 
+Native document summarization uses natural language processing techniques to generate a summary for native documents. A native document refers to the file format used to create the original document such as Microsoft Word (docx) or a portable document file (pdf). Native document support eliminates the need for text preprocessing before using Azure AI Language resource capabilities. Currently, native document support is available for two types of summarization:
 
-A native document refers to the file format used to create the original document such as Microsoft Word (docx) or a portable document file (pdf). Native document support eliminates the need for text preprocessing prior to using Azure AI Language resource capabilities.  Currently, native document support is available for two types of summarization:
-* **Extractive summarization**: Produces a summary by extracting salient sentences within the document, together the positioning information of those sentences. 
+* [**Extractive summarization**](how-to/document-summarization.md): Produces a summary by extracting salient sentences within the document, together the positioning information of those sentences.
 
   * Multiple extracted sentences: These sentences collectively convey the main idea of the document. They're original sentences extracted from the input document's content.
   * Rank score: The rank score indicates how relevant a sentence is to the main topic. Text summarization ranks extracted sentences, and you can determine whether they're returned in the order they appear, or according to their rank.
@@ -132,15 +133,15 @@ A native document refers to the file format used to create the original document
   * Contextual input range: The range within the input that was used to generate the summary text.
 
 
- Currently **Document Summarization** supports the following native document formats:
+Currently, **Document Summarization** supports the following native document formats:
 
 |File type|File extension|Description|
 |---------|--------------|-----------|
 |Text| `.txt`|An unformatted text document.|
 |Adobe PDF| `.pdf`       |A portable document file formatted document.|
 |Microsoft Word|`.docx`|A Microsoft Word document file.|
 
-For more information, *see* [**Use native documents for language processing**](../native-document-support/use-native-documents.md)
+For more information, *see* [**Summarize native documents**](how-to/document-summarization.md)
 
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サマリー機能に関する概要ドキュメントの調整"
}
```

### Explanation
この変更は、Azure AI Languageの要約機能に関する概要ドキュメントに対して行われた微調整を示しています。主なポイントは以下の通りです：

1. **日付の更新**: ドキュメントの最終更新日が2025年2月17日から2025年3月5日に変更されています。このように日付を更新することで、情報が新しいものであることを示しています。

2. **文の簡略化と明確化**: 要約サービスに関する説明文がいくつかの部分で簡略化され、よりわかりやすく整理されています。特に、入力形式や要求される仕様に関する細かい点が明確にされ、ユーザーにとっての理解が容易になっています。

3. **機能間の区別を明確化**: 様々な要約形式（テキスト要約、会話要約、ネイティブドキュメント要約）の説明が明確に区別され、各形式がどのように機能するかが具体的に記載されています。また、文書要約がTEXT、PDF、Wordの形式をサポートすることが強調されています。

4. **参考リンクの更新**: ドキュメント内の参考リンクが更新され、関連情報へのアクセスが容易になるように整理されています。特に、ネイティブドキュメントのサポートに関する新しいリファレンスが追加されています。

5. **注釈の追加**: 読者に対するヒントや具体例が追加され、実際の使用方法に即した情報が提供されています。これにより、初心者でも実際にAPIを利用する際の手順が理解しやすくなっています。

この更新により、Azure AI Languageの要約サービスに関する情報がより整理され、明確になったことで、ユーザーはこれらの機能を簡単に理解し活用することができるようになります。

## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -430,10 +430,12 @@ items:
         displayName: Data privacy, logging, data retention
     - name: How-to guides
       items:
-      - name: Call PII
-        href: personally-identifiable-information/how-to-call.md
-      - name: Call PII for conversations
-        href: personally-identifiable-information/how-to-call-for-conversations.md
+      - name: Redact PII from text
+        href: personally-identifiable-information/how-to/redact-text-pii.md
+      - name: Redact PII from conversations
+        href: personally-identifiable-information/how-to/redact-conversation-pii.md
+      - name: Redact PII from native documents
+        href: personally-identifiable-information/how-to/redact-document-pii.md
       - name: Use containers
         items:
           - name: Use Docker containers
@@ -644,10 +646,12 @@ items:
       href: summarization/language-support.md
     - name: How-to guides
       items:
-      - name: Call the document summarization API
-        href: summarization/how-to/document-summarization.md
       - name: Call the conversation summarization API
         href: summarization/how-to/conversation-summarization.md
+      - name: Call the text summarization API
+        href: summarization/how-to/text-summarization.md
+      - name: Call the document summarization API
+        href: summarization/how-to/document-summarization.md
       - name: Use containers
         items:
         - name: Use Docker Containers
@@ -673,7 +677,7 @@ items:
       - name: Data, privacy, and security
         href: /legal/cognitive-services/language-service/data-privacy?context=/azure/ai-services/language-service/context/context
         displayName: Data privacy, logging, data retention
-          
+
 - name: Concepts
   items:
   - name: Developer guide
@@ -711,12 +715,12 @@ items:
     href: tutorials/prompt-flow.md
   - name: Native document support
     items:
-    - name: Use native documents for language processing
-      href: native-document-support/use-native-documents.md
+    - name: Native documents for language processing
+      href: native-document-support/overview.md
     - name: Create SAS tokens for storage containers
       href: native-document-support/shared-access-signatures.md
     - name: Create a managed identity for storage containers
-      href: native-document-support/managed-identities.md  
+      href: native-document-support/managed-identities.md
   - name: Scenario deep-dives
     items:
       - name: Call Center
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TOCの更新: PII関連のガイドと要約APIのリンクの整理"
}
```

### Explanation
この変更は、Azure AI Languageサービスに関連する目次（toc.yml）を更新し、個人情報の取り扱いや要約APIに関するガイドを整理したものです。主な変更点は以下の通りです：

1. **PII（個人情報）の取扱いに関する項目の更新**:
   - 「Call PII」と「Call PII for conversations」という項目が「Redact PII from text」、「Redact PII from conversations」、「Redact PII from native documents」という新しい名称に変更され、内容がより具体的に表現されています。これにより、ユーザーは具体的にどの情報を非表示にする操作ができるのかがわかりやすくなりました。

2. **要約APIに関するリンクの追加**: 
   - 「Call the text summarization API」という項目が新たに追加され、ユーザーがテキスト要約APIを利用する手順を明確に示すリンクが提供されるようになりました。

3. **ドキュメントへのリンク整理**:
   - 「Use native documents for language processing」という名称が「Native documents for language processing」に変更され、リンクも整理されています。これにより、ナビゲーションが改善され、関連情報を見つけやすくなっています。

4. **不要なパラメータの削除**:
   - 一部の不要な空行が削除され、全体の構成がより整然とした印象を与えるようになっています。

これらの変更により、ユーザーはAzure AI Languageサービスに関連する目次から求める情報にアクセスしやすくなり、特にPIIの取扱いや要約APIの利用に関する理解がしやすくなっています。

## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: whats-new
-ms.date: 10/04/2024
+ms.date: 03/05/2025
 ms.author: jboback
 ---
 
@@ -17,7 +17,7 @@ Azure AI Language is updated on an ongoing basis. To stay up-to-date with recent
 
 ## November 2024
 
-* [Native document support](native-document-support/use-native-documents.md) is now available in public preview `2024-11-15-preview` without gated preview limitations.
+* [Native document support](native-document-support/overview.md) is now available in public preview `2024-11-15-preview` without gated preview limitations.
 
 ## October 2024
 
@@ -26,7 +26,7 @@ Azure AI Language is updated on an ongoing basis. To stay up-to-date with recent
 ## September 2024
 
 * PII detection now has container support. See more details in the Azure Update post: [Announcing Text PII Redaction Container Release](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/announcing-text-pii-redaction-container-release/4264655).
-* Custom sentiment analysis (preview) will be retired on January 10th, 2025. Please transition to other custom model training services, such as custom text classification in Azure AI Language, by that date.  See more details in the Azure Update post: [Retirement: Announcing upcoming retirement of custom sentiment analysis (preview) in Azure AI Language (microsoft.com)](https://azure.microsoft.com/updates/v2/custom-sentiment-analysis-retirement).
+* Custom sentiment analysis (preview) will be retired January 10, 2025. You can transition to other custom model training services, such as custom text classification in Azure AI Language, by that date.  See more details in the Azure Update post: [Retirement: Announcing upcoming retirement of custom sentiment analysis (preview) in Azure AI Language (microsoft.com)](https://azure.microsoft.com/updates/v2/custom-sentiment-analysis-retirement).
 * Custom text analytics for health (preview) will be retired on January 10th, 2025. Please transition to other custom model training services, such as custom named entity recognition in Azure AI Language, by that date.  See more details in the Azure Update post: [Retirement: Announcing upcoming retirement of custom text analytics for health (preview) in Azure AI Language (microsoft.com)](https://azure.microsoft.com/updates/v2/custom-text-analytics-for-health-retirement).
 
 ## August 2024
@@ -38,15 +38,15 @@ Azure AI Language is updated on an ongoing basis. To stay up-to-date with recent
 * [Conversational PII redaction](https://techcommunity.microsoft.com/blog/ai-azure-ai-services-blog/announcing-conversational-pii-detection-service-s-general/4162881) service in English-language contexts is now Generally Available (GA).
 * Conversation Summarization now supports 12 additional languages in preview as listed [here](summarization/language-support.md).
 * Summarization Meeting or Conversation Chapter titles features will now support reduced length to focus on the key topics.
-* Enable support for data augmentation for diacritics to generate variations of training data for diacritic variations used in some natural languages which is especially useful for Germanic and Slavic languages. 
+* Enable support for data augmentation for diacritics to generate variations of training data for diacritic variations used in some natural languages which is especially useful for Germanic and Slavic languages.
 
 ## February 2024
 
 * Expanded [language detection](./language-detection/how-to/call-api.md#script-name-and-script-code) support for additional scripts according to the [ISO 15924 standard](https://wikipedia.org/wiki/ISO_15924) is now available starting in API version `2023-11-15-preview`.
 
 ## January 2024
 
-* [Native document support](native-document-support/use-native-documents.md) is now available in `2023-11-15-preview` public preview.
+* [Native document support](native-document-support/overview.md) is now available in `2023-11-15-preview` public preview.
 
 ## December 2023
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "最新情報ドキュメントの更新"
}
```

### Explanation
この変更は、Azure AI Languageサービスに関する「What's New」ドキュメントの情報を更新したものです。主な変更内容は以下のとおりです：

1. **日付の更新**: ドキュメントの最終更新日が2024年10月4日から2025年3月5日に変更され、最新の情報が反映されることを示しています。

2. **ネイティブドキュメントサポートのリンク変更**: 「Native document support」のリンクが「use-native-documents.md」から「overview.md」に変更され、ユーザーがより包括的な情報にアクセスできるようにしています。

3. **カスタムセンチメント分析のリタイアメント通知の文章修正**: カスタムセンチメント分析（プレビュー）のリタイア予定日が2025年1月10日であることは変わらないが、通知文が簡略化され、「Please transition to other custom model training services」という一文が削除されました。これにより、表現がよりシンプルになっています。

4. **その他の情報の整理**: 他のセクションにおいても、文の整理や一部の冗長な表現の削除が行われています。これにより、文書全体の明瞭さが向上し、重要なポイントに対する理解が容易になっています。

これらの更新により、Azure AI Languageの最新機能やサービスに関する情報が最新の状態になり、ユーザーにとって有益なリソースへのアクセスがしやすくなっています。


