---
date: '2024-12-13'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a7b86da...MicrosoftDocs:3d9c9bc
summary: 今回の変更は、Azure AI Searchのドキュメントの改善を目的としており、新しいセマンティックランキングコード移行に関するドキュメントの追加、正規表現検索の強化された説明、セキュリティおよび権限に関する説明の明確化が含まれています。また、一部のAPI更新に伴う互換性のない変更も指摘されています。これにより、ユーザーはAzure
  AI Searchをより効果的かつ安全に利用することができるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a7b86da...MicrosoftDocs:3d9c9bc){target="_blank"}

<format>
# Highlights
今回の変更は、Azure AI Searchのドキュメントの改善を目的としており、多くの項目で詳細が追加または修正されています。特に、新しいセマンティックランキングコード移行に関するドキュメントの追加、正規表現検索の強化された説明、そしてセキュリティおよび権限に関する説明の明確化が目立ちます。

## New features
- セマンティックランキングコード移行に関する新しいドキュメントが追加されました。

## Breaking changes
- ドキュメントの中には、APIの更新に伴う「breaking changes」（互換性のない変更）が指摘されている箇所があります。特に、`queryLanguage` プロパティの利用が今後無視されるようになった点です。

## Other updates
- 正規表現検索に関する詳細な説明の追加。
- セキュリティ設定におけるロール要件や権限の修正。
- ベクトル検索における`k`パラメータの推奨値変更。
- 様々な文書で、最新の情報に基づく内容の修正や日付の更新。

# Insights
この差分に示される一連の変更は、Azure AI Searchのユーザーにとって非常に重要な更新を含んでいます。まず、セマンティックランキングコード移行に関する新しいドキュメントの追加は、これからAzure AI Searchを効果的に利用するための重要なガイドラインを提供しています。このドキュメントは、開発者が最新のAPIバージョンに対応するための具体的な手段を示しており、プレビューAPIからの移行を円滑に行えるように支援します。

また、正規表現検索に関する説明が強化され、スラッシュで囲むことや全小文字での記述が必須であることなど、使用に関する詳細なガイドラインが明記されています。これにより、ユーザーは検索クエリの精度を高め、効率的に情報を取得できるようになるでしょう。

さらに、セキュリティ設定に関する修正では、データプレーンのフル管理アクセスやRBACの役割に関する説明がより正確になり、ユーザーが必要な権限を設定する際の指針を提供しています。このようなセキュリティや権限に関する変更は、ユーザーがより安全にAzure AI Searchを利用するために不可欠です。

ベクトル検索のクエリにおいては、`k` パラメータの推奨値が50に変更され、これがセマンティックランクモデルによって必要とされることが明示されました。この仕様は、検索結果の質を高めるための指針となり、ユーザーに的確な検索環境を提供するための一部となります。

