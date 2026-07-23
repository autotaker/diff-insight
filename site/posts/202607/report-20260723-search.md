---
date: '2026-07-23'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1958566...MicrosoftDocs:d74629f
summary: この変更は、Azure AI Searchに関連する複数のドキュメントのマイナーアップデートを示しています。説明が明確化され、新しい情報が追加されています。特に、デバッグセッションやLuceneクエリ構文、OData検索スコア関数に関する重要な制約や推奨事項が強調されています。デバッグセッションではカスタムスキル関連のアイデンティティのサポート状況が追加され、OData検索スコア関数においては、`search.score()`を用いた並べ替え機能が強化されています。また、ドキュメント全体の構造や説明が整理され、より実用的な内容となっています。これにより、Azure
  AI Searchのユーザーはより効果的に製品を活用できるようになります。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1958566...MicrosoftDocs:d74629f){target="_blank"}

<format>
# Highlights
この変更は、Azure AI Searchに関連する複数のドキュメントのマイナーアップデートを示しています。各記事で、特定の機能や設定に関する説明が明確化され、新しい情報が追加されています。デバッグセッション、Luceneクエリ構文、プライベート接続、およびOData検索スコア関数における重要な制約や推奨事項が強調されています。

## New features
- デバッグセッションでは、カスタムスキル関連のマネージドアイデンティティのサポート状況が追加
- Luceneクエリ構文では、ブーストの仕組みや優先順位付け方法の詳細な説明が追加
- OData検索スコア関数で、新たに利用可能な機能として、`search.score()`を用いた並べ替え機能が強化

## Breaking changes
- デバッグセッションが共有プライベートリンクをサポートしないことの明記
- OData検索スコア関数で、`search.score()`を純粋なベクトルまたはハイブリッドクエリで使用できない制約が追加

## Other updates
- ドキュメント全体にわたる説明の精緻化と構造の整理
- クロスリファレンスの改善とトラブルシューティングガイドの追加

# Insights
Azure AI Searchの利用者にとって、最新のドキュメント更新は実用的であり、具体的に役立つ情報が増えています。特にデバッグセッション周りの更新では、開発者が問題の根本原因を迅速に特定するための手段が強化されました。プライベートリンクを使用している場面でのデバッグに関する制限など、重要な点が明確にされています。

Luceneクエリ構文の改訂では、検索機能の高度な使用法について深い理解が得られる助けになります。特に検索のブーストやフィールド検索の説明が強化され、検索シナリオに応じたクエリ構築が容易になりました。

OData検索スコア関数の文書更新は、開発者が`search.score()`を使用して検索結果を的確にプロファイルするための有益な情報を提供しています。制約の追加により、誤った実装をすることを防ぎ、より効率的なデータ検索を実現するための指針が明確になっています。

