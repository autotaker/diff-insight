---
date: '2025-09-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9037dee...MicrosoftDocs:de1cf56
summary: |-
  この差分は、Azure AIサービスのドキュメントに関する更新を示しています。主な変更点には、日付の更新、コマンド表示の統一、言語とモデルの対応範囲拡大、新機能の追加が含まれます。

  具体的には、ドキュメントインテリジェンスのREST APIガイドや会話型言語理解のコンテナ使用に関するガイドラインが最新情報に更新され、また、Azure AI Languageの新機能セクションでは、PIIと「NER」の新モデルが発表され、DateOfBirthエンティティの対応言語が拡大されました。

  破壊的変更は特にないものの、用語や記述の正確さおよび明確さが改善されています。その他の更新として、ドキュメントのリリース日が最新に更新され、cURLとPowerShellの表記が改善されたことで可読性が向上しました。

  この一連の更新は、Azure AIサービスが最新で正確な情報を提供し続ける意図を反映しており、特にユーザーエクスペリエンスを優先する設計がなされています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9037dee...MicrosoftDocs:de1cf56){target="_blank"}

<format>
# ハイライト
この差分は、Azure AIサービスのドキュメントに関する更新を示しています。主な変更点としては、日付の更新、コマンド表示の統一、言語とモデルの対応範囲拡大、新機能の追加などが含まれています。

## 新機能
- ドキュメントインテリジェンスのREST APIガイド、会話型言語理解のコンテナ使用、PIIの適応に関するガイドライン、およびAzure AI Languageの「新機能」セクションなど、各ドキュメントが最新情報に更新。
- Azure AI Languageでは、2025年8月のプレビューでPIIと「NER」の新モデルを発表し、DateOfBirthエンティティの対応言語を拡大。

## 破壊的変更
- 特に目立った破壊的変更はありませんが、用語や記述の正確さおよび明確さを改善した変更が多かったです。

## その他の更新
- ドキュメントのリリース日を最新の日付に更新。
- cURLとPowerShellに関する表記が改善され、可読性を向上。
- 誤解を生む可能性のある用語やプロセッサ情報の明確化が行われました。

# インサイト
この差分からは、Azure AIサービスがユーザーに対して最新で正確な情報を提供し続けようとする意図が読み取れます。特に、新機能や改善点に関する情報を明確かつ簡潔に記載することで、ユーザーに対するサポートを強化しています。

Azure AI Languageの更新では、新モデルや言語対応の拡大により、より多くの地域や異なるユーザー層に対して利便性を提供しようとする動きが見られます。また、新しいSDKと関連するAPIが導入され、より高速な技術進化に対応する形でサービスの向上を図っています。

