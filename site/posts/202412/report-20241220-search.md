---
date: '2024-12-20'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6ebedb4...MicrosoftDocs:53fdfa0
summary: このコード差分では、Azure AI Searchに関連するドキュメントに対して、プライベート実行環境やマルチテナント環境についてのリンクと表現の修正が行われました。主な目的は、情報の正確性とアクセス性の向上です。文書内の用語やリンクが見直され、より確実に正確な情報にアクセスできるよう配慮されています。新機能の追加はありませんが、用語の変更、リンクの更新、情報の追加などによって、文書の質が向上しています。全体として、ユーザーが情報を得る際の体験を改善し、信頼性のある情報を提供することを目指しています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6ebedb4...MicrosoftDocs:53fdfa0){target="_blank"}

# ハイライト

このコード差分では、Azure AI Searchに関連する複数のドキュメントに対するマイナーな更新が行われました。主な内容は、プライベート実行環境やマルチテナント環境に関するリンクや表現を修正し、情報の正確性とアクセス性を向上させることです。多数のドキュメントは、用語やリンクを見直し、ユーザーがより確実に正しい情報にアクセスできるように配慮されています。

## 新機能

特に新しい機能が追加されたわけではありませんが、文書の質を向上させるための細かい修正が施されています。

## 破壊的変更

特に破壊的変更はありません。すべての更新は現行の文書の改善に焦点を当てたマイナーアップデートです。

## その他の更新

- 用語の修正（「text-to-vector embeddings」から「vectorization」への変更など）。
- リンクの更新と正確性の向上。
- 詳細情報の追加による文書の明確化。

# インサイト

このコード差分は、Azure AI Search関連のドキュメントをより使いやすくし、ユーザーに正確な情報を提供することを目的としています。特に、実行環境に関するリンクと用語の更新は、ユーザーがドキュメントを通じて情報を得る際の体験を改善するために重要です。これにより、ユーザーは異なる実行環境がどのように動作し、それがシステムにどのように影響するかについて、より深く理解できるようになります。

リンクの更新は、ドキュメント内の情報の整合性を維持し、ユーザーが誤解されないように設計されています。また、マイナーな用語の修正は、技術的な正確さを保証するためにも重要です。情報は常に進化しているため、こうした小さな調整もユーザーにとっては重要なアップデートとなることでしょう。