全体として、これらの文書はユーザーがAzure AI Searchを効果的に使用し、潜在的な問題を事前に回避するのに役立ちます。特に新しく追加された情報や制約は、製品をより堅牢に使用するために不可欠な知識を提供しています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-debug-session.md](#item-edf092) | minor update | Cognitive Search Debug Sessionに関する内容の更新 | modified | 20 | 12 | 32 | 
| [query-lucene-syntax.md](#item-736436) | minor update | Luceneクエリ構文に関するドキュメントの更新 | modified | 53 | 8 | 61 | 
| [search-indexer-howto-access-private.md](#item-73d30d) | minor update | プライベート接続に関するドキュメントの更新 | modified | 3 | 1 | 4 | 
| [search-query-odata-search-score-function.md](#item-f51766) | minor update | OData検索スコア関数に関するドキュメントの更新 | modified | 8 | 3 | 11 | 


# Modified Contents
## articles/search/cognitive-search-debug-session.md{#item-edf092}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,9 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 10/21/2025
+ms.date: 07/21/2026
 ms.update-cycle: 365-days
+ai-usage: ai-assisted
 ---
 
 # Debug Sessions in Azure AI Search
@@ -52,29 +53,36 @@ Debug Sessions work with all generally available [indexer data sources](search-d
 + For custom skills, a user-assigned managed identity isn't supported for a debug session connection to Azure Storage. As stated in the prerequisites, you can use a system managed identity, or specify a full access connection string that includes a key. For more information, see [Connect a search service to other Azure resources using a managed identity](search-how-to-managed-identities.md).
 
 + Data sources with encryption enabled via [customer managed keys (CMK)](search-security-manage-encryption-keys.md).
-  
+
++ Shared private links aren't supported. If your search service uses private endpoint connectivity to reach data sources or other resources, debug sessions can't access those resources. For a workaround, see [Debug sessions and private connectivity](#debug-sessions-and-private-connectivity).
+
 + Currently, the ability to select which document to debug is unavailable. This limitation isn't permanent and should be lifted soon. At this time, Debug Sessions selects the first document in the source data container or folder.
 
 ## How a debug session works
 
-When you start a session, the search service creates a copy of the skillset, indexer, and a data source containing a single document used to test the skillset. All session state is saved to a new blob container created by the Azure AI Search service in an Azure Storage account that you provide. The name of the generated container has a prefix of `ms-az-cognitive-search-debugsession`. The prefix is required because it mitigates the chance of accidentally exporting session data to another container in your account. 
+When you start a session, the search service creates a copy of the skillset, indexer, and a data source containing a single document used to test the skillset. The Azure AI Search service saves all session state to a new blob container that it creates in an Azure Storage account you provide. The generated container name has a prefix of `ms-az-cognitive-search-debugsession`. This prefix reduces the chance of accidentally exporting session data to another container in your account.
+
+If you configure the storage account connection by using a [managed identity](search-how-to-managed-identities.md), assign the `Storage Blob Data Contributor` role to your search service identity on the storage account. In your storage account, [enable trusted services](search-indexer-howto-access-trusted-service-exception.md) to allow write access from Azure AI Search.
 
 A cached copy of the enriched document and skillset is loaded into the visual editor so that you can inspect the content and metadata of the enriched document, with the ability to check each document node and edit any aspect of the skillset definition. Any changes made within the session are cached. Those changes won't affect the published skillset unless you commit them. Committing changes will overwrite the production skillset.
 
 If the enrichment pipeline doesn't have any errors, a debug session can be used to incrementally enrich a document, test and validate each change before committing the changes.
 
-Debug sessions help identify the root cause of errors or warnings by analyzing the data, skill inputs and outputs, and field mappings. If the indexer encounters configuration issues, such as incorrect network setup, permission-related access errors, or similar, please review the specific error message along with the linked documentation provided. For troubleshooting guidance, refer to the [common indexer errors and warnings](cognitive-search-common-errors-warnings.md).
+Debug sessions help identify the root cause of errors or warnings by analyzing data, skill inputs and outputs, and field mappings. Use the skill details pane to inspect what each skill receives as input and produces as output. This inspection helps verify that skill definitions, expressions, and field mappings are correctly formed. If the indexer encounters configuration problems, such as incorrect network setup or permission-related access errors, review the specific error message and the linked documentation. For troubleshooting guidance, see [Common indexer errors and warnings](cognitive-search-common-errors-warnings.md).
+
+## Debug sessions and private connectivity
+
+Debug sessions don't support shared private links. If your production search service uses private endpoint connectivity to access data sources or other resources, debug sessions can't run against that service.
+
+**Workaround: use a test search service**
 
-## Debug Sessions with private connectivity
+To debug your skillset, create a separate Azure AI Search service without private connectivity restrictions. To keep production data and schema details out of a non-private environment, build your test setup with synthetic documents:
 
-If your AI enrichment pipeline uses shared private links to access Azure resources, additional configuration is required to ensure indexer and debug sessions work correctly. This includes permissions, trusted access, and network setup.
+- Create test documents that match the field types and structure of your production data, but use generic field names (for example, `content`, `title`, `category`) and placeholder values instead of real data. Skillset logic depends on content types and structure, not specific field names.
+- Copy the skillset JSON from your production service. If skill inputs reference production field names, update those references to match your generic test field names. Use [field mappings](search-indexer-field-mappings.md) in the test indexer to align test field names with skillset inputs.
+- Configure an indexer to run against the test data source.
 
-- If you're using [managed identity](search-how-to-managed-identities.md), assign the necessary roles to your search service identity, including `Storage Blob Data Contributor`, so debug sessions can write session data to your storage account.
-- Ensure the search service has access to all resources referenced in the [skillset definition](cognitive-search-working-with-skillsets.md), including any used in the debug session.
-- In your storage account, [enable trusted services](search-indexer-howto-access-trusted-service-exception.md) to allow access from Azure AI Search.
-- Set `"executionEnvironment" = "private"` property in the indexer definition to ensure the [indexer runs in a private context](search-indexer-howto-access-private.md?#4---configure-the-indexer-to-run-in-the-private-environment).
-- Create a [shared private link](search-indexer-howto-access-private.md) for each resource accessed by the search service, including: your data source, if configured to indexer AI enrichment cache and knowledge store, and any other resources configured in your skillset.
-- For other troubleshooting guidance, refer to the [common indexer errors and warnings](cognitive-search-common-errors-warnings.md).
+Run the debug session on the test service to inspect skill inputs and outputs, validate skill expressions and field mappings, and identify errors. When your changes are validated, restore the original production field name references in the skillset JSON and apply it back to your production service.
 
 
 ## Debug session layout
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Cognitive Search Debug Sessionに関する内容の更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchにおけるデバッグセッションに関する文書の改訂を示しています。主な変更点として、日付の更新や新しい情報の追加が含まれています。具体的には、デバッグセッションの利用に関する注意事項や制約がより明確に記述され、特にプライベートリンクの非対応やトラブルシューティングの指針が強調されています。

追加された情報としては、カスタムスキルに関連するマネージドアイデンティティのサポート状況や、プライベート接続を利用した場合のデバッグ方法、そしてテスト用の検索サービスの作成に関するガイダンスが含まれています。これにより、ユーザーはデバッグセッションを通じてエラーの根本原因を特定しやすくなることを目的としています。

また、コードの修正によって、ドキュメントの内容が整理され、視覚エディタでの操作が効率的に行えるようになりました。これらの変更は、Azure AI Searchのユーザーが効果的に機能を使用し、問題を迅速に解決できるようサポートするためのものです。

## articles/search/query-lucene-syntax.md{#item-736436}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,9 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 02/19/2026
+ms.date: 07/20/2026
 ms.update-cycle: 365-days
+ai-usage: ai-assisted
 ---
 
 # Lucene query syntax in Azure AI Search
@@ -19,7 +20,7 @@ To use full Lucene syntax, set the queryType to `full` and pass in a query expre
 
 ## Example (full syntax)
 
-The following example is a search request constructed using the full syntax. This particular example shows in-field search and term boosting. It looks for hotels where the category field contains the term `budget`. Any documents containing the phrase `"recently renovated"` are ranked higher as a result of the term boost value (3).  
+The following example is a search request constructed using the full syntax. This particular example shows fielded search and phrase boosting. It looks for hotels where the category field contains the term `budget`. Documents containing the phrase `"recently renovated"` receive extra boost weight and might rank higher as a result of the phrase boost value (3).
 
 ```http
 POST /indexes/hotels-sample/docs/search?api-version=2026-04-01
@@ -71,7 +72,7 @@ You can embed Boolean operators in a query string to improve the precision of a
 |Text operator | Character | Example | Usage |
 |--------------|----------- |--------|-------|
 | AND | `+` | `wifi AND luxury` | Specifies terms that a match must contain. In the example, the query engine looks for documents containing both `wifi` and `luxury`. The plus character (`+`) can also be used directly in front of a term to make it required. For example, `+wifi +luxury` stipulates that both terms must appear somewhere in the field of a single document.|
-| OR | (none) <sup>1</sup> | `wifi OR luxury` | Finds a match when either term is found. In the example, the query engine returns match on documents containing either `wifi` or `luxury` or both. Because OR is the default conjunction operator, you could also leave it out, such that `wifi luxury` is the equivalent of  `wifi OR luxury`.|
+| OR | (none) <sup>1</sup> | `wifi OR luxury` | Finds a match when either term is found. In the example, the query engine returns matches on documents containing either `wifi` or `luxury` or both. With `searchMode=any`, OR is the default conjunction operator, so `wifi luxury` is equivalent to `wifi OR luxury`. With `searchMode=all`, use the explicit `OR` operator to get this behavior. |
 | NOT | `!`, `-` | `wifi –luxury` | Returns a match on documents that exclude the term. For example, `wifi –luxury` searches for documents that have the `wifi` term but not `luxury`. |
 
 <sup>1</sup> The `|` character isn't supported for OR operations.
@@ -126,11 +127,53 @@ Proximity searches are used to find terms that are near each other in a document
 
 ##  <a name="bkmk_termboost"></a> Term boosting
 
-Term boosting refers to ranking a document higher if it contains the boosted term, relative to documents that don't contain the term. This differs from scoring profiles in that scoring profiles boost certain fields, rather than specific terms.  
+Think of search as two steps. First, Azure AI Search finds matching documents. Then, it ranks those matches. Term boosting affects only the second step: it can move documents that match one part of your query higher in the results.
 
-The following example helps illustrate the differences. Suppose that there's a scoring profile that boosts matches in a certain field, say *genre* in the  [musicstoreindex example](index-add-scoring-profiles.md#example-boosting-by-weighted-text-and-functions). Term boosting could be used to further boost certain search terms higher than others. For example, `rock^2 electronic` boosts documents that contain the search terms in the genre field higher than other searchable fields in the index. Further, documents that contain the search term *rock* are ranked higher than the other search term *electronic* as a result of the term boost value (2).  
+Term boosting differs from a scoring profile. A boost favors a word, phrase, or group in the current query. A scoring profile favors fields or other index content according to rules defined in the index.
 
- To boost a term, use the caret, `^`, symbol with a boost factor (a number) at the end of the term you're searching. You can also boost phrases. The higher the boost factor, the more relevant the term is relative to other search terms. By default, the boost factor is 1. Although the boost factor must be positive, it can be less than 1 (for example, 0.20).  
+### Boost scope
+
+Write a caret (`^`) and a positive number immediately after the part of the query that you want to favor. For example, `tax^2` can move documents that contain `tax` higher than documents that match only an unboosted term. The default boost value is 1. You can also use a value between 0 and 1, such as `0.2`, to give a match less weight.
+
+The punctuation tells you which words each instruction affects:
+
+- A field name plus a colon, called a field prefix, appears before a word, quoted phrase, or parenthesized group. For example, `content:` tells Azure AI Search to look in the `content` field.
+- A boost, such as `^2`, appears after a word, quoted phrase, or parenthesized group. It tells Azure AI Search what to favor when ranking the matches.
+
+The following table uses the default `searchMode=any`, where a space between words works like `OR`.
+
+| Query | What can match | What the boost favors |
+| --- | --- | --- |
+| `deferred tax^2` | `deferred`, `tax`, or both. | Only the word `tax`. |
+| `"deferred tax"^2` | The complete phrase, with the words next to each other and in this order. | The complete phrase. |
+| `(deferred OR tax)^2` | `deferred`, `tax`, or both. | Everything inside the parentheses as one group. |
+
+With `searchMode=all`, the query `deferred tax^2` requires both words to match. The boost still applies only to `tax`. To match either word instead, write `deferred OR tax^2`.
+
+Place the caret after the closing quotation mark or parenthesis when you want to boost the entire phrase or group. Parentheses don't create a phrase. Use quotation marks when the words must be next to each other and in a specific order.
+
+### Boost and field scope
+
+A field name followed by a colon limits where Azure AI Search looks. A boost changes how Azure AI Search ranks a match. You can use both in the same query.
+
+| Query | What it means |
+| --- | --- |
+| `content:deferred tax^2` | The field prefix applies only to `deferred`. The separate `tax^2` part uses the fields selected by `searchFields`, or all searchable fields if `searchFields` isn't specified. A `tax` match gets extra ranking weight. |
+| `content:"deferred tax"^2` | Look for the complete phrase only in `content`, and give that phrase match extra ranking weight. |
+| `content:(deferred OR tax)^2` | Look for either word only in `content`, and give the grouped match extra ranking weight. |
+
+For example, if `searchFields` is set to `title`, the first query looks for `deferred` in `content` and `tax` in `title`. The quotation marks and parentheses in the other queries keep both words in `content`.
+
+> [!IMPORTANT]
+> The colon and caret work in opposite directions. The field prefix `content:` applies to the query part after it. The boost `^2` applies to the query part before it. Use quotation marks or parentheses to make that part include more than one word. For more information, see [Fielded search](#bkmk_fields) and [Precedence (grouping)](#precedence-grouping).
+
+### Effect of an analyzer on boosted queries
+
+For ordinary words, phrases, and groups of words, boosting doesn't skip text analysis. Before matching, Azure AI Search still processes the query text with each field's analyzer. As a result, the same boosted text might match differently in fields that use different analyzers.
+
+A phrase or group with a field prefix uses that field's analyzer. Text without a field prefix uses the analyzer for each field being searched. For example, an analyzer that changes text to lowercase can match `"DEFERRED TAX"^2` against lowercase indexed terms.
+
+Other query forms, such as wildcard, regular expression, and fuzzy queries, use different analysis rules. Adding a boost doesn't change those rules. For more information, see [Stage 2: Lexical analysis](search-lucene-query-architecture.md#stage-2-lexical-analysis).
 
 ##  <a name="bkmk_regex"></a> Regular expression search
  
@@ -196,9 +239,11 @@ When using Unicode characters, make sure symbols are properly escaped in the que
 
 ## Precedence (grouping)
 
-You can use parentheses to create subqueries, including operators within the parenthetical statement. For example, `motel+(wifi|luxury)` searches for documents containing the `motel` term and either `wifi` or `luxury` (or both).
+Use parentheses to control which parts of a query are evaluated together. For example, `motel AND (wifi OR luxury)` requires `motel` and at least one of the terms inside the parentheses: `wifi` or `luxury`.
+
+Place a field prefix before a parenthesized group to search that entire group in one field. For example, `hotelAmenities:(wifi OR pool)` looks for `wifi` or `pool` only in the `hotelAmenities` field.
 
-Field grouping is similar but scopes the grouping to a single field. For example, `hotelAmenities:(gym+(wifi|pool))` searches the field `hotelAmenities` for `gym` and `wifi`, or `gym` and `pool`.  
+Parentheses control how `AND` and `OR` work together. They don't require words to appear next to each other or in a specific order. Use quotation marks for that behavior. To boost a group, place the caret after the closing parenthesis, as in `hotelAmenities:(wifi OR pool)^2`. For more information, see [Boost scope](#boost-scope).
 
 ## Query size limits
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Luceneクエリ構文に関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、Azure AI SearchにおけるLuceneクエリ構文に関する文書の改訂を示しています。主な変更点として、情報の明確化、例の修正、及び新しいセクションの追加が行われています。特に、サポートされているクエリ構文やブーストの仕組み、優先順位付けの手法が詳細に説明されています。

具体的には、フィールド検索とフレーズブーストに関連する説明が改善され、ユーザーがどのように検索リクエストを構築するか、ブーストの適用方法、ブースティングのスコープに関する新しいセクションが導入されています。また、クエリ内におけるフィールドプレフィックスの利用や、ブーストに影響を与えるアナライザーの動作についても明確に述べられています。

これにより、ユーザーはLuceneクエリ構文を効果的に利用し、より正確な検索結果を得るための理解を深めることが期待されます。全体的に、文書は最新の情報に基づいて整理され、より実用的な内容となっています。

## articles/search/search-indexer-howto-access-private.md{#item-73d30d}

<details>
<summary>Diff</summary>
````diff
@@ -396,7 +396,7 @@ Azure AI Search makes outbound calls to other Azure resources in the following s
 + Knowledge base connections to Azure OpenAI for agentic retrieval workflows
 + Indexer or query connections to Azure OpenAI or Azure Vision in Foundry Tools for vectorization
 + Indexer connections to supported data sources
-+ Indexer (skillset) connections to Azure Storage for caching enrichments, debug session state, or writing to a knowledge store
++ Indexer (skillset) connections to Azure Storage for caching enrichments or writing to a knowledge store
 + Indexer (skillset) connections to Foundry Tools for billing purposes
 + Encryption key requests to Azure Key Vault
 + Custom skill requests to Azure Functions or similar resource
@@ -433,6 +433,8 @@ When evaluating shared private links for your scenario, remember these constrain
 
 + Shared private link [resource limits](search-limits-quotas-capacity.md#shared-private-link-resource-limits) vary by pricing tier.
 
++ Debug sessions don't support shared private links. If your search service uses private endpoint connectivity, you can't run debug sessions against it. For a workaround, see [Debug sessions and private connectivity](cognitive-search-debug-session.md#debug-sessions-and-private-connectivity).
+
 + When you [change your pricing tier](search-capacity-planning.md#change-your-pricing-tier), shared private link resources are evaluated against the target tier's limits. If your shared private link count exceeds the target tier's maximum, the tier change is blocked. If the tier change succeeds, existing shared private link resources aren't recreated and don't require reapproval. Private indexer connectivity continues to work after the search service returns to a "Succeeded" provisioning state and "Running" status, provided the shared private link provisioning state remains "Succeeded" and the connection status remains "Approved."
 
 ## Troubleshooting
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベート接続に関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、Azure AI Searchにおけるプライベート接続に関するドキュメントの微修正を表しています。主な変更内容は、インデクサー（スキルセット）の接続に関する説明の精緻化と、デバッグセッションに関する新しい制約の追加です。

特に、インデクサー接続において、Azure Storageへのキャッシュ用途が単に「エンリッチメントのキャッシュ」として明確化され、ナレッジストアへの書き込みに関しても同様に触れられています。また、共有プライベートリンクに関連するリソース制限に関する情報が追加され、価格帯によって異なる場合があることが強調されています。

なお、新たに「デバッグセッションは共有プライベートリンクをサポートしない」という重要な情報が追加されており、プライベートエンドポイント接続を使用している場合はデバッグセッションを実行できないことが明確にされています。これに関しては、マニュアル内の他のセクションへの参照も行われています。これにより、ユーザーがプライベート接続に関しての制限やワークアラウンドを理解しやすくなっています。全体的に、文書はユーザーにとって実用的な情報が整備されており、より理解しやすい内容となっています。

## articles/search/search-query-odata-search-score-function.md{#item-f51766}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,9 @@ ms.service: azure-ai-search
 ms.custom:
   - ignite-2023
 ms.topic: concept-article
-ms.date: 02/19/2026
+ms.date: 07/20/2026
 ms.update-cycle: 365-days
+ai-usage: ai-assisted
 translation.priority.mt:
   - "de-de"
   - "es-es"
@@ -31,16 +32,20 @@ When you send a query to Azure AI Search without the [**$orderby** parameter](se
 
 ## Syntax
 
-The syntax for `search.score` in **$orderby** is `search.score()`. The function `search.score` doesn't take any parameters. It can be used with the `asc` or `desc` sort-order specifier, just like any other clause in the **$orderby** parameter. It can appear anywhere in the list of sort criteria.
+The syntax for `search.score` in **$orderby** is `search.score()`. The function `search.score` doesn't take any parameters. For full-text queries, you can use it with the `asc` or `desc` sort-order specifier, just like any other clause in the **$orderby** parameter. It can appear anywhere in the list of sort criteria.
 
 ## Example
 
-Sort hotels in descending order by `search.score` and `rating`, and then in ascending order by distance from the given coordinates so that between two hotels with identical ratings, the closest one is listed first:
+Sort hotels in descending order by `search.score` and `rating`, and then in ascending order by distance from the given coordinates so that between two hotels with identical relevance scores and ratings, the closest one is listed first:
 
 ```odata-filter-expr
     search.score() desc,rating desc,geo.distance(location, geography'POINT(-122.131577 47.678581)') asc
 ```
 
+## Limitations
+
+You can't use `search.score()` in **$orderby** for pure vector or hybrid queries. The service rejects these requests with an HTTP 400 `InvalidRequestParameter` error. To correct the request, remove `search.score()` from **$orderby**.
+
 ## Next steps  
 
 - [OData expression language overview for Azure AI Search](query-odata-filter-orderby-syntax.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OData検索スコア関数に関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、OData検索スコア関数に関する文書の微修正と情報の追加を表しています。主に、`search.score()`の使用に関する明確化と制限事項の追加が行われています。具体的には、`search.score()`を`$orderby`パラメーターで使用する際の注意点や制限が強調されています。

変更の一部として、`search.score()`を用いた場合の説明が明確にされ、全テキストクエリに対して`asc`または`desc`の並べ替え指定子を使って利用可能であることが示されています。また、サンプルの内容も調整され、結果の relevancy スコアや評価に基づくホテルの並べ替えについて具体的に言及されています。

さらに、新たに制限に関するセクションが追加され、純粋なベクトルまたはハイブリッドクエリの場合、`search.score()`が`$orderby`で使用できないことが明記されています。このようなリクエストは、HTTP 400の`InvalidRequestParameter`エラーで拒否されることが説明されています。こうした変更により、ユーザーはより正確に`search.score()`の使用方法を理解し、エラーを避けるための知識を得ることができます。全体として、文書は明確で実用的な情報を提供するように整理されています。