この一連の更新は、特に複雑なAIサービスをより使いやすくするためのもので、技術者以外のユーザーにも容易に触れることができるように設計されていることがわかります。これは、ユーザーエクスペリエンスを優先する現代の技術文書作成の良い例と言えるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [rest-api.md](#item-9d952f) | minor update | ドキュメントインテリジェンスのREST APIに関する更新 | modified | 2 | 2 | 4 | 
| [use-containers.md](#item-77ab95) | minor update | コンテナの使用に関するドキュメントの更新 | modified | 17 | 15 | 32 | 
| [adapt-to-domain-pii.md](#item-62092f) | minor update | PIIドキュメントにおける使用ガイドラインの更新 | modified | 1 | 1 | 2 | 
| [whats-new.md](#item-69b272) | minor update | Azure AI Languageの新機能に関する更新 | modified | 20 | 2 | 22 | 


# Modified Contents
## articles/ai-services/document-intelligence/quickstarts/includes/rest-api.md{#item-9d952f}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: include
-ms.date: 07/17/2025
+ms.date: 07/21/2025
 ms.author: lajanuar
 ---
 
@@ -30,7 +30,7 @@ In this quickstart, learn to use the Document Intelligence REST API to analyze a
 
 * Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services)
 
-* cURL command-line tool installed.
+* The `cURL` command line tool installed.
 
 * **PowerShell version 7.*+** (or a similar command-line application.):
   * [Windows](/powershell/scripting/install/installing-powershell-on-windows)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスのREST APIに関する更新"
}
```

### Explanation
このコードの差分は、Azure AIサービスのドキュメントインテリジェンスに関するクイックスタートガイドのマークダウンファイルに対する小規模な更新を示しています。具体的には、2つの行が追加され、2つの行が削除されており、合計4つの変更が行われました。

主な更新内容は、以下の通りです：

1. ドキュメントの日付が「07/17/2025」から「07/21/2025」に変更されました。これは、ドキュメントの更新やリリース日を正確に反映するためのものです。
2. `cURL`コマンドラインツールの表記が「cURL command-line tool installed」から「The `cURL` command line tool installed」に変更されています。この修正は、文の読みやすさを向上させるためのものです。
3. PowerShellのバージョンについても言及があり、バージョン7に関する説明文が 編集されています。

これらの変更は、ドキュメントを最新の情報に保ち、ユーザーが必要なツールを正確かつ明確に理解できるようにすることを目的としています。

## articles/ai-services/language-service/conversational-language-understanding/how-to/use-containers.md{#item-77ab95}

<details>
<summary>Diff</summary>
````diff
@@ -39,9 +39,9 @@ The following table describes the minimum and recommended specifications for the
 
 We recommended that you have a CPU with AVX-512 instruction set, for the best experience (performance and accuracy).
 
-|     | Minimum host specs     | Recommended host specs |
+|  Processor   | Minimum host specs     | Recommended host specs |
 |---------------------|------------------------|------------------------|
-| **CLU**     | `1 core`, `2-GB memory`     | `4 cores`, `8-GB memory`    |
+| **CPU**     | 1-core, 2-GB memory     | 4-cores, 8-GB memory    |
 
 CPU core and memory correspond to the `--cpus` and `--memory` settings, which are used as part of the `docker run` command.
 
@@ -54,7 +54,7 @@ Before you proceed with running the docker image, you need to export your own tr
 |**{API_KEY}** |The key for your Language resource. You can find it on your resource's **Key and endpoint** page, on the Azure portal.|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|
 |**{ENDPOINT_URI}**|The endpoint for accessing the Conversational Language Understanding API. You can find it on your resource's **Key and endpoint** page, on the Azure portal.|`https://<your-custom-subdomain>.cognitiveservices.azure.com`|
 |**{PROJECT_NAME}**|The name of the project containing the model that you want to export. You can find it on your projects tab in the Language Studio portal.|myProject|
-|**{TRAINED_MODEL_NAME}** |The name of the trained model you want to export. You can find your trained models on your model evaluation tab under your project in the Language Studio portal|myTrainedModel
+|**{TRAINED_MODEL_NAME}** |The name of the trained model you want to export. You can find your trained models on your model evaluation tab under your project in the Language Studio portal|myTrainedModel|
 |**{EXPORTED_MODEL_NAME}** |The name to assign for the new exported model created.|myExportedModel |
 
 ```bash
@@ -74,8 +74,8 @@ The CLU container image can be found on the `mcr.microsoft.com` container regist
 
 The latest CLU container is available in several languages. To download the container for the English container, use the following command:
 
-```
-docker pull mcr.microsoft.com/azure-cognitive-services/language/clu:latest
+```bash
+  docker pull mcr.microsoft.com/azure-cognitive-services/language/clu:latest
 ```
 
 [!INCLUDE [Tip for using docker list](../../../includes/cognitive-services-containers-docker-list-tip.md)]
@@ -94,16 +94,18 @@ After the exported model is created, users have to run the container to download
 | **{PROJECT_NAME}**| Name of the project that the exported model belongs to  | myProject  |
 | **{EXPORTED_MODEL_NAME}**   | Exported model to be downloaded | myExportedModel   |
 
-```bash
-docker run --rm -it -p {LOCAL_CLU_PORT}:80 \
-mcr.microsoft.com/azure-cognitive-services/language/clu:{IMAGE_TAG} \ 
--v {LOCAL_MODEL_DIRECTORY}:/DeploymentPackage \
-Billing={ENDPOINT_URI} \ 
-ApiKey={API_KEY} \
-downloadmodel \
-projectName={PROJECT_NAME} \
-exportedModelName={EXPORTED_MODEL_NAME}
-```
+
+  
+  ```bash
+    docker run --rm -it -p {LOCAL_CLU_PORT}:80 \
+    mcr.microsoft.com/azure-cognitive-services/language/clu:{IMAGE_TAG} \ 
+    -v {LOCAL_MODEL_DIRECTORY}:/DeploymentPackage \
+    Billing={ENDPOINT_URI} \ 
+    ApiKey={API_KEY} \
+    downloadmodel \
+    projectName={PROJECT_NAME} \
+    exportedModelName={EXPORTED_MODEL_NAME}
+  ```
 
 DO NOT alter the downloaded files. Even altering the name or folder structure can affect the integrity of the container and might break it.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテナの使用に関するドキュメントの更新"
}
```

### Explanation
このコードの差分は、Azure AIサービスの会話型言語理解に関する「コンテナの使用」マニュアルの更新を示しています。この更新では、17行が追加され、15行が削除され、合計32行が変更されました。

主要な変更点は次のとおりです：

1. 表のヘッダーが「CLU」から「CPU」に変更され、プロセッサに関する正確な情報が反映されています。また、ホストの最小および推奨仕様がより明確に示されるようになりました。
2. 詳細なコマンドライン構文が追加され、コマンドを使用する際の可読性が向上しました。特に、Dockerコマンドの引数がそれぞれの行に分割されて見やすくなっています。
3. 一部の説明に対して、より明確かつ簡潔な文が使われており、理解が容易になっています。
4. コードブロック内の説明が強調され、ユーザーがモデルをエクスポートする方法についての指示がより直感的に示されています。

これらの変更は、ドキュメントが最新の情報に基づくものであり、ユーザーがコンテナを使用して会話型言語理解の機能を適切に利用できるようにすることを目的としています。

## articles/ai-services/language-service/personally-identifiable-information/how-to/adapt-to-domain-pii.md{#item-62092f}

<details>
<summary>Diff</summary>
````diff
@@ -42,7 +42,7 @@ Once you test the service with your own data, you can use `entitySynonyms` to:
 ## Usage guidelines
 
 1. Synonyms must be restricted to phrases that directly refer to the type, and preserve semantic correctness. For example, for the entity type `InternationalBankAccountNumber`, a valid synonym could be "Financial Account Number" or *FAN*. But, the word *deposit* though may be associated with type, as it doesn't directly have a meaning of a bank account number and therefore shouldn't be used.
-1. Synonyms should be country agnostic. For example, *German passport* wouldn't be helpful to include.
+1. Synonyms should be country/region agnostic. For example, *German passport* wouldn't be helpful to include.
 1. Synonyms can't be reused for more than one entity type.
 1. This synonym recognition feature only accepts a subset of entity types supported by the service. The supported entity types and example synonyms include:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PIIドキュメントにおける使用ガイドラインの更新"
}
```

### Explanation
このコードの差分は、個人を特定できる情報（PII）の適応に関するマニュアルの使用ガイドラインに対する小規模な更新を示しています。具体的には、1行が追加され、1行が削除されており、合計2行が変更されました。

主要な変更点は以下の通りです：

1. 使用ガイドラインの最初のポイントにおいて、「国に依存しない」という表現が「国/地域に依存しない」と変更されました。この修正により、ガイドラインが国だけでなく地域にも適応することが強調されています。
2. 文言の調整により、言語のフォーマリティが向上し、より明確になっています。

この変更は、ガイドラインの適用範囲を広げ、ユーザーがより柔軟にシノニム（同義語）の使用を理解できるようにすることを目的としています。

## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -6,17 +6,35 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: whats-new
-ms.date: 07/16/2025
+ms.date: 09/04/2025
 ms.author: lajanuar
 ---
 
 # What's new in Azure AI Language?
 
 Azure AI Language is updated on an ongoing basis. Bookmark this page to stay up to date with release notes, feature enhancements, and our newest documentation.
 
+## August 2025
+
+**Release of new PII and NER model (2025-08-01-preview)**. This new preview model version introduces broader functionality and expanded capabilities for personal information identification (PII) and named entity recognition (NER):
+
+* **Expanded language support for DateOfBirth entity**. The **DateOfBirth** entity, which initially supported English only, now includes Tier 1 language coverage. This expansion supports French, German, Italian, Spanish, Portuguese, Brazilian Portuguese, and Dutch, ensuring broader international applicability.
+
+* **Two new entity types added**:
+   * **SortCode**: A financial identifier used in the UK and Ireland to specify the bank and branch associated with an account.
+   * **LicensePlateNumber**: Support is now available for standard alphanumeric vehicle identification codes. At this time, license plates that consist exclusively of letters aren't supported.
+
+* **Improved AI accuracy in financial entity recognition**. The **2025-08-01-preview** model is further optimized to minimize both false positives and false negatives in financial entity recognition, resulting in greater accuracy and reliability.
+
+**New Python SDK release: azure-ai-language-conversations 2.0.0b1**. The latest Python SDK, **azure-ai-language-conversations 2.0.0b1**, is now available and supports the **2025-15-05-preview** REST API for conversation runtime.
+
+* **Conversational Language Understanding (CLU) inference** now allows for seamless integration with advanced large-scale language models, providing real-time recognition of user intent without the need for extra model training.
+* **Enhanced intent prediction capabilities** enable support for complex, multi-turn conversations. iThese advancements contribute to greater sophistication in conversational AI systems and, as a result, workflow automation processes are improved.
+
+
 ## July 2025
 
- **Expanded .NET SDK support for text and conversation authoring APIs**:
+ **Expanded .NET SDK support for text and conversation authoring APIs**. 
 
   * [**Azure.AI.Language.Text.Authoring `1.0.0-beta.2`**](https://www.nuget.org/packages/Azure.AI.Language.Text.Authoring/1.0.0-beta.2) now supports project import with raw JSON string for custom NER and custom text classification.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Languageの新機能に関する更新"
}
```

### Explanation
このコードの差分は、Azure AI Languageの「新機能」に関するドキュメントの更新を示しています。主に、20行が追加され、2行が削除され、合計22行が変更されました。

主要な変更点は次の通りです：

1. 更新日が「2025年7月16日」から「2025年9月4日」に変更されました。これは、文書のタイムスタンプを最新の状態に保つためのものです。
2. 2025年8月の新機能として、個人情報識別（PII）と命名体認識（NER）の新しいモデルが発表されました。このプレビュー版では、機能の拡張と能力の充実が強調されています。
   - **DateOfBirthエンティティの言語サポートが拡大**され、英語だけでなく、フランス語、ドイツ語、イタリア語、スペイン語、ポルトガル語、ブラジルポルトガル語、オランダ語に対応するようになりました。
   - **新しいエンティティタイプ**が追加され、「SortCode」と「LicensePlateNumber」がサポートされています。これにより、UKおよびアイルランドの銀行情報や車両識別情報の認識能力が向上しました。
   - 金融エンティティ認識における**AIの精度が改善**され、誤検出が減少したことが報告されています。
3. 新しいPython SDK **azure-ai-language-conversations 2.0.0b1**が公開され、これが**2025年5月15日プレビューAPI**に対応している旨が記載されています。

これらの変更は、Azure AI Languageが常に進化しており、新機能や改善点についてユーザーに正確で最新の情報を提供することを目指しています。