全体的に、これらの更新はAzure AI Searchユーザーの技術的理解を深め、より効率的にサービスを利用させることを目的としています。このような文書の改善により、ユーザーはAzure AI Searchの持つ能力を最大限に活用できるようになり、同時に最新のアップデートにも迅速に対応できます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [hybrid-search-how-to-query.md](#item-345ce6) | minor update | ハイブリッド検索クエリの改善 | modified | 3 | 1 | 4 | 
| [keyless-connections.md](#item-3f0d72) | minor update | キーレス接続に関するロールの説明の修正 | modified | 1 | 2 | 3 | 
| [query-lucene-syntax.md](#item-736436) | minor update | 正規表現検索に関する詳細の追加 | modified | 8 | 3 | 11 | 
| [search-api-migration.md](#item-07297b) | minor update | セマンティックモデルのアップデートに関する説明の修正 | modified | 1 | 1 | 2 | 
| [search-get-started-rag.md](#item-05ff0e) | minor update | 検索インデックスに関する権限の説明の修正 | modified | 0 | 1 | 1 | 
| [search-get-started-rbac.md](#item-9d96c1) | minor update | RBACにおける役割の説明の修正 | modified | 2 | 2 | 4 | 
| [search-indexer-howto-access-private.md](#item-73d30d) | minor update | プライベートリンク接続に関する内容の更新 | modified | 2 | 2 | 4 | 
| [search-query-lucene-examples.md](#item-ce3624) | minor update | 正規表現検索の説明の強化 | modified | 1 | 1 | 2 | 
| [search-security-enable-roles.md](#item-4985c4) | minor update | データプレーンのロール要件の更新 | modified | 1 | 1 | 2 | 
| [search-security-rbac.md](#item-a5d129) | minor update | インデックスの読み取り/クエリ権限の修正 | modified | 1 | 1 | 2 | 
| [semantic-code-migration.md](#item-ad1ba7) | new feature | セマンティックランキングコードの移行に関する新しいドキュメント | added | 114 | 0 | 114 | 
| [semantic-how-to-configure.md](#item-7a92a6) | minor update | セマンティックランカー設定に関する記事の修正 | modified | 7 | 29 | 36 | 
| [semantic-how-to-enable-disable.md](#item-71ac1e) | minor update | セマンティックランカーの有効化・無効化に関する記事の修正 | modified | 2 | 2 | 4 | 
| [semantic-how-to-query-request.md](#item-85530d) | minor update | クエリにセマンティックランクを追加する方法に関する記事の修正 | modified | 2 | 2 | 4 | 
| [semantic-search-overview.md](#item-b7497b) | minor update | Azure AI Searchにおけるセマンティックランクの概要に関する記事の修正 | modified | 7 | 7 | 14 | 
| [service-configure-firewall.md](#item-75be3f) | minor update | ファイアウォール構成に関する記事の文言修正 | modified | 1 | 1 | 2 | 
| [toc.yml](#item-c4768f) | minor update | 検索に関する目次ファイルの更新 | modified | 6 | 6 | 12 | 
| [vector-search-how-to-query.md](#item-9bb93c) | minor update | ベクトル検索のクエリに関する文書の更新 | modified | 4 | 2 | 6 | 
| [whats-new.md](#item-fa71b4) | minor update | 新機能リストの更新 | modified | 7 | 1 | 8 | 


# Modified Contents
## articles/search/hybrid-search-how-to-query.md{#item-345ce6}

<details>
<summary>Diff</summary>
````diff
@@ -228,6 +228,8 @@ POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/d
 
 Assuming that you [enabled semantic ranker](semantic-how-to-enable-disable.md) and your index definition includes a [semantic configuration](semantic-how-to-query-request.md), you can formulate a query that includes vector search and keyword search, with semantic ranking over the merged result set. Optionally, you can add captions and answers. 
 
+Whenever you use semantic ranking with vectors, make sure `k` is set to 50. Semantic ranker uses up to 50 matches as input. Specifying less than 50 deprives the semantic ranking models of necessary inputs.
+
 ```http
 POST https://{{search-service-name}}.search.windows.net/indexes/{{index-name}}/docs/search?api-version=2024-07-01
 Content-Type: application/json
@@ -306,7 +308,7 @@ api-key: {{admin-api-key}}
 
 + Prefiltering is applied before query execution. If prefilter reduces the search area to 100 documents, the vector query executes over the "DescriptionVector" field for those 100 documents, returning the k=50 best matches. Those 50 matching documents then pass to RRF for merged results, and then to semantic ranker.
 
-+ Postfilter is applied after query execution. If k=50 returns 50 matches on the vector query side, then the post-filter is applied to the 50 matches, reducing results that meet filter criteria, leaving you with fewer than 50 documents to pass to semantic ranker.
++ Postfilter is applied after query execution. If k=50 returns 50 matches on the vector query side, followed by a post-filter applied to the 50 matches, your results are reduced by the number of documents that meet filter criteria. This leaves you with fewer than 50 documents to pass to semantic ranker. Keep this in mind if you're using semantic ranking. The semantic ranker works best if it has 50 documents as input.
 
 ## Set maxTextRecallSize and countAndFacetMode (preview)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ハイブリッド検索クエリの改善"
}
```

### Explanation
このコードの変更は、ハイブリッド検索に関する文書の一部を更新したもので、特にセマンティックランクの使用方法に関する説明が追加されています。具体的には、`k`の値が50に設定されるべき理由と、この数値がセマンティックランクモデルにとって重要であることを明確にしています。

変更内容には、以下のポイントが含まれています：
- セマンティックランクを用いる場合、`k`は50に設定する必要があり、これによりランクモデルが必要な入力を確保できることを説明しています。
- プレフィルタリングとポストフィルタリングのプロセスについての詳細な記述が強化されています。特に、ポストフィルタリングがどのように適用されるか、またその結果がセマンティックランクにどのように影響を与えるかが説明されています。

この変更により、ユーザーはセマンティックランクを最適に利用するための具体的なガイダンスを得ることができ、検索クエリの精度が向上することを期待できます。

## articles/search/keyless-connections.md{#item-3f0d72}

<details>
<summary>Diff</summary>
````diff
@@ -223,8 +223,7 @@ Local development using roles includes these steps:
 As a local developer, your Azure identity needs full control over data plane operations. These are the suggested roles:
 
 - Search Service Contributor, create and manage objects
-- Search Index Data Contributor, load an index
-- Search Index Data Reader, query an index
+- Search Index Data Contributor, load and query an index
 
 Find your personal identity with one of the following tools. Use that identity as the `<identity-id>` value.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "キーレス接続に関するロールの説明の修正"
}
```

### Explanation
このコードの変更は、キーレス接続に関する文書内の役割の説明を簡略化したものです。具体的には、Azureのローカル開発に関連するロールに関する記述が変更されています。

主な変更点は次の通りです：
- "Search Index Data Contributor"の役割に関する説明が修正され、「インデックスの読み込み」と「クエリの実行」が1つの項目に統合されました。これにより、役割の役割がより明確になり、重複していた情報が削除されています。

この変更により、ユーザーはAzureでのローカル開発において必要なロールの情報をより分かりやすく理解できるようになります。

## articles/search/query-lucene-syntax.md{#item-736436}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 09/19/2024
+ms.date: 12/11/2024
 ---
 
 # Lucene query syntax in Azure AI Search
@@ -136,9 +136,14 @@ The following example helps illustrate the differences. Suppose that there's a s
 
 ##  <a name="bkmk_regex"></a> Regular expression search
  
- A regular expression search finds a match based on patterns that are valid under Apache Lucene, as documented in the [RegExp class](https://lucene.apache.org/core/6_6_1/core/org/apache/lucene/util/automaton/RegExp.html). In Azure AI Search, a regular expression is enclosed between forward slashes `/`.
+A regular expression search finds a match based on patterns that are valid under Apache Lucene, as documented in the [RegExp class](https://lucene.apache.org/core/6_6_1/core/org/apache/lucene/util/automaton/RegExp.html). 
 
- For example, to find documents containing `motel` or `hotel`, specify `/[mh]otel/`. Regular expression searches are matched against single words.
+In Azure AI Search, a regular expression is:
+
+* Enclosed between forward slashes `/`
+* Lower-case only
+
+For example, to find documents containing `motel` or `hotel`, specify `/[mh]otel/`. Regular expression searches are matched against single words.
 
 Some tools and languages impose extra escape character requirements beyond the [escape rules](#escaping-special-characters) imposed by Azure AI Search. For JSON, strings that include a forward slash are escaped with a backward slash: `microsoft.com/azure/` becomes `search=/.*microsoft.com\/azure\/.*/` where `search=/.* <string-placeholder>.*/` sets up the regular expression, and `microsoft.com\/azure\/` is the string with an escaped forward slash. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "正規表現検索に関する詳細の追加"
}
```

### Explanation
このコードの変更は、Azure AI Searchにおける正規表現検索の説明を強化したものです。主に正規表現の使用に関する明確なガイドラインが追加されています。

主な変更点は以下の通りです：
- 正規表現がAzure AI Searchで使用される際のルールが詳細に説明されるようになりました。具体的には、正規表現はスラッシュ `/` で囲まれていること、全て小文字である必要があることが明記されています。
- 例として、`motel` または `hotel` を含む文書を検索する場合の正規表現例 `/[mh]otel/` がそのまま示されています。
- 正規表現検索が単語単位での一致を確認することも強調されています。

この変更により、ユーザーはAzure AI Searchにおける正規表現の使用方法について、より正確に理解し、実装できるようになりました。

## articles/search/search-api-migration.md{#item-07297b}

<details>
<summary>Diff</summary>
````diff
@@ -72,7 +72,7 @@ Effective March 29, 2024 and applicable to all [supported REST APIs](/rest/api/s
 
 + For all API versions, updates on July 14, 2023 to the Microsoft-hosted semantic models made semantic ranker language-agnostic, effectively decommissioning the `queryLanguage` property. There's no "breaking change" in code, but the property is ignored.
 
-See [Migrate from preview version](semantic-how-to-configure.md#migrate-from-preview-versions) to transition your code to use `semanticConfiguration`.
+See [Migrate from preview version](semantic-code-migration.md) to transition your code to use `semanticConfiguration`.
 
 ## Upgrade to 2024-11-01-preview
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックモデルのアップデートに関する説明の修正"
}
```

### Explanation
このコードの変更は、Azureの検索APIマイグレーションに関する文書において、セマンティックモデルの最新の更新に関する情報を修正したものです。具体的には、`queryLanguage` プロパティに関する重要な情報が統合され、関連する参照も更新されています。

主な変更点は次の通りです：
- セマンティックモデルについての説明が追加され、2023年7月14日の更新によって、`queryLanguage` プロパティが効果的に廃止されたことが明記されています。これにより、このプロパティは今後無視されることになります。
- マイグレーションに関するリンクが更新され、`semantic-how-to-configure.md` から `semantic-code-migration.md` に修正されました。この修正により、ユーザーはより正確な情報源にアクセスできるようになります。

これらの修正は、APIを使用している開発者にとって、セマンティック構成への移行をスムーズにするための重要なガイダンスを提供します。

## articles/search/search-get-started-rag.md{#item-05ff0e}

<details>
<summary>Diff</summary>
````diff
@@ -63,7 +63,6 @@ Azure OpenAI is receiving the (query) "Can you recommend a few hotels" from your
 
     1. On Azure AI Search, make sure you have permissions to create, load, and query a search index:
 
-       - **Search Index Data Reader**
        - **Search Index Data Contributor**
        - **Search Service Contributor**
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索インデックスに関する権限の説明の修正"
}
```

### Explanation
このコードの変更は、Azure AI Searchにおける検索インデックスの権限に関する説明を修正したものです。具体的には、必要な権限リストから1つの項目が削除されました。

主な変更点は以下の通りです：
- **Search Index Data Reader** の権限がリストから削除されました。これにより、検索インデックスを作成、読み込み、クエリするために必要な権限が更新されました。
- 残る権限として、**Search Index Data Contributor** と **Search Service Contributor** が引き続き必要であることが示されています。

この修正は、ユーザーに対して正確な権限情報を提供し、検索インデックスを操作するために必要なアクセス権の理解を助ける目的があります。

## articles/search/search-get-started-rbac.md{#item-9d96c1}

<details>
<summary>Diff</summary>
````diff
@@ -72,11 +72,11 @@ You need this step if you have more than one subscription or tenant.
 
    1. Select **+ Add** > **Add role assignment**.
 
-   1. Choose a role (Search Service Contributor, Search Index Data Contributor, Search Index Data Reader) and assign it to your Microsoft Entra user or group identity.
+   1. Choose a role (**Search Service Contributor**, **Search Index Data Contributor**, **Search Index Data Reader**) and assign it to your Microsoft Entra user or group identity.
 
       Repeat for each role.
 
-      You need all three roles for creating, loading, and querying objects on Azure AI Search. For more information, see [Connect using roles](search-security-rbac.md).
+      You need **Search Service Contributor** plus **Search Index Data Contributor** to create, load, and query objects on Azure AI Search. For more information, see [Connect using roles](search-security-rbac.md).
 
 > [!TIP]
 > Later, if you get authentication failure errors, recheck the settings in this section. There could be policies at the subscription or resource group level that override any API settings you specify.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RBACにおける役割の説明の修正"
}
```

### Explanation
このコードの変更は、Azure AI SearchのRBAC（ロールベースのアクセス制御）に関する文書の修正を示しています。具体的には、要求される役割に関する説明が明確に整理され、情報の正確性が向上しました。

主な変更点は下記の通りです：
- 役割の選択時に、役割名が太字で強調されるよう修正されました。具体的には、**Search Service Contributor**, **Search Index Data Contributor**, **Search Index Data Reader**が強調されています。
- すべての役割が必要であるという説明が変更され、**Search Service Contributor** と **Search Index Data Contributor** の2つの役割だけが、オブジェクトの作成、読み込み、およびクエリを行うために必要であることが明記されました。**Search Index Data Reader** の役割は必要ないことが示されています。

これにより、ユーザーは役割の選択とその要件についてより明確に理解できるようになります。全体として、この修正はRBACの設定を簡単にし、使用する役割に関する混乱を避けることを目的としています。

## articles/search/search-indexer-howto-access-private.md{#item-73d30d}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 11/19/2024
+ms.date: 12/10/2024
 ---
 
 # Make outbound connections through a shared private link
@@ -126,7 +126,7 @@ You can create a shared private link for the following resources.
 
 <sup>7</sup> Shared private link for Azure OpenAI is only supported in public cloud. Other cloud offerings such as [Microsoft Azure Government](https://azure.microsoft.com/explore/global-infrastructure/government/) don't have support for shared private links for `openai_account` Group ID.
 
-<sup>8</sup> Shared private links are now supported (as of November 2024) for connections to Azure AI multiservice accounts. Azure AI Search connects to Azure AI multiservice for [billing purposes](cognitive-search-attach-cognitive-services.md). These connections can now be private through a shared private link. 
+<sup>8</sup> Shared private links are now supported (as of November 2024) for connections to Azure AI multiservice accounts. Azure AI Search connects to Azure AI multiservice for [billing purposes](cognitive-search-attach-cognitive-services.md). These connections can now be private through a shared private link. Shared private link is only supported when configuring [a managed identity (keyless configuration)](cognitive-search-attach-cognitive-services.md#bill-through-a-keyless-connection) in the skillset definition. 
 
 ## 1 - Create a shared private link
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベートリンク接続に関する内容の更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchに関するドキュメントの更新であり、プライベートリンクを通じた接続に関する情報が追加されています。特に、プライベートリンクを設定する際の要件が明確化されました。

主な変更点は以下の通りです：
- `ms.date`フィールドが2024年11月19日から2024年12月10日へ更新され、文書の最終更新日が修正されました。
- プライベートリンクのサポートに関する補足情報が追加されました。具体的には、共有プライベートリンクが**マネージドアイデンティティ**（キーレス構成）を設定する際にのみサポートされることが明記されました。

この変更により、ユーザーはAzure AI Searchを利用してプライベートリンクを構成する際の具体的な条件を理解できるようになり、設定手順がより明確になります。全体として、この更新はユーザーの理解を助け、Azure AI Searchと他のAzureサービスとの接続をより一層优化することを目的としています。

## articles/search/search-query-lucene-examples.md{#item-ce3624}

<details>
<summary>Diff</summary>
````diff
@@ -391,7 +391,7 @@ After you boost the term *beach*, the match on Campus Commander Hotel moves down
 
 ## Example 5: Regex
 
-A regular expression search finds a match based on the contents between forward slashes `/`, as documented in the [RegExp class](https://lucene.apache.org/core/6_6_1/core/org/apache/lucene/util/automaton/RegExp.html).
+A regular expression search finds a match based on the contents between forward slashes `/` and lower-case strings, as documented in the [RegExp class](https://lucene.apache.org/core/6_6_1/core/org/apache/lucene/util/automaton/RegExp.html).
 
 ```http
 POST /indexes/hotel-samples-index/docs/search?api-version=2024-07-01
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "正規表現検索の説明の強化"
}
```

### Explanation
このコードの変更は、Azure SearchにおけるLuceneの正規表現検索に関する文書の修正を示しています。具体的には、正規表現検索がどのように機能するかの説明が強化されています。

主な変更点は次の通りです：
- 正規表現検索の説明が変更され、**小文字の文字列**に対するマッチも含まれることが明記されました。具体的には、「/」で囲まれた内容だけでなく、小文字の文字列に基づいてもマッチが生成されると説明されています。

この修正により、ユーザーは正規表現検索の動作についてより明確に理解できるようになり、特に小文字に関する要件が強調されたことによって、より効果的な検索クエリの構築が可能になります。全体として、この更新は文書の情報の正確性と役立ち度を向上させることを目的としています。

## articles/search/search-security-enable-roles.md{#item-4985c4}

<details>
<summary>Diff</summary>
````diff
@@ -51,7 +51,7 @@ The default failure mode for unauthorized requests is `http401WithBearerChalleng
    | Role-based access control | Requires membership in a role assignment to complete the task. It also requires an authorization header on the request. |
    | Both | Requests are valid using either an API key or role-based access control, but if you provide both in the same request, the API key is used. |
 
-1. As an administrator, if you choose a roles-only approach, [assign data plane roles](search-security-rbac.md) to your user account to restore full administrative access over data plane operations in the Azure portal. Roles include Search Service Contributor, Search Index Data Contributor, and Search Index Data Reader. You need all three roles if you want equivalent access.
+1. As an administrator, if you choose a roles-only approach, [assign data plane roles](search-security-rbac.md) to your user account to restore full administrative access over data plane operations in the Azure portal. Roles include Search Service Contributor, Search Index Data Contributor, and Search Index Data Reader. You need the first two roles if you want equivalent access.
 
    Sometimes it can take five to ten minutes for role assignments to take effect. Until that happens, the following message appears in the Azure portal pages used for data plane operations.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データプレーンのロール要件の更新"
}
```

### Explanation
このコードの変更は、Azureのデータプレーンに関するセキュリティ設定のドキュメント内で、ロール要件に関する説明が修正されたことを示しています。特に、管理者がロールベースのアクセス制御を選択した場合に必要なロールについて明確化されています。

主な変更点は以下の通りです：
- データプレーンのフル管理アクセスを復元するために必要なロールのリストが変更されました。「Search Service Contributor」と「Search Index Data Contributor」の2つのロールが必要であると明記されており、以前は「すべての3つのロールが必要」と記述されていた部分が修正されています。

この修正により、ユーザーは必要なロールをより明確に理解できるようになり、Azureポータルでのデータプレーン操作に対する適切な権限設定が行いやすくなります。全体として、この更新は文書の正確性を向上させ、役立つ情報を提供することを目指しています。

## articles/search/search-security-rbac.md{#item-a5d129}

<details>
<summary>Diff</summary>
````diff
@@ -87,7 +87,7 @@ Combine these roles to get sufficient permissions for your use case.
 |View resource properties/metrics/endpoint |❌|❌|✅|✅|✅|
 |List all objects on the resource |❌|❌|✅|✅|✅|
 |Access quotas and service statistics |❌|❌|✅|✅|❌|
-|Read/query an index |✅|❌|❌|❌|❌|
+|Read/query an index |✅|✅|❌|❌|❌|
 |Upload data for indexing |❌|✅|❌|❌|❌|
 |Create or edit indexes/aliases |❌|❌|✅|✅|❌|
 |Create, edit and run indexers/data sources/skillsets |❌|❌|✅|✅|❌|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスの読み取り/クエリ権限の修正"
}
```

### Explanation
このコードの変更は、Azure Searchのロールベースアクセス制御（RBAC）に関するドキュメント内で、特定のロールにおけるインデックスの読み取りおよびクエリの権限が修正されたことを示しています。

具体的な変更点は以下の通りです：
- 表の中で、"Read/query an index"（インデックスの読み取り/クエリ）の行に対する権限が更新されました。以前は、特定のロールに対して「❌」と記載されていたのが、現在は「✅」の状態に変更されています。具体的には、**

  - **"[User](#)" ロールはインデックスの読み取りおよびクエリが可能になり、これを示すために表の内容が更新されました**。  
 
この修正により、ユーザーは特定のロールを持つことでインデックスにアクセスできることが明確になり、Azure Searchを利用する際に必要な権限を理解しやすくなります。全体として、この更新は文書の正確性を高め、適切な権限管理についての理解を促進するものです。

## articles/search/semantic-code-migration.md{#item-ad1ba7}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,114 @@
+---
+title: Migrate semantic ranking code 
+titleSuffix: Azure AI Search
+description: Migrate semantic ranking code from preview to stable versions, and now to newer preview versions.
+manager: nitinme
+author: HeidiSteen
+ms.author: heidist
+ms.service: azure-ai-search
+ms.custom:
+  - ignite-2023
+ms.topic: how-to
+ms.date: 12/10/2024
+---
+
+# Migrate semantic ranking code from previous versions
+
+If your semantic ranking code was written against early preview APIs, this article identifies the code changes necessary for migrating to newer API versions. Breaking changes for semantic ranker are limited to query logic in recent APIs, but if your code was written against the initial preview version, you might need to change your semantic configuration as well.
+
+## Breaking changes
+
+There are two breaking changes for semantic ranker across REST API versions:
+
++ `searchFields` was replaced by `semanticConfiguration` in 2021-04-30-preview
++ `queryLanguage` was ignored starting in 2023-07-01-preview, but reinstated for query rewrite in 2024-11-01-preview
+
+Other version-specific updates pertain to new capabilities, but don't break existing code and are therefore not breaking changes.
+
+If you're using Azure SDKs, multiple APIs have been renamed over time. The SDK change logs provide the details.
+
+## API versions providing semantic ranking
+
+Check your code for the REST API version or SDK package version to confirm which one provides semantic ranking. The following API versions have some level of support for semantic ranking.
+
+| Release&nbsp;type | REST&nbsp;API&nbsp;version | Semantic ranker updates |
+|--|--|--|
+| initial | [2020-06-30-preview](/rest/api/searchservice/preview-api/search-documents) | Adds `queryType=semantic` to Search Documents |
+| preview | [2021-04-30-preview](/rest/api/searchservice/preview-api/search-documents)  | Adds `semanticConfiguration` to Create or Update Index |
+| preview | [2023-07-01-preview](/rest/api/searchservice/preview-api/search-documents) | Updates `semanticConfiguration`. Starting on July 14, 2023 updates to the Microsoft-hosted semantic models made semantic ranker language-agnostic, effectively decommissioning the `queryLanguage` property for semantic ranking. There's no breaking change in code, but the property is ignored. Customers were advised to remove this property from code.|
+| preview | [2023-10-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2023-10-01-preview&preserve-view=true) | Adds `semanticQuery` to send a query used only for reranking purposes. |
+| stable | [2023-11-01](/rest/api/searchservice/operation-groups?view=rest-searchservice-2023-11-01&preserve-view=true) | Generally available. Introduced changes to `semanticConfiguration` that progressed to the stable version. If your code targets this version or later, it's compatible with newer API versions unless you adopt new preview features.|
+| preview | [2024-05-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-05-01-preview&preserve-view=true) | No change |
+| stable | [2024-07-01](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-07-01&preserve-view=true) | No change |
+| preview | [2024-09-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-09-01-preview&preserve-view=true) | No change |
+| preview | [2024-11-01-preview](/rest/api/searchservice/operation-groups?view=rest-searchservice-2024-11-01-preview&preserve-view=true) | Adds query rewrite. The `queryLanguage` property is now required if you use [query rewrite (preview)](semantic-how-to-query-rewrite.md).  |
+
+## Change logs for Azure SDKs
+
+Azure SDKs are on an independent release schedule. You should check the change logs to determine which packages provide semantic features and whether any APIs have been renamed.
+
++ [Azure SDK for .NET change log](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Search.Documents_11.5.1/sdk/search/Azure.Search.Documents/CHANGELOG.md#1150-2023-11-10&preserve-view=true)
++ [Azure SDK for Python change log](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md#1140-2023-10-13&preserve-view=true)
++ [Azure SDK for Java change log](https://github.com/Azure/azure-sdk-for-java/blob/azure-search-documents_11.6.1/sdk/search/azure-search-documents/CHANGELOG.md#1160-2023-11-13&preserve-view=true)
++ [Azure SDK for JavaScript change log](https://github.com/Azure/azure-sdk-for-js/blob/%40azure/search-documents_12.0.0/sdk/search/search-documents/CHANGELOG.md#1200-2023-11-13&preserve-view=true)
+
+## 2024-11-01-preview
+
++ Adds [query rewrite](semantic-how-to-query-rewrite.md) to Search Documents.
++ Requires `queryLanguage` for query rewrite workloads. For a list of valid values, see the [REST API](/rest/api/searchservice/documents/search-post?view=rest-searchservice-2024-11-01-preview#querylanguage&preserve-view=true).
+
+## 2024-09-01-preview
+
+No changes to semantic ranking syntax from the 2024-07-01 stable version.
+
+## 2024-07-01
+
+No changes to semantic ranking syntax from the 2024-05-01-preview version.
+
+Don't use this API version. It implements a vector query syntax that's incompatible with any newer API version.
+
+## 2024-05-01-preview
+
+No changes to semantic ranking syntax from the 2024-03-01-preview version.
+
+## 2024-03-01-preview
+
+No changes to semantic ranking syntax from the 2023-10-01-preview version, but vector queries are introduced. Semantic ranking now applies to responses from hybrid and vector queries. You can apply reranking on any human-readable text fields in the response, assuming the fields are listed in `prioritizedFields`.
+
+## 2023-11-01
+
++ Excludes `SemanticDebug` and `semanticQuery`, otherwise the same as the 2023-10-01-preview version.
+
+## 2023-10-01-preview
+
++ Adds `semanticQuery`
+
+## 2023-07-01-preview
+
++ Adds `semanticErrorHandling`, `semanticMaxWaitInMilliseconds`.
++ Adds numerous semantic-related fields to the response, such as `SemanticDebug` and `SemanticErrorMode`.
++ Ignores `queryLanguage`, it's no longer used in semantic ranking.
+
+Starting on July 14, 2023, semantic ranker is language agnostic. In preview versions, semantic ranking would deprioritize results differing from the `querylanguage` specified by the field analyzer. However, the `queryLanguage` property is still applicable to [spell correction](speller-how-to-add.md) and the short list of languages supported by that feature.
+
+## 2021-04-30-preview
+
++ Semantic support is through [Search Documents](/rest/api/searchservice/preview-api/search-documents) and [Create or Update Index](/rest/api/searchservice/preview-api/create-or-update-index) preview API calls.
++ Adds `semanticConfiguration` to a search index. A semantic configuration has a name and a prioritized field list.
++ Adds ``prioritizedFields`.
+
+The `searchFields` property is no longer used to prioritize fields. In all versions moving forward, `semanticConfiguration.prioritizedFields` replaces `searchFields` as the mechanism for specifying which fields to use for L2 ranking.
+
+## 2020-06-30-preview
+
++ Semantic support is through a [Search Documents](/rest/api/searchservice/preview-api/search-documents) preview API call.
++ Adds `queryType=semantic` to the query request.
++ Adapts `searchFields` so that if the query type is semantic, the `searchFields` property determines the priority order of field inputs to the semantic ranker.
++ Adds `captions`, `answers`, and `highlights` to the query response.
+
+## Next steps
+
+Test your semantic configuration migration by running a semantic query.
+
+> [!div class="nextstepaction"]
+> [Create a semantic query](semantic-how-to-query-request.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "セマンティックランキングコードの移行に関する新しいドキュメント"
}
```

### Explanation
このコードの変更は、「セマンティックランキングコードの移行」に関する新しいドキュメントが追加されたことを示しています。このドキュメントは、Azure AI Searchのセマンティックランキング機能を使用する際に、プレビューから安定版、さらに新しいプレビュー版へのコード移行に必要な変更を詳述しています。

主な内容は以下の通りです：
- 以前のプレビューAPIを使用してセマンティックランキングコードを書いた開発者に向け、必要なコード変更を解説しています。
- セマンティックランカーに対する「breaking changes」（互換性のない変更）として、「searchFields」が「semanticConfiguration」に置き換えられたことや、「queryLanguage」が2023年から無視されるようになったことについて説明しています。
- 最新のAPIバージョンがセマンティックランキングにどのように対応しているかを示す表があり、過去のバージョンや新しいバージョンにおける機能の変更点が詳述されています。
- Azure SDKのリリーススケジュールに関する情報や、各SDKの変更ログへのリンクも提供されており、どのパッケージがセマンティック機能を提供しているかを確認する手助けとなります。
- 最後に、移行テストを行うためのセマンティッククエリを作成する手順も示されています。

このドキュメントの追加により、開発者は最新のAPIバージョンへの移行を円滑に行うことができ、Azure Searchのセマンティック機能を効果的に活用するための情報を得られるようになります。

## articles/search/semantic-how-to-configure.md{#item-7a92a6}

<details>
<summary>Diff</summary>
````diff
@@ -9,14 +9,17 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 10/20/2024
+ms.date: 12/10/2024
 ---
 
 # Configure semantic ranker and return captions in search results
 
 Semantic ranking iterates over an initial result set, applying an L2 ranking methodology that promotes the most semantically relevant results to the top of the stack. You can also get semantic captions, with highlights over the most relevant terms and phrases, and [semantic answers](semantic-answers.md).
 
-This article explains how to configure a search index for semantic reranking. 
+This article explains how to configure a search index for semantic reranking.
+
+> [!NOTE]
+> If you have existing code that calls preview or previous API versions, see [Migrate semantic ranking code](semantic-code-migration.md) for help with modifying your code.
 
 ## Prerequisites
 
@@ -28,10 +31,10 @@ This article explains how to configure a search index for semantic reranking.
 
 ## Choose a client
 
-You can use any of the following tools and software development kits (SDKs) to add a semantic configuration:
+You can specify a semantic configuration on new or existing indexes, using any of the following tools and software development kits (SDKs) to add a semantic configuration:
 
 + [Azure portal](https://portal.azure.com), using the index designer to add a semantic configuration.
-+ [Visual Studio Code](https://code.visualstudio.com/download) with the [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)
++ [Visual Studio Code](https://code.visualstudio.com/download) with the [REST client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) and a [Create or Update Index (REST) API](/rest/api/searchservice/indexes/create-or-update).
 + [Azure SDK for .NET](https://www.nuget.org/packages/Azure.Search.Documents)
 + [Azure SDK for Python](https://pypi.org/project/azure-search-documents)
 + [Azure SDK for Java](https://central.sonatype.com/artifact/com.azure/azure-search-documents)
@@ -155,31 +158,6 @@ SearchIndex searchIndex = new(indexName)
 
 ---
 
-## Migrate from preview versions
-
-If your semantic ranking code is using preview APIs, this section explains how to migrate to stable versions. You can check the change logs for verification of general availability:
-
-+ [2024-07-01 (REST)](/rest/api/searchservice/indexes/create-or-update?view=rest-searchservice-2024-07-01&preserve-view=true)
-+ [Azure SDK for .NET (11.5) change log](https://github.com/Azure/azure-sdk-for-net/blob/Azure.Search.Documents_11.5.1/sdk/search/Azure.Search.Documents/CHANGELOG.md#1150-2023-11-10)
-+ [Azure SDK for Python (11.4) change log](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/CHANGELOG.md#1140-2023-10-13)
-+ [Azure SDK for Java (11.6) change log](https://github.com/Azure/azure-sdk-for-java/blob/azure-search-documents_11.6.1/sdk/search/azure-search-documents/CHANGELOG.md#1160-2023-11-13)
-+ [Azure SDK for JavaScript (12.0) change log](https://github.com/Azure/azure-sdk-for-js/blob/%40azure/search-documents_12.0.0/sdk/search/search-documents/CHANGELOG.md#1200-2023-11-13)
-
-
-### queryLanguage for semantic ranker
-
-As of July 14, 2023, semantic ranker is language agnostic. It can rerank results composed of multilingual content, with no bias towards a specific language. In preview versions, semantic ranking would deprioritize results differing from the language specified by the field analyzer.
-
-Stop using `queryLanguage` in your code if you were using it for semantic ranking. The `queryLanguage` property is still applicable to features such as [spell correction](speller-how-to-add.md), but not to semantic ranking.
-
-### searchFields for semantic ranker
-
-For the REST API and all SDK packages targeting version `2021-04-30-Preview` and later, the `searchFields` property is no longer used for semantic ranking.
-
-Instead, use the `semanticConfiguration` property (in a search index) to determine which search fields are used in semantic ranking. To specify field prioritization, add a `semanticConfiguration` to in an index schema following the [instructions in this article](#add-a-semantic-configuration).
-
-You can keep `searchFields` in query requests if you're using it to limit full text search to the list of named fields. 
-
 ## Next steps
 
 Test your semantic configuration by running a semantic query.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランカー設定に関する記事の修正"
}
```

### Explanation
このコードの変更は、「セマンティックランカー設定」に関するドキュメントが修正されたことを示しています。このアップデートには、具体的な内容の追加や不要な内容の削除が含まれています。

主な変更点は以下の通りです：
- 文書の最初に、既存のコードがプレビューまたは以前のAPIバージョンを使用している場合は、コード移行に関する別の記事（[Migrate semantic ranking code](semantic-code-migration.md)）を参照するように促す注釈が追加されました。
- セマンティック設定を追加するための利用可能なツールやSDKに関する説明が増補され、新規または既存のインデックスに対してセマンティック設定を指定できるという文が加わりました。
- 一部の内容が削除され、特にプレビュー版からの移行に関するセクションおよび「queryLanguage」や「searchFields」に関連する古い情報が取り除かれました。

これらの変更によって、ドキュメントの内容はより簡潔になり、最新のAPIバージョンに準拠した情報が提供され、開発者がセマンティックランカーを正しく設定できるようサポートしています。

## articles/search/semantic-how-to-enable-disable.md{#item-71ac1e}

<details>
<summary>Diff</summary>
````diff
@@ -10,12 +10,12 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: how-to
-ms.date: 10/28/2024
+ms.date: 12/10/2024
 ---
 
 # Enable or disable semantic ranker
 
-Semantic ranker is a premium feature billed by usage. By default, semantic ranker is turned off when you create a new search service, but anyone with *Contributor* permissions can enable it. If you don't want anyone enabling it inadvertently, you can [disable it using the REST API](#disable-semantic-ranker-using-the-rest-api).
+Semantic ranker is a premium feature billed by usage. By default, semantic ranker is turned off when you create a new search service, but anyone with *Contributor* permissions can enable it. If you don't want anyone enabling it inadvertently, you can [disable it service-wide using the management REST API](#disable-semantic-ranker-using-the-rest-api).
 
 ## Check availability
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セマンティックランカーの有効化・無効化に関する記事の修正"
}
```

### Explanation
このコードの変更は、「セマンティックランカーの有効化・無効化」に関する記事が修正されたことを示しています。主に文書内容の一部が変更され、情報がより明確になっています。

主な変更点は以下の通りです：
- 記事の日付が「2024年10月28日」から「2024年12月10日」に更新されました。
- セマンティックランカーの無効化に関する説明が変更され、単に「無効化する」と言う代わりに「サービス全体で無効化する」と明記されています。これにより、無効化の範囲が明確に示されています。

このような微調整により、読者はセマンティックランカーの利用や管理に関する理解を深めることができ、より正確な情報を基に判断することができるようになります。

## articles/search/semantic-how-to-query-request.md{#item-85530d}

<details>
<summary>Diff</summary>
````diff
@@ -11,14 +11,14 @@ ms.custom:
   - ignite-2023
   - ignite-2024
 ms.topic: how-to
-ms.date: 11/19/2024
+ms.date: 12/10/2024
 ---
 
 # Add semantic ranking to queries in Azure AI Search
 
 You can apply semantic ranking to text queries, hybrid queries, and vector queries if your search documents contain string fields and the [vector query has a text representation](vector-search-how-to-query.md#query-with-integrated-vectorization) in the search document.
 
-This article explains how to invoke the semantic ranker on queries. 
+This article explains how to invoke the semantic ranker on queries. It assumes you're using the most recent stable or preview APIs. For help with older versions, see [Migrate semantic ranking code](semantic-code-migration.md).
 
 ## Prerequisites
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クエリにセマンティックランクを追加する方法に関する記事の修正"
}
```

### Explanation
このコードの変更は、「Azure AI Searchにおけるクエリへのセマンティックランクの追加方法」に関する記事が修正されたことを示しています。この更新により、文書の内容がより明確で役立つものになっています。

主な変更点は以下の通りです：
- 記事の日付が「2024年11月19日」から「2024年12月10日」に更新されました。
- セマンティックランカーをクエリに適用する方法の説明に、最新の安定版またはプレビュー版APIを使用していることを前提とする旨が追加されました。また、古いバージョンのAPIを使用している場合には、コードの移行に関する別の記事（[Migrate semantic ranking code](semantic-code-migration.md)）を参照するように促す文が加えられています。

これらの変更によって、読者は最新の情報を得ることができ、古いバージョンのAPIからの移行方法についても理解を深めることが可能となります。

## articles/search/semantic-search-overview.md{#item-b7497b}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 09/24/2024
+ms.date: 12/10/2024
 ---
 
 # Semantic ranking in Azure AI Search
@@ -20,13 +20,13 @@ In Azure AI Search, *semantic ranker* is a feature that measurably improves sear
 Semantic ranker is a premium feature, billed by usage. We recommend this article for background, but if you'd rather get started, [follow these steps](#how-to-get-started-with-semantic-ranker).
 
 > [!NOTE]
-> Semantic ranker doesn't use generative AI or vectors. If you're looking for vector support and similarity search, see [Vector search in Azure AI Search](vector-search-overview.md) for details.
+> Semantic ranker doesn't use generative AI or vectors. If you're looking for vectors and similarity search, see [Vector search in Azure AI Search](vector-search-overview.md) for details.
 
 ## What is semantic ranking?
 
-Semantic ranker is a collection of query-side capabilities that improve the quality of an initial [BM25-ranked](index-similarity-and-scoring.md) or [RRF-ranked](hybrid-search-ranking.md) search result for text-based queries, vector queries, and hybrid queries. When you enable it on your search service, semantic ranking extends the query execution pipeline in two ways: 
+Semantic ranker is a collection of query-side capabilities that improve the quality of an initial [BM25-ranked](index-similarity-and-scoring.md) or [RRF-ranked](hybrid-search-ranking.md) search result for text-based queries, vector queries, and hybrid queries. When you enable it on your search service, semantic ranking extends the query execution pipeline in two ways:
 
-* First, it adds secondary ranking over an initial result set that was scored using BM25 or Reciprocal Rank Fusion (RRF). This secondary ranking uses multi-lingual, deep learning models adapted from Microsoft Bing to promote the most semantically relevant results. 
+* First, it adds secondary ranking over an initial result set that was scored using BM25 or Reciprocal Rank Fusion (RRF). This secondary ranking uses multi-lingual, deep learning models adapted from Microsoft Bing to promote the most semantically relevant results.
 
 * Second, it extracts and returns captions and answers in the response, which you can render on a search page to improve the user's search experience.
 
@@ -72,11 +72,11 @@ In semantic ranking, the query subsystem passes search results as an input to su
 
 1. Summarization output is a summary string for each document, composed of the most relevant information from each field. Summary strings are sent to the ranker for scoring, and to machine reading comprehension models for captions and answers.
 
-   The maximum length of each generated summary string passed to the semantic ranker is 256 tokens. 
+   As of November 2024, the maximum length of each generated summary string passed to the semantic ranker is 2,048 tokens. Previously, it was 256 tokens.
 
 ### How ranking is scored
 
-Scoring is done over the caption, and any other content from the summary string that fills out the 256 token length.
+Scoring is done over the caption, and any other content from the summary string that fills out the 2,048 token length.
 
 1. Captions are evaluated for conceptual and semantic relevance, relative to the query provided.
 
@@ -131,7 +131,7 @@ Semantic ranker is available on search services at the Basic and higher tiers, s
 
 When you enable semantic ranker, choose a pricing plan for the feature:
 
-* At lower query volumes (under 1000 monthly), semantic ranking is free.
+* At lower query volumes (under 1,000 monthly), semantic ranking is free.
 * At higher query volumes, choose the standard pricing plan.
 
 The [Azure AI Search pricing page](https://azure.microsoft.com/pricing/details/search/) shows you the billing rate for different currencies and intervals.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Searchにおけるセマンティックランクの概要に関する記事の修正"
}
```

### Explanation
このコードの変更は、「Azure AI Searchにおけるセマンティックランクの概要」に関する記事が修正されたことを示しています。この更新により、記事の内容が最新の情報を反映し、ユーザーにとってより有用なものになっています。

主な変更点は以下の通りです：
- 記事の日付が「2024年9月24日」から「2024年12月10日」に更新されました。
- セマンティックランカーについての説明において、「ベクトル」と「類似性検索」に関する文言が修正され、より理解しやすくなりました。
- 各ドキュメントの要約を生成する際のトークンの最大長が「256トークン」から「2048トークン」に増加したことが言及され、これによってより詳細な情報を提供できるようになったことが説明されています。
- セマンティックランクの無料利用について、月間クエリ数が「1000未満」から「1,000未満」と表記を統一しました。

これらの変更によって、読者はセマンティックランキングの機能や、関連する制限についての情報をより明瞭に理解できるようになっています。

## articles/search/service-configure-firewall.md{#item-75be3f}

<details>
<summary>Diff</summary>
````diff
@@ -160,7 +160,7 @@ The trusted services are used for vectorization workloads: generating vectors fr
 1. On the **Roles** page:
 
    + Select **Search Index Data Contributor** to load a search index with vectors generated by an embedding model. Choose this role if you intend to use integrated vectorization during indexing.
-   + Or, select **Search Index Data Reader** to provide queries with a vector generated by an embedding model. The embedding used in a query isn't written to an index, so no write permissions are required.
+   + Or, select **Search Index Data Reader** to provide queries containing a vector generated by an embedding model at query time. The embedding used in a query isn't written to an index, so no write permissions are required.
 
 1. Select **Next**.
 1. On the **Members** page, select **Managed identity** and **Select members**.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファイアウォール構成に関する記事の文言修正"
}
```

### Explanation
このコードの変更は、「ファイアウォールの構成」に関する記事の内容が修正されたことを示しています。この更新により、特定の役割に関する説明が明確になり、読者にとって理解しやすくなっています。

具体的な変更点は以下の通りです：
- 修正された部分では、「Search Index Data Reader」役割についての説明が、クエリ時にベクトルを提供できることを明示しています。具体的には、ベクトルがクエリの際に生成されることを強調し、ユーザーの理解を助けるためにより詳しい説明が追加されました。

このような文言の修正により、読者はファイアウォール構成の設定における役割について、より正確で具体的な情報を得ることができます。

## articles/search/toc.yml{#item-c4768f}

<details>
<summary>Diff</summary>
````diff
@@ -430,20 +430,20 @@ items:
     href: hybrid-search-how-to-query.md
   - name: Ranking and relevance
     items:
+    - name: Add a scoring profile
+      href: index-add-scoring-profiles.md
+    - name: Configure BM25 ranking
+      href: index-ranking-similarity.md
     - name: Enable or disable semantic ranker
       href: semantic-how-to-enable-disable.md      
     - name: Configure semantic ranker
       href: semantic-how-to-configure.md
     - name: Add semantic ranking to queries
-      displayName: query
       href: semantic-how-to-query-request.md
     - name: Rewrite queries with semantic ranker
-      displayName: query
       href: semantic-how-to-query-rewrite.md
-    - name: Add a scoring profile
-      href: index-add-scoring-profiles.md
-    - name: Configure BM25 ranking
-      href: index-ranking-similarity.md
+    - name: Migrate semantic ranking code
+      href: semantic-code-migration.md
   - name: Security
     items:
     - name: Configure network access
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索に関する目次ファイルの更新"
}
```

### Explanation
このコードの変更は、検索に関する目次ファイル (`toc.yml`) の内容が修正されたことを示しています。この更新によって、目次の構成が見直され、より整理された形になっています。

主な変更点は以下の通りです：
- 新たに「スコアリングプロファイルの追加」と「BM25ランクの設定」に関する項目が追加され、リンクが提供されました。
- 従来の「クエリ」として表示されていた項目が変更され、具体的な内容やリンクが整理されました。具体的には、セマンティックランカーに関連する「クエリの追加」および「クエリの書き換え」についての表記が修正され、新しい項目として「セマンティックランクのコード移行」が追加されました。

これにより、ユーザーは検索機能に関連する情報をより効率的に探索できるようになり、必要なリソースへアクセスしやすくなっています。

## articles/search/vector-search-how-to-query.md{#item-9bb93c}

<details>
<summary>Diff</summary>
````diff
@@ -400,18 +400,20 @@ api-key: {{admin-api-key}}
             "kind": "text",
             "text": "mystery novel set in London",
             "fields": "descriptionVector, synopsisVector",
-            "k": 5
+            "k": 50
         },
         {
             "kind": "text"
             "text": "living english author",
             "fields": "authorBioVector",
-            "k": 5
+            "k": 50
         }
     ]
 }
 ```
 
+Whenever you use semantic ranking with vectors, make sure `k` is set to 50. Semantic ranker uses up to 50 matches as input. Specifying less than 50 deprives the semantic ranking models of necessary inputs.
+
 The scored results from all four queries are fused using [RRF ranking](hybrid-search-ranking.md). Secondary [semantic ranking](semantic-search-overview.md) is invoked over the fused search results, but on the `searchFields` only, boosting results that are the most semantically aligned to `"search":"mystery novel set in London"`.
 
 > [!NOTE]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベクトル検索のクエリに関する文書の更新"
}
```

### Explanation
このコードの変更は、「ベクトル検索のクエリ」に関する文書の内容が更新されたことを示しています。この修正により、クエリにおけるパラメータ設定の重要性が強調されています。

主な変更点は次の通りです：
- クエリ内の `k` パラメータの値が、従来の5から50に変更されました。これにより、より多くの結果を考慮するように設定されています。
- さらに、セマンティックランキングとベクトルを使用する際に、`k` を50に設定する必要性が明記されました。この設定の重要性を説明するとともに、50未満に設定するとセマンティックランキングモデルにとって必要な入力が不足することになります。
- 最後に、クエリから得られたスコア付き結果が、RRFランクを使用して融合されることについての追加情報が提供され、融合された結果に対してセマンティックランキングが適用されることが記述されています。

この変更により、ユーザーはベクトル検索を行う際の適切な設定を理解し、検索結果の質を向上させることが期待されます。

## articles/search/whats-new.md{#item-fa71b4}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: HeidiSteen
 ms.author: heidist
 ms.service: azure-ai-search
 ms.topic: overview
-ms.date: 11/05/2024
+ms.date: 12/11/2024
 ms.custom:
   - references_regions
   - ignite-2024
@@ -20,6 +20,12 @@ ms.custom:
 > [!NOTE]
 > Preview features are announced here, but we also maintain a [preview features list](search-api-preview.md) so you can find them in one place.
 
+## December 2024
+
+| Item&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type |  Description |
+|-----------------------------|------|--------------|
+| [**RAG chat with Azure AI Search + Python**](https://azure.github.io/ai-app-templates/repo/azure-samples/azure-search-openai-demo/) | Template | An AI application template for building a RAG solution using Azure AI Search and Python. |
+
 ## November 2024
 
 | Item&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type |  Description |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新機能リストの更新"
}
```

### Explanation
このコードの変更は、「新機能」についての文書が更新されたことを示しています。具体的には、リリース日の日付が変更され、2024年12月の新機能が追加されました。

主な変更点は以下の通りです：
- 文書の日付が2024年11月5日から2024年12月11日に更新されました。この変更は、将来の機能に関する情報をより正確に反映させるためのものです。
- 新しく「2024年12月」というセクションが追加され、その中にAzure AI SearchとPythonを使用したRAGソリューションを構築するためのAIアプリケーションテンプレートについての情報が含まれています。このテンプレートのリンクも提供されています。
- 既存の「2024年11月」セクションも存在し、内容は引き続き維持されています。

これにより、ユーザーは最新の機能リリース情報を把握しやすくなり、新しい機能やテンプレートの利用を促進することが期待されます。