このような細かい更新が積み重なることで、Azure AI Searchのドキュメント全体がより信頼性のあるものとなり、ユーザーが必要とする情報を容易に得られる環境が整備されています。技術者および開発者が自らのプロジェクトに適切な選択を行うための手助けとなり得る、良い改善と言えるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-attach-cognitive-services.md](#item-68eaec) | minor update | プライベート実行環境に関する表現の修正 | modified | 1 | 1 | 2 | 
| [cognitive-search-defining-skillset.md](#item-e2d71d) | minor update | 実行環境に関するリンクの更新 | modified | 1 | 1 | 2 | 
| [search-get-started-rbac.md](#item-9d96c1) | minor update | アクセストークン生成とトラブルシューティングの情報追加 | modified | 11 | 2 | 13 | 
| [search-how-to-create-indexers.md](#item-de71fb) | minor update | 実行環境へのリンクの更新 | modified | 1 | 1 | 2 | 
| [search-how-to-large-index.md](#item-d34e42) | minor update | マルチテナント環境へのリンクの更新 | modified | 1 | 1 | 2 | 
| [search-howto-run-reset-indexers.md](#item-fb10c8) | minor update | インデクサ実行環境に関する内容の追加およびリンクの修正 | modified | 6 | 4 | 10 | 
| [search-howto-schedule-indexers.md](#item-d57e7b) | minor update | 実行環境に関する用語の修正 | modified | 1 | 1 | 2 | 
| [search-indexer-how-to-access-private-sql.md](#item-1bd4cc) | minor update | インデクサ実行環境に関する用語の明確化 | modified | 2 | 2 | 4 | 
| [search-indexer-howto-access-ip-restricted.md](#item-aec22f) | minor update | マルチテナント実行環境のリンク修正 | modified | 1 | 1 | 2 | 
| [search-indexer-howto-access-private.md](#item-73d30d) | minor update | プライベートリンクとインデクサ関連のリンク修正 | modified | 5 | 5 | 10 | 
| [search-indexer-overview.md](#item-292796) | minor update | インデクサの概要に関する内容の更新 | modified | 6 | 6 | 12 | 
| [search-indexer-securing-resources.md](#item-c075c4) | minor update | ネットワークアクセスとインデクサ実行環境の説明の更新 | modified | 5 | 5 | 10 | 
| [search-indexer-troubleshooting.md](#item-087365) | minor update | マルチテナント実行環境に関するリンクの更新 | modified | 1 | 1 | 2 | 
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | インデクサの最大実行時間の説明の修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/cognitive-search-attach-cognitive-services.md{#item-68eaec}

<details>
<summary>Diff</summary>
````diff
@@ -274,7 +274,7 @@ Billing goes into effect when API calls to Azure AI services resources exceed 20
 
 Keyless and key-based connections are used for billing, but not for enrichment operations' connections. For connections, a search service [connects over the internal network](search-security-overview.md#internal-traffic) to an Azure AI services resource that's located in the [same physical region](search-region-support.md). Most regions that offer Azure AI Search also offer other Azure AI services such as Language. If you attempt AI enrichment in a region that doesn't have both services, you'll see this message: "Provided key isn't a valid CognitiveServices type key for the region of your search service."
 
-Indexers can be configured to run in a [private execution environment](search-howto-run-reset-indexers.md#indexer-execution) for dedicated processing using just the search nodes of your own search service. Even if you're using private execution environment, Azure AI Search still uses its internally provisioned Azure AI multiservice resource to perform all skill enrichments.
+Indexers can be configured to run in a [private execution environment](search-howto-run-reset-indexers.md#indexer-execution-environment) for dedicated processing using just the search nodes of your own search service. Even if you're using private execution environment, Azure AI Search still uses its internally provisioned Azure AI multiservice resource to perform all skill enrichments.
 
 > [!NOTE]
 > Some built-in skills are based on non-regional Azure AI services (for example, the [Text Translation Skill](cognitive-search-skill-text-translation.md)). Using a non-regional skill means that your request might be serviced in a region other than the Azure AI Search region. For more information on non-regional services, see the [Azure AI services product by region](https://aka.ms/allinoneregioninfo) page.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベート実行環境に関する表現の修正"
}
```

### Explanation
このコードの差分は、ドキュメント内の特定の文言を微調整したものです。特に、プライベート実行環境に関する説明のリンク先が更新され、文脈に合わせて正確な表現を用いるための修正が行われています。具体的には、「search-howto-run-reset-indexers.md#indexer-execution」というリンクが「search-howto-run-reset-indexers.md#indexer-execution-environment」に変更されました。これにより、ユーザーがより正確な情報にアクセスできるようになっています。全体として、この変更はわずか1行の追加と1行の削除を伴うマイナーなアップデートです。

## articles/search/cognitive-search-defining-skillset.md{#item-e2d71d}

<details>
<summary>Diff</summary>
````diff
@@ -75,7 +75,7 @@ After the name and description, a skillset has four main properties:
 
 Inside the skillset definition, the skills array specifies which skills to execute. Three to five skills are common, but you can add as many skills as necessary, subject to [service limits](search-limits-quotas-capacity.md#indexer-limits).
 
-The end result of an enrichment pipeline is textual content in either a search index or a knowledge store. For this reason, most skills either create text from images (OCR text, captions, tags), or analyze existing text to create new information (entities, key phrases, sentiment). Skills that operate independently are processed in parallel. Skills that depend on each other specify the output of one skill (such as key phrases) as the input of a second skill (such as text translation). The search service determines the order of skill execution and the execution environment.
+The end result of an enrichment pipeline is textual content in either a search index or a knowledge store. For this reason, most skills either create text from images (OCR text, captions, tags), or analyze existing text to create new information (entities, key phrases, sentiment). Skills that operate independently are processed in parallel. Skills that depend on each other specify the output of one skill (such as key phrases) as the input of a second skill (such as text translation). The search service determines the order of skill execution and the [execution environment](search-howto-run-reset-indexers.md#indexer-execution-environment).
 
 All skills have a type, context, inputs, and outputs. A skill might optionally have a name and description. The following example shows two unrelated [built-in skills](cognitive-search-predefined-skills.md) so that you can compare the basic structure.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "実行環境に関するリンクの更新"
}
```

### Explanation
このコードの差分は、ドキュメント内でスキルセットの定義に関する説明を微調整したものです。具体的には、エンリッチメントパイプラインの最終結果についての説明において、実行環境へのリンクが追加され、「search-howto-run-reset-indexers.md#indexer-execution」という部分が「search-howto-run-reset-indexers.md#indexer-execution-environment」に修正されました。この変更により、読者はどのようにスキルが実行されるか、およびその実行環境についての具体的な情報に簡単にアクセスできるようになります。全体として、この変更は1行の追加と1行の修正を伴うマイナーなアップデートです。

## articles/search/search-get-started-rbac.md{#item-9d96c1}

<details>
<summary>Diff</summary>
````diff
@@ -120,7 +120,7 @@ Several quickstarts and tutorials use a REST client, such as Visual Studio Code
 
 You should have a `.rest` or `.http` file, similar to the one described in [Quickstart: Vector search](search-get-started-vector.md).
 
-1. Get an access token:
+1. Generate an access token.
 
    ```azurecli
    az account get-access-token --scope https://search.azure.com/.default --query accessToken --output tsv
@@ -149,13 +149,22 @@ You should have a `.rest` or `.http` file, similar to the one described in [Quic
          }
    ```
 
-If the call fails, revisit the previous steps to make sure you didn't skip any. You might also want to restart your device.
+### Troubleshoot 401 errors
+
+- Check the active subscription and tenant (`az account show`) and make sure it's valid for your search service.
+
+- Check the search service **Settings** > **Keys** options in the Azure portal and confirm the service is configured for **Both"** or **Role-based access control**.
+
+- For the REST client only: Check the token and endpoint specified in your file and make sure there's no surrounding quotes or extra spaces.
+
+If all else fails, restart your device to remove any cached tokens, and then repeat the steps in this section, starting with `az login`.
 
 ## Additional configuration
 
 Configure a managed identity for outbound connections:
 
 - [Configure a system-assigned or user-assigned managed identity](search-howto-managed-identities-data-sources.md) for your search service.
+
 - [Use role assignments](keyless-connections.md) to authorize access to other Azure resources.
 
 Network access configuration:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "アクセストークン生成とトラブルシューティングの情報追加"
}
```

### Explanation
このコードの差分は、RBAC（ロールベースのアクセス制御）に関するドキュメントを更新し、アクセストークンの生成手順およびトラブルシューティングに関する詳細情報を追加したものです。具体的には、アクセストークンを取得するステップのタイトルが「Get an access token」から「Generate an access token」に変更され、さらに401エラーのトラブルシューティングセクションを新たに追加しました。このセクションでは、Azureポータルの設定を確認する方法や、トークンとエンドポイントの確認手順など、具体的な解決策が示されています。全体として、これによりユーザーは問題解決のための具体的なガイダンスを得ることができ、手順の明確さが向上しました。変更は11行の追加と2行の削除を伴うマイナーなアップデートです。

## articles/search/search-how-to-create-indexers.md{#item-de71fb}

<details>
<summary>Diff</summary>
````diff
@@ -197,7 +197,7 @@ POST /indexers?api-version=[api-version]
 }
 ```
 
-Parameters are used to set the batch size and how to handle processing failures. The [execution environment](search-howto-run-reset-indexers.md#indexer-execution) determines whether indexer and skillset processing can use the multitenant capabilities provided by Microsoft or the private processing nodes allocated exclusively to your search service. If your search service is Standard2 or higher, you can set `executionEnvironment` to private to pin all indexer processing to just your search service clusters.
+Parameters are used to set the batch size and how to handle processing failures. The [execution environment](search-howto-run-reset-indexers.md#indexer-execution-environment) determines whether indexer and skillset processing can use the multitenant capabilities provided by Microsoft or the private processing nodes allocated exclusively to your search service. If your search service is Standard2 or higher, you can set `executionEnvironment` to private to pin all indexer processing to just your search service clusters.
 
 There are numerous tutorials and examples that demonstrate REST clients for creating objects. [Quickstart: Text search using REST](search-get-started-rest.md) can get you started.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "実行環境へのリンクの更新"
}
```

### Explanation
このコードの差分は、インデクサの作成方法に関するドキュメントを微調整したもので、実行環境に関するリンクが更新されました。具体的には、元のリンク「search-howto-run-reset-indexers.md#indexer-execution」が「search-howto-run-reset-indexers.md#indexer-execution-environment」に修正され、より正確な情報を提供します。この変更によりユーザーは、インデクサとスキルセットの処理がどのように行われるかを知るための適切なドキュメントにアクセスできるようになります。全体として、この変更は1行の追加と1行の修正を伴うマイナーなアップデートです。

## articles/search/search-how-to-large-index.md{#item-d34e42}

<details>
<summary>Diff</summary>
````diff
@@ -97,7 +97,7 @@ When there are no longer any new or updated documents in the data source, indexe
 For more information about setting schedules, see [Create Indexer REST API](/rest/api/searchservice/indexers/create) or see [Schedule indexers for Azure AI Search](search-howto-schedule-indexers.md).
 
 > [!NOTE]
-> Some indexers that run on an older runtime architecture have a 24-hour rather than 2-hour maximum processing window. The two-hour limit is for newer content processors that run in an [internally managed multi-tenant environment](search-indexer-securing-resources.md#indexer-execution-environment). Whenever possible, Azure AI Search tries to offload indexer and skillset processing to the multi-tenant environment. If the indexer can't be migrated, it runs in the private environment and it can run for as long as 24 hours. If you're scheduling an indexer that exhibits these characteristics, assume a 24-hour processing window.
+> Some indexers that run on an older runtime architecture have a 24-hour rather than 2-hour maximum processing window. The two-hour limit is for newer content processors that run in an [internally managed multitenant environment](search-howto-run-reset-indexers.md#indexer-execution-environment). Whenever possible, Azure AI Search tries to offload indexer and skillset processing to the multi-tenant environment. If the indexer can't be migrated, it runs in the private environment and it can run for as long as 24 hours. If you're scheduling an indexer that exhibits these characteristics, assume a 24-hour processing window.
 
 <a name="parallel-indexing"></a>
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチテナント環境へのリンクの更新"
}
```

### Explanation
このコードの差分は、大規模インデックスに関するドキュメントの更新を示しており、インデクサの処理時間に関するノート部分のリンクが修正されました。具体的には、元のリンク「search-indexer-securing-resources.md#indexer-execution-environment」が「search-howto-run-reset-indexers.md#indexer-execution-environment」に更新され、より正確な情報源への導線が提供されています。これにより、ユーザーはインデクサの実行環境についての最新情報を得ることができ、インデクシングプロセスの理解を深めることができます。変更は1行の追加と1行の修正を含むマイナーなアップデートです。

## articles/search/search-howto-run-reset-indexers.md{#item-fb10c8}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 10/25/2024
+ms.date: 12/19/2024
 ---
 
 # Run or reset indexers, skills, or documents
@@ -38,16 +38,18 @@ Once indexer execution starts, you can't pause or stop it. Indexer execution sto
 
 You can run multiple indexers at one time assuming sufficient capacity, but each indexer itself is single-instance. Starting a new instance while the indexer is already in execution produces this error: `"Failed to run indexer "<indexer name>" error: "Another indexer invocation is currently in progress; concurrent invocations are not allowed."`
 
+## Indexer execution environment
+
 An indexer job runs in a managed execution environment. Currently, there are two environments:
 
-+ A private execution environment runs on search clusters that are specific to your search service. If your search service is Standard2 or nigher, you can [set the `executionEnvironment` parameter](search-how-to-create-indexers.md?tabs=indexer-rest#create-an-indexer) in the indexer definition to always run an indexer in the private execution environment. 
++ A private execution environment runs on search clusters that are specific to your search service. If your search service is Standard2 or higher, you can [set the `executionEnvironment` parameter](search-how-to-create-indexers.md?tabs=indexer-rest#create-an-indexer) in the indexer definition to always run an indexer in the private execution environment. 
 
 + A multitenant environment has content processors that are managed and secured by Microsoft at no extra cost. This environment is used to offload computationally intensive processing, leaving service-specific resources available for routine operations. Whenever possible, most skillsets execute in the multitenant environment. This is the default.
 
-  Computationally intensive processing includes skillsets running on content processors, and high volume indexer jobs or indexer jobs with large documents. Non-skillset processing on the multitenant content processors is determined by hueristics and system information and isn't under customer control. S2 services and higher support pinning an indexer and skillset processing exclusively to your search clusters through the `executionEnvironment` parameter.
+  *Computationally intensive processing* refers to skillsets running on content processors and indexer jobs that process a high volume of documents, or documents of a large size. Non-skillset processing on the multitenant content processors is determined by hueristics and system information and isn't under customer control. S2 services and higher support pinning an indexer and skillset processing exclusively to your search clusters through the `executionEnvironment` parameter.
 
   > [!NOTE]
-  > [IP firewalls](search-indexer-securing-resources.md#indexer-execution-environment) block the multitenant environment, so if you have a firewall, create a rule that allows multitenant processing.
+  > [IP firewalls](search-indexer-securing-resources.md#network-access-and-indexer-execution-environments) block the multitenant environment, so if you have a firewall, create a rule that allows multitenant processing.
 
 Indexer limits vary for each environment:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサ実行環境に関する内容の追加およびリンクの修正"
}
```

### Explanation
このコードの差分は、インデクサの実行またはリセットに関するドキュメントに対する更新を示しており、インデクサの実行環境に関するセクションが充実しました。具体的には、マルチテナント環境とプライベート実行環境についての説明が追加され、コンピュータリソースのオフロードと処理能力の管理方法について詳細が提供されています。また、いくつかの記述にリンクや表現の修正が加えられており、正確性と明瞭さが向上しています。これにより、ユーザーはインデクサ実行環境の選択肢やその影響についてより良い理解を得られるようになります。変更は、6行の追加と4行の削除を伴い、全体として10行の変更が行われています。

## articles/search/search-howto-schedule-indexers.md{#item-d57e7b}

<details>
<summary>Diff</summary>
````diff
@@ -111,7 +111,7 @@ You can run multiple indexers simultaneously, but each indexer is single instanc
 
 For text-based indexing, the scheduler can kick off as many indexer jobs as the search service supports, which is determined by the number of [search units](search-capacity-planning.md#concepts-search-units-replicas-partitions). For example, if the service has three replicas and four partitions, you can have 12 indexer jobs in active execution, whether initiated on demand or on a schedule.
 
-For skills-based indexing, indexers run in a specific [execution environment](search-howto-run-reset-indexers.md#indexer-execution). For this reason, the number of service units has no bearing on the number of skills-based indexer jobs you can run. Multiple skills-based indexers can run in parallel, but doing so depends on content processor availability within the execution environment.
+For skills-based indexing, indexers run in a specific [execution environment](search-howto-run-reset-indexers.md#indexer-execution-environment). For this reason, the number of service units has no bearing on the number of skills-based indexer jobs you can run. Multiple skills-based indexers can run in parallel, but doing so depends on content processor availability within the execution environment.
 
 **Do scheduled jobs always start at the designated time?**
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "実行環境に関する用語の修正"
}
```

### Explanation
このコードの差分は、インデクサのスケジューリングに関するドキュメントの一部更新を示しており、スキルベースのインデクシングに関連する実行環境についての表現が修正されました。具体的には、「実行環境」のリンクテキストが「indexer-execution」から「indexer-execution-environment」に変更されています。この修正により、ドキュメントの正確性が向上し、ユーザーがインデクサの実行環境に関する詳細情報にアクセスしやすくなります。変更は1行の追加と1行の削除を含むマイナーなアップデートで、計2行の修正が行われています。

## articles/search/search-indexer-how-to-access-private-sql.md{#item-1bd4cc}

<details>
<summary>Diff</summary>
````diff
@@ -151,9 +151,9 @@ This article assumes a [REST client](search-get-started-rest.md) and uses the RE
      }
     ```
 
-1. [Create the indexer definition](search-howto-create-indexers.md), setting the indexer execution environment to "private".
+1. [Create the indexer definition](search-howto-create-indexers.md), setting the indexer `executionEnvironment` to "private".
 
-   [Indexer execution](search-indexer-securing-resources.md#indexer-execution-environment) occurs in either a private environment that's specific to the search service, or a multi-tenant environment that's used internally to offload expensive skillset processing for multiple customers. **When connecting over a private endpoint, indexer execution must be private.**
+   [Indexer execution](search-howto-run-reset-indexers.md#indexer-execution-environment) occurs in either a private execution environment that's specific to your search service, or a multi-tenant environment hosted by Microsoft and used to offload expensive skillset processing for multiple customers. **When connecting over a private endpoint, indexer execution must be private.**
 
    ```http
     POST https://myservice.search.windows.net/indexers?api-version=2024-07-01
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサ実行環境に関する用語の明確化"
}
```

### Explanation
このコードの差分は、プライベートSQLにアクセスするためのインデクサ設定に関するドキュメントの更新を示しています。具体的には、「インデクサ実行環境」の設定に関する表現が明確化されました。まず、インデクサの実行環境を指定する際の用語が「indexer execution environment」から「indexer `executionEnvironment`」に変更され、より具体的な記述がされています。また、インデクサ実行の説明に関連するリンクが変更され、適切なリンクに更新されています。これにより、ユーザーはプライベートエンドポイントを介しての接続においてインデクサの実行がプライベートである必要があることを理解しやすくなっています。変更は2行の追加と2行の削除を伴い、計4行の修正が行われています。

## articles/search/search-indexer-howto-access-ip-restricted.md{#item-aec22f}

<details>
<summary>Diff</summary>
````diff
@@ -80,7 +80,7 @@ For ping, the request times out, but the IP address is visible in the response.
 
 ## Get IP addresses for "AzureCognitiveSearch" service tag
 
-You'll also need to create an inbound rule that allows requests from the [multitenant execution environment](search-indexer-securing-resources.md#indexer-execution-environment). This environment is managed by Microsoft and it's used to offload processing intensive jobs that could otherwise overwhelm your search service. This section explains how to get the range of IP addresses needed to create this inbound rule.
+You'll also need to create an inbound rule that allows requests from the [multitenant execution environment](search-indexer-securing-resources.md#network-access-and-indexer-execution-environments). This environment is managed by Microsoft and it's used to offload processing intensive jobs that could otherwise overwhelm your search service. This section explains how to get the range of IP addresses needed to create this inbound rule.
 
 An IP address range is defined for each region that supports Azure AI Search. Specify the full range to ensure the success of requests originating from the multitenant execution environment. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチテナント実行環境のリンク修正"
}
```

### Explanation
このコードの差分は、IP制限されたインデクサへのアクセスに関するドキュメントの内容を更新したもので、特に「マルチテナント実行環境」に関連するリンクが修正されました。具体的には、元のリンク「indexer-execution-environment」が「network-access-and-indexer-execution-environments」に変更されています。この更新により、ユーザーは正確で最新の情報にアクセスできるようになります。また、ドキュメント全体として、マルチテナント環境がマイクロソフトによって管理され、リソースがオフロードされる経緯についての説明は変わっていません。この修正は、1行の追加と1行の削除を含むマイナーなアップデートであり、全体で2行の修正が行われています。

## articles/search/search-indexer-howto-access-private.md{#item-73d30d}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 12/10/2024
+ms.date: 12/19/2024
 ---
 
 # Make outbound connections through a shared private link
@@ -28,7 +28,7 @@ Shared private link is a premium feature that's billed by usage. When you set up
 
 Azure AI Search makes outbound calls to other Azure resources in the following scenarios:
 
-+ Indexer or search engine connections to Azure OpenAI for text-to-vector embeddings
++ Indexer or query connections to Azure OpenAI, Azure AI Vision, or the Azure AI Foundry model catalog for vectorization
 + Indexer connections to supported data sources
 + Indexer (skillset) connections to Azure Storage for caching enrichments, debug session sate, or writing to a knowledge store
 + Indexer (skillset) connections to Azure AI services for billing purposes
@@ -53,7 +53,7 @@ There are two scenarios for using [Azure Private Link](/azure/private-link/priva
 
 + Scenario one: create a shared private link when an *outbound* (indexer) connection to Azure requires a private connection.
 
-+ Scenario two: [configure search for a private *inbound* connection](service-create-private-endpoint.md) from clients that run in a virtual network. 
++ Scenario two: [configure search for a private *inbound* connection](service-create-private-endpoint.md) from clients that run in a virtual network.
 
 Scenario one is covered in this article.
 
@@ -65,7 +65,7 @@ When evaluating shared private links for your scenario, remember these constrain
 
 + Several of the resource types used in a shared private link are in preview. If you're connecting to a preview resource (Azure Database for MySQL or Azure SQL Managed Instance), use a preview version of the Management REST API to create the shared private link. These versions include `2020-08-01-preview`, `2021-04-01-preview`, `2024-03-01-preview`, and `2024-06-01-preview`. We recommend the latest preview API.
 
-+ Indexer execution must use the private execution environment that's specific to your search service. Private endpoint connections aren't supported from the multitenant content processing environment. The configuration setting for this requirement is covered in this article.
++ Indexer execution must use the [private execution environment](search-howto-run-reset-indexers.md#indexer-execution-environment) that's specific to your search service. Private endpoint connections aren't supported from the multitenant content processing environment. The configuration setting for this requirement is covered in this article.
 
 + Review shared private link [resource limits for each tier](search-limits-quotas-capacity.md#shared-private-link-resource-limits).
 
@@ -360,7 +360,7 @@ If the provisioning state (`properties.provisioningState`) of the resource is "S
 
 ## 4 - Configure the indexer to run in the private environment
 
-[Indexer execution](search-indexer-securing-resources.md#indexer-execution-environment) occurs in either a private environment that's specific to the search service, or a multitenant environment that's used internally to offload expensive skillset processing for multiple customers. 
+[Indexer execution](search-howto-run-reset-indexers.md#indexer-execution-environment) occurs in either a private environment that's specific to the search service, or a multitenant environment that's used internally to offload expensive skillset processing for multiple customers. 
 
 The execution environment is transparent, but once you start building firewall rules or establishing private connections, you must take indexer execution into account. For a private connection, configure indexer execution to always run in the private environment. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベートリンクとインデクサ関連のリンク修正"
}
```

### Explanation
このコードの差分は、プライベートにアクセスするためのインデクサに関する記事の更新を反映しています。主な変更点は、いくつかの用語やリンクの修正です。まず、更新された日付が「2024年12月10日」から「2024年12月19日」に変更されています。また、Azure OpenAIやAzure AI Vision、Azure AI Foundryモデルカタログへの接続の表現が明確化されています。以前は「text-to-vector embeddings」と表記されていたのが、より具体的に「vectorization」となりました。

さらに、プライベート実行環境に関する説明も強化されており、関連するリンクが「search-indexer-securing-resources.md」から「search-howto-run-reset-indexers.md」に変更されています。これにより、ユーザーが正確で役立つ情報にアクセスしやすくなっています。全体としては5行の追加と5行の削除を含むマイナーなアップデートで、合計で10行の変更が行われています。

## articles/search/search-indexer-overview.md{#item-292796}

<details>
<summary>Diff</summary>
````diff
@@ -10,18 +10,18 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 08/19/2024
+ms.date: 12/19/2024
 ---
 
 # Indexers in Azure AI Search
 
 An *indexer* in Azure AI Search is a crawler that extracts textual data from cloud data sources and populates a search index using field-to-field mappings between source data and a search index. This approach is sometimes referred to as a 'pull model' because the search service pulls data in without you having to write any code that adds data to an index. 
 
-Indexers also drive [skillset execution and AI enrichment](cognitive-search-concept-intro.md), where you can configure skills to integrate extra processing of content en route to an index. A few examples are OCR over image files, text split skill for data chunking, text translation for multiple languages.
+Indexers also drive [skillset execution and AI enrichment](cognitive-search-concept-intro.md), where you can configure skills to integrate extra processing of content en route to an index. A few examples are OCR over image files, text split skill for data chunking, and calling embedding models to generate vectors for vector search.
 
-Indexers target [supported data sources](#supported-data-sources). An indexer configuration specifies a data source (origin) and a search index (destination). Several sources, such as Azure Blob Storage, have more configuration properties specific to that content type.
+Indexers target [supported data sources](#supported-data-sources). An indexer configuration specifies a data source (origin) and a search index (destination). Several sources, such as Azure Blob Storage, have more indexer configuration properties specific to that content type.
 
-You can run indexers on demand or on a recurring data refresh schedule that runs as often as every five minutes. More frequent updates require a ['push model'](search-what-is-data-import.md) that simultaneously updates data in both Azure AI Search and your external data source.
+You can run indexers on demand or on a recurring data refresh schedule that runs as often as every five minutes. More frequent updates preclude the use of indexers, requiring that you implement a ['push model'](search-what-is-data-import.md) that simultaneously pushes data to both Azure AI Search and your external data source for data synchronization.
 
 A search service runs one indexer job per search unit. If you need concurrent processing, make sure you have [sufficient replicas](/azure/search/search-capacity-planning#add-or-reduce-replicas-and-partitions). Indexers don't run in the background, so you might detect more query throttling than usual if the service is under pressure.
 
@@ -32,8 +32,8 @@ You can use an indexer as the sole means for data ingestion, or in combination w
 | Scenario |Strategy |
 |----------|---------|
 | Single data source | This pattern is the simplest: one data source is the sole content provider for a search index. Most supported data sources provide some form of change detection so that subsequent indexer runs pick up the difference when content is added or updated in the source. |
-| Multiple data sources | An indexer specification can have only one data source, but the search index itself can accept content from multiple sources, where each indexer run brings new content from a different data provider. Each source can contribute its share of full documents, or populate selected fields in each document. For a closer look at this scenario, see [Tutorial: Index from multiple data sources](tutorial-multiple-data-sources.md). |
-| Multiple indexers | Multiple data sources are typically paired with multiple indexers if you need to vary run time parameters, the schedule, or field mappings. </br></br>[Cross-region scale out of Azure AI Search](search-reliability.md#data-sync) is another scenario. You might have copies of the same search index in different regions. To synchronize search index content, you could have multiple indexers pulling from the same data source, where each indexer targets a different search index in each region.</br></br>[Parallel indexing](search-howto-large-index.md#parallel-indexing) of very large data sets also requires a multi-indexer strategy, where each indexer targets a subset of the data. |
+| Multiple data sources | An indexer specification can have only one data source, but the search index itself can accept content from multiple sources, where each indexer job brings new content from a different data provider. Each source can contribute its share of full documents, or populate selected fields in each document. For a closer look at this scenario, see [Tutorial: Index from multiple data sources](tutorial-multiple-data-sources.md). |
+| Multiple indexers | Multiple data sources are typically paired with multiple indexers if you need to vary run time parameters, the schedule, or field mappings. </br></br>[Cross-region scale out of Azure AI Search](search-reliability.md#data-sync) is a variation of this scenario. You might have copies of the same search index in different regions. To synchronize search index content, you could have multiple indexers pulling from the same data source, where each indexer targets a different search index in each region.</br></br>[Parallel indexing](search-howto-large-index.md#parallel-indexing) of very large data sets also requires a multi-indexer strategy, where each indexer targets a subset of the data. |
 | Content transformation | Indexers drive [skillset execution and AI enrichment](cognitive-search-concept-intro.md). Content transforms are defined in a [skillset](cognitive-search-working-with-skillsets.md) that you attach to the indexer. You can use skills to [incorporate data chunking and vectorization](vector-search-integrated-vectorization.md).|
 
  You should plan on creating one indexer for every target index and data source combination. You can have multiple indexers writing into the same index, and you can reuse the same data source for multiple indexers. However, an indexer can only consume one data source at a time, and can only write to a single index. As the following graphic illustrates, one data source provides input to one indexer, which then populates a single index:  
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサの概要に関する内容の更新"
}
```

### Explanation
このコードの差分は、Azure AI Searchにおけるインデクサの概要に関するドキュメントの内容を更新したものです。主な変更点として、最初に更新された日付が「2024年8月19日」から「2024年12月19日」に修正されています。また、インデクサによるAI教育とエンリッチメントの処理内容がより詳細に記述されています。具体的には、従来の「text-to-vector embeddings」の記載が、「vectors for vector search」の生成を呼び出す内容に変更され、情報が明確化されました。

さらに、インデクサが特定のデータソース用の設定プロパティを持つことが強調されており、その内容もわかりやすく整理されています。他にも、データの同期を必要とするプッシュモデルの記載が改善されており、インデクサの役割や指定の改善が行われています。全体の修正には6行の追加と6行の削除があり、合計で12行の変更が行われています。これにより、ユーザーがインデクサを利用する際の理解が深まることでしょう。

## articles/search/search-indexer-securing-resources.md{#item-c075c4}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: conceptual
-ms.date: 10/25/2024
+ms.date: 12/19/2024
 ---
 
 # Indexer access to content protected by Azure network security
@@ -68,18 +68,18 @@ Your Azure resources could be protected using any number of the network isolatio
 | SQL Managed Instance | Supported | N/A |
 | Azure Functions | Supported | Supported, only for certain tiers of Azure functions |
 
-## Indexer execution environment
+## Network access and indexer execution environments
 
-Azure AI Search has the concept of an *indexer execution environment* that optimizes processing based on the characteristics of the job. There are two environments. If you're using an IP firewall to control access to Azure resources, knowing about execution environments will help you set up an IP range that is inclusive of both environments.
+Azure AI Search has the concept of an [*indexer execution environment*](search-howto-run-reset-indexers.md#indexer-execution-environment) that optimizes processing based on the characteristics of the job. There are two environments. If you're using an IP firewall to control access to Azure resources, knowing about execution environments will help you set up an IP range that is inclusive of both environments.
 
 For any given indexer run, Azure AI Search determines the best environment in which to run the indexer. Depending on the number and types of tasks assigned, the indexer will run in one of two environments/
 
 | Execution environment | Description |
 |-----------------------|-------------|
-| Private | Internal to a search service. Indexers running in the private environment share computing resources with other indexing and query workloads on the same search service. If you set up a private connection between an indexer and your data, such as a shared private link, this is the only execution enriovnment you can use and it's used automatically. |
+| Private | Internal to a search service. Indexers running in the private environment share computing resources with other indexing and query workloads on the same search service. If you set up a private connection between an indexer and your data, such as a shared private link, this is the only execution environment you can use and it's used automatically. |
 |  multitenant | Managed and secured by Microsoft at no extra cost. It isn't subject to any network provisions under your control. This environment is used to offload computationally intensive processing, leaving service-specific resources available for routine operations. Examples of resource-intensive indexer jobs include skillsets, processing large documents, or processing a high volume of documents. |
 
-For Standard2 services and higher, you can configure an indexer to always use the private environment. For more information, see [Create an indexer](search-how-to-create-indexers.md?tabs=indexer-rest#create-an-indexer).
+For Standard2 services and higher, you can configure an indexer to always use the private environment. However, skillset processing always executes in the multitenant environment, even if you configure your search service to use the private environment. For more information about indexer configuration, see [Create an indexer](search-how-to-create-indexers.md?tabs=indexer-rest#create-an-indexer).
 
 ### Setting up IP ranges for indexer execution
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ネットワークアクセスとインデクサ実行環境の説明の更新"
}
```

### Explanation
このコードの差分は、Azure AI Searchにおけるインデクサのリソース保護に関するドキュメントの一部を更新したものです。主な変更点として、最初に更新された日付が「2024年10月25日」から「2024年12月19日」に修正されています。また、「インデクサ実行環境」というセクションのタイトルが「ネットワークアクセスとインデクサ実行環境」に変更され、より明確に内容が示されています。

インデクサの実行環境についての説明は整理されており、特にプライベート接続を使用する場合の環境の選択に関する内容が強化されています。具体的には、プライベート環境とマルチテナント環境の違いが明確に示されていて、ユーザーはどの環境でインデクサが実行されるかが一目で理解できるようになっています。

さらに、「プライベート環境」を選択できるサービスのバージョンについての記述が明確になり、条件がより詳しく示されています。全体として5行の追加と5行の削除を含むマイナーアップデートで、合計で10行の変更があり、文書の可読性と理解度が向上しています。

## articles/search/search-indexer-troubleshooting.md{#item-087365}

<details>
<summary>Diff</summary>
````diff
@@ -115,7 +115,7 @@ To update the policy and allow indexer access to the document library:
 
 1. Get the IP address ranges for the indexer execution environment for your region.
 
-    Extra IP addresses are used for requests that originate from the indexer's [multitenant execution environment](search-indexer-securing-resources.md#indexer-execution-environment). You can get this IP address range from the service tag.
+    Extra IP addresses are used for requests that originate from the indexer's [multitenant execution environment](search-indexer-securing-resources.md#network-access-and-indexer-execution-environments). You can get this IP address range from the service tag.
 
     The IP address ranges for the `AzureCognitiveSearch` service tag can be either obtained via the [discovery API](/azure/virtual-network/service-tags-overview#use-the-service-tag-discovery-api) or the [downloadable JSON file](/azure/virtual-network/service-tags-overview#discover-service-tags-by-using-downloadable-json-files).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチテナント実行環境に関するリンクの更新"
}
```

### Explanation
このコードの差分は、Azure AI Search におけるインデクサのトラブルシューティングに関するドキュメントを更新したものです。主な変更点は、マルチテナント実行環境に関するリンク先が変更されたことです。具体的には、「multitenant execution environment」に関するリンクが、以前の「search-indexer-securing-resources.md#indexer-execution-environment」から「search-indexer-securing-resources.md#network-access-and-indexer-execution-environments」に修正されました。

この変更により、関連するセクションにユーザーがより簡単にアクセスできるようになり、情報の可視性が向上します。また、追加と削除がそれぞれ1行ずつあり、合計で2行の変更が行われたことで、文書が最新の情報に基づいて整理されています。全体的に、ユーザーがインデクサのアクセスに必要な情報をより効率的に取得できるように配慮された変更です。

## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -133,7 +133,7 @@ Maximum running times exist to provide balance and stability to the service as a
 
 <sup>4</sup> Maximum of 30 skills per skillset.
 
-<sup>5</sup> Regarding the 2 or 24 hour maximum duration for indexers: a 2-hour maximum is the most common and it's what you should plan for. It refers to indexers that run in the [public environment](search-howto-run-reset-indexers.md#indexer-execution), used to offload computationally intensive processing and leave more resources for queries. The 24-hour limit applies if you configure the indexer to run in a private environment using only the infrastructure that's allocated to your search service. Note that some older indexers are incapable of running in the public environment, and those indexers always have a 24-hour processing range. If you have unscheduled indexers that run continuously for 24 hours, you can assume those indexers couldn't be migrated to the newer infrastructure. As a general rule, for indexing jobs that can't finish within two hours, put the indexer on a [5 minute schedule](search-howto-schedule-indexers.md) so that the indexer can quickly pick up where it left off. On the Free tier, the 3-10 minute maximum running time is for indexers with skillsets.
+<sup>5</sup> Regarding the 2 or 24 hour maximum duration for indexers: a 2-hour maximum is the most common and it's what you should plan for. It refers to indexers that run in the [public environment](search-howto-run-reset-indexers.md#indexer-execution-environment), used to offload computationally intensive processing and leave more resources for queries. The 24-hour limit applies if you configure the indexer to run in a private environment using only the infrastructure that's allocated to your search service. Note that some older indexers are incapable of running in the public environment, and those indexers always have a 24-hour processing range. If you have unscheduled indexers that run continuously for 24 hours, you can assume those indexers couldn't be migrated to the newer infrastructure. As a general rule, for indexing jobs that can't finish within two hours, put the indexer on a [5 minute schedule](search-howto-schedule-indexers.md) so that the indexer can quickly pick up where it left off. On the Free tier, the 3-10 minute maximum running time is for indexers with skillsets.
 
 <sup>6</sup> The maximum number of characters is based on Unicode code units, specifically UTF-16.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデクサの最大実行時間の説明の修正"
}
```

### Explanation
このコードの差分は、Azure AI Search における制限、クォータ、およびキャパシティに関するドキュメントの一部を更新したものです。主な変更は、インデクサの最大実行時間に関する注釈 `<sup>5</sup>` の内容が、微細な修正を受けたことです。

具体的には、「public environment」へのリンクが「search-howto-run-reset-indexers.md#indexer-execution」から「search-howto-run-reset-indexers.md#indexer-execution-environment」に変更されました。これにより、リンク先が最新の情報に適合するように修正され、ユーザーが必要な情報にアクセスしやすくなっています。

この変更は1行の追加と1行の削除を含んでおり、合計で2行の変更が行われています。全体として、情報の整合性や可読性が向上し、ユーザーの理解を助けるための重要な更新となります。


