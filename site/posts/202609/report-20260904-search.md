---
date: '2026-09-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1b8d987...MicrosoftDocs:453abd5
summary: この記事の更新では、検索機能に関する最新情報が提供され、APIキーからロールベースアクセスへの移行が強調されています。この変更により、セキュリティが強化され、情報の理解が促進されます。新しい機能としては、APIキーの使用からロールベースアクセスへの具体的なガイドラインや、「Search
  Service Contributor」ロールの権限に関する詳細が含まれています。また、ロールベースのアクセス制御に関わる権限の拡張という破壊的変更があります。その他、記事の日付や情報の整理、セクションタイトルの調整も行われています。全体として、今回の更新はAzure
  AI Searchのユーザーや管理者に対し、重要な知識を提供し、セキュリティと運用の効率化に貢献するものとなっています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1b8d987...MicrosoftDocs:453abd5){target="_blank"}

<format>
# ハイライト
この記事の更新は、検索機能に関する文書の最新情報を提供し、APIキーからロールベースアクセスへの移行を強調しています。この結果、セキュリティの強化と情報の理解を促進する変更が含まれています。

## 新しい機能
- APIキーの使用からロールベースアクセスへの具体的な多々なガイドライン。
- 「Search Service Contributor」ロールの権限に関する詳細。

## 破壊的変更
- ロールベースのアクセス制御(RBAC)に関わる権限の拡張。

## その他の更新
- 記事の日付の更新。
- テーブル情報の整理と明確化。
- セクションタイトルの変更と調整。

# 洞察
今回の更新により、文書は検索機能とセキュリティに関する明確で詳細な知識を提供することに焦点を当てています。特に、検索サービスにおけるセキュリティ管理の方法、APIキーからロールベースのアクセスへの移行、RBACの実装に関する理解が深まります。

「articles/search/search-limits-quotas-capacity.md」の更新では、日付や容量に関する情報を最新のものに保つための修正が加えられ、これによりユーザーは現在のサービスキャパシティを正しく評価することができます。地域情報の誤記修正は、読みやすさを向上させ、誤解を避ける助けとなります。

「articles/search/search-security-api-keys.md」と「articles/search/search-security-rbac.md」の更新では、APIキーからロールベースアクセスモデルへの移行が強調されており、より高いセキュリティを達成するための明確なステップが示されています。特に、特定のロールがどのキーと相当するか、および各ロールが持つ権限の詳細が明記されました。この情報は組織のセキュリティ管理者にとって重要で、適切なアクセス制御を行うための指針となります。

まとめると、今回の文書の更新はAzure AI Searchの利用者や管理者に重要な知識を提供し、セキュリティと運用の効率化に貢献するものです。これにより、組織内でのセキュリティ維持と、利用者の体験向上を図ることが可能となります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-limits-quotas-capacity.md](#item-3b201a) | minor update | 検索制限、クオータ、キャパシティの更新 | modified | 13 | 13 | 26 | 
| [search-security-api-keys.md](#item-d8c908) | minor update | APIキーからロールベースアクセスへの移行に関する更新 | modified | 7 | 3 | 10 | 
| [search-security-rbac.md](#item-a5d129) | minor update | RBACにおけるSearch Service Contributorの権限の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/search-limits-quotas-capacity.md{#item-3b201a}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ author: mattwojo
 ms.author: mattwoj
 ms.service: azure-ai-search
 ms.topic: limits-and-quotas
-ms.date: 08/17/2026
+ms.date: 09/03/2026
 ms.update-cycle: 180-days
 ai-usage: ai-assisted
 ms.custom:
@@ -94,9 +94,9 @@ This table shows the progression of storage quota increases in GB over time. Sta
 | After May 17, 2024 <sup>2</sup> | 15  | 160 | 512 | 1,024 | **2,048**  | **4,096**  | N/A |
 | After February 10, 2025 <sup>3</sup> | 15  | 160 | 512 | 1,024 | 2,048  | 4,096  | N/A |
 
-<sup>1</sup> Higher capacity storage for Basic, S1, S2, and S3 in these regions. **Americas**: Brazil South​, Canada Central​, Canada East​​, East US​, East US 2, ​Central US​, North Central US​, South Central US​, West US​, West US 2​, West US 3​, West Central US. **Europe**: France Central​. Italy North​​, North Europe​​, Norway East, Poland Central​​, Switzerland North​, Sweden Central​, UK South​, UK West​. **Middle East**:  UAE North. **Africa**: South Africa North. **Asia Pacific**: Australia East​, Australia Southeast​​, Central India, Jio India West​, East Asia, Southeast Asia​, Japan East, Japan West​, Korea Central, Korea South​.
+<sup>1</sup> Higher capacity storage for Basic, S1, S2, and S3 in these regions. **Americas**: Brazil South, Canada Central, Canada East, East US, East US 2, Central US, North Central US, South Central US, West US, West US 2, West US 3, West Central US. **Europe**: France Central. Italy North, North Europe, Norway East, Poland Central, Switzerland North, Sweden Central, UK South, UK West. **Middle East**:  UAE North. **Africa**: South Africa North. **Asia Pacific**: Australia East, Australia Southeast, Central India, Jio India West, East Asia, Southeast Asia, Japan East, Japan West, Korea Central, Korea South.
 
-<sup>2</sup> Higher capacity storage for L1 and L2. More regions provide higher capacity at every billable tier. **Americas:** East US 2 EUAP. **Europe**: Germany North​, Germany West Central, Switzerland West​. **Azure Government**: Texas, Arizona, Virginia. **Africa**: South Africa North​. **Asia Pacific**: China North 3, China East 3.
+<sup>2</sup> Higher capacity storage for L1 and L2. More regions provide higher capacity at every billable tier. **Americas:** East US 2 EUAP. **Europe**: Germany North, Germany West Central, Switzerland West. **Azure Government**: Texas, Arizona, Virginia. **Africa**: South Africa North. **Asia Pacific**: China North 3, China East 3.
 
 <sup>3</sup> Higher capacity storage is available in West Europe.
 
@@ -105,7 +105,7 @@ This table shows the progression of storage quota increases in GB over time. Sta
 >
 > + Israel Central
 > + Qatar Central
-> + ⁠Spain Central
+> + Spain Central
 > + South India
 
 <!-- End include -->
@@ -318,24 +318,24 @@ A [knowledge base](agentic-retrieval-how-to-create-knowledge-base.md) specifies
 |--|--|--|--|--|--|--|--|--|--|
 | Maximum knowledge sources per service | 3 | 5 or 15 <sup>1</sup> | 50 | 200 | 200 | 0 | 10 | 10 | 30 |
 | Maximum knowledge bases per service | 3 | 5 or 15 <sup>1</sup> | 50 | 200 | 200 | 0 | 10 | 10 | 30 |
-| Maximum knowledge sources per knowledge base (`minimal`) <sup>2</sup> | 3 | 5 or 10 <sup>1</sup> | 10 | 10 | 10 | 0 | 10 | 10 | 10 |
-| Maximum knowledge sources per knowledge base  (`low`) | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 |
-| Maximum knowledge sources per knowledge base  (`medium`) | 3 | 5 | 5 | 5 | 5 | 0 | 5 | 5 | 5 |
+| Maximum knowledge sources per knowledge base | 3 | 5 or 10 <sup>1</sup> | 10 | 10 | 10 | 0 | 10 | 10 | 10 |
 
 <sup>1</sup> Basic services created before April 3, 2024 have lower limits (5) on knowledge sources and knowledge bases.
 
-### Knowledge sources per knowledge base
+### Knowledge source selection during retrieval
 
-Per-knowledge-base limits on knowledge sources depend on the API version used to create or update the knowledge base. In `2026-05-01-preview` and later, all retrieval reasoning efforts support the same knowledge source limits. Earlier preview API versions have lower limits for `low` and `medium` reasoning efforts.
+A knowledge base can contain up to the tier-specific maximum shown above, regardless of the API version or retrieval reasoning effort. The API version and reasoning effort instead affect how many knowledge sources can be selected during retrieval.
 
 | API version | Retrieval reasoning effort | Free | Basic | S1 | S2 | S3 | S3 HD | L1 | L2 |
 |--|--|--|--|--|--|--|--|--|--|
 | `2026-05-01-preview` and later | `minimal`, `low`, `medium` | 3 | 5 or 10 <sup>1</sup> | 10 | 10 | 10 | 0 | 10 | 10 |
-| `2026-05-01-preview`, `2025-08-01-preview` | `minimal` <sup>2</sup> | 3 | 5 or 10 <sup>1</sup> | 10 | 10 | 10 | 0 | 10 | 10 |
-| `2026-05-01-preview`, `2025-08-01-preview` | `low` | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 |
-| `2026-05-01-preview`, `2025-08-01-preview` | `medium` | 3 | 5 | 5 | 5 | 5 | 0 | 5 | 5 |
+| `2026-04-01`, `2025-11-01-preview` | `minimal` <sup>2</sup> | 3 | 5 or 10 <sup>1</sup> | 10 | 10 | 10 | 0 | 10 | 10 |
+| `2025-11-01-preview` | `low` | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 |
+| `2025-11-01-preview` | `medium` | 3 | 5 | 5 | 5 | 5 | 0 | 5 | 5 |
+
+The `2025-08-01-preview` uses the legacy knowledge agent contract and doesn't support `retrievalReasoningEffort`.
 
-<sup>2</sup> In earlier preview API versions, the `minimal` reasoning effort supports more knowledge sources than `low` or `medium` because it bypasses LLM-based query planning.
+<sup>2</sup> The `minimal` reasoning effort uses all knowledge sources in the knowledge base because it bypasses LLM-based query planning.
 
 ## Data limits (AI enrichment)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "検索制限、クオータ、キャパシティの更新"
}
```

### Explanation
この修正では、「articles/search/search-limits-quotas-capacity.md」文書に対して、いくつかの重要な更新が行われました。主な変更内容には、日付の修正やテーブル内の情報の整理が含まれています。

具体的には、最初に記載されていた日付が2026年8月17日から2026年9月3日に更新されました。これにより、情報の最新性が維持されます。また、ストレージ容量の増加に関するテーブル内の地域情報が修正され、視覚的に明確化されました。いくつかの地域名が不必要な空白を排除されて修正されており、読みやすさが向上しています。

テキストのセクションタイトルも「知識ソースごとの制限」から「知識ソースの選択（取得中）」に変更されており、内容がより適切なものとなっています。更に、APIのバージョンや取得の推論努力に関する新しい情報も追加されました。これらの更新により、文書はより明確で、利用者にとって理解しやすいものになっています。

## articles/search/search-security-api-keys.md{#item-d8c908}

<details>
<summary>Diff</summary>
````diff
@@ -325,10 +325,14 @@ After you create new keys via portal or management layer, access is restored to
 
 ## Migrate from keys to roles
 
-If you want to transition to role-based access, it's helpful to understand how keys map to [built-in roles in Azure AI Search](search-security-rbac.md#built-in-roles):
+To replace key-based access with role-based access, use the following role assignments:
 
-+ An admin key corresponds to the **Search Service Contributor** and **Search Index Data Contributor** roles.
-+ A query key corresponds to the **Search Index Data Reader** role.
++ To replace an admin key, assign **Search Service Contributor** to manage search objects and **Search Index Data Contributor** for direct data plane access.
+
++ To replace a query key, assign **Search Index Data Reader**.
+
+> [!IMPORTANT]
+> Search Service Contributor is a control plane role that can retrieve admin keys, which provide full read-write access to the data plane. Only grant this role to trusted users.
 
 ## Secure keys
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIキーからロールベースアクセスへの移行に関する更新"
}
```

### Explanation
この修正は、「articles/search/search-security-api-keys.md」文書において、APIキーからロールベースのアクセスに移行する際の指針に関する内容を更新しました。主な変更点として、ボリュームの増加や説明の追加があります。

具体的には、APIキーの代わりにロールベースのアクセスを使用する方法が明確化され、どのロールがどのキーに相当するかの情報が更新されました。特に、管理者キーは「Search Service Contributor」と「Search Index Data Contributor」ロールに、クエリキーは「Search Index Data Reader」ロールにそれぞれ置き換えられることが明示されています。

さらに、重要な注意事項が新たに追加されており、「Search Service Contributor」ロールは管理者キーの取得が可能であるため、信頼できるユーザーにのみこのロールを付与することを推奨しています。これにより、セキュリティ面での警告が強調され、利用者にとって有益な情報が提供されています。全体として、文書はロールベースアクセスの実装に関する理解を深めるための重要なポイントが含まれる形で更新されています。

## articles/search/search-security-rbac.md{#item-a5d129}

<details>
<summary>Diff</summary>
````diff
@@ -62,7 +62,7 @@ The following built-in roles grant permissions to Azure AI Search. Control plane
 | [Owner](/azure/role-based-access-control/built-in-roles#owner) | Control | <ul><li>Full control plane access, including the ability to assign roles and change authentication settings.</li><li>Subscription administrators have this role by default.</li><li>Can manage API keys.</li><li>Can't create search objects, load documents, query indexes, or retrieve from knowledge bases.</li></ul> |
 | [Contributor](/azure/role-based-access-control/built-in-roles#contributor) | Control | <ul><li>Same level of control plane access as Owner, minus the ability to assign roles.</li></ul> |
 | [Reader](/azure/role-based-access-control/built-in-roles#reader) | Control | <ul><li>Read-only control plane access.</li><li>Can view service metrics and object definitions.</li><li>Can't view or manage API keys, load documents, query indexes, or retrieve from knowledge bases.</li></ul> |
-| [Search Service Contributor](/azure/role-based-access-control/built-in-roles#search-service-contributor) | Control & Data | <ul><li>Full control plane access. Data plane access is limited to object management.</li><li>Can create indexes, indexers, skillsets, knowledge bases, and other search objects.</li><li>Can't load documents, query indexes, or retrieve from knowledge bases.</li><li>For the full permissions list, see [`Microsoft.Search/searchServices/*`](/azure/role-based-access-control/permissions/ai-machine-learning#microsoftsearch).</li></ul> |
+| [Search Service Contributor](/azure/role-based-access-control/built-in-roles#search-service-contributor) | Control & Data | <ul><li>Full control plane access. Data plane access is limited to object management.</li><li>Can create indexes, indexers, skillsets, knowledge bases, and other search objects.</li><li>Can retrieve admin and query API keys through control plane operations.</li><li>Can't load documents, query indexes, or retrieve from knowledge bases directly through role-based access.</li><li>For the full permissions list, see [`Microsoft.Search/searchServices/*`](/azure/role-based-access-control/permissions/ai-machine-learning#microsoftsearch).</li></ul> |
 | [Search Index Data Contributor](/azure/role-based-access-control/built-in-roles#search-index-data-contributor) | Data | <ul><li>Read-write content access.</li><li>Can load documents, query indexes, and retrieve from knowledge bases.</li><li>Can't modify object definitions or retrieve admin keys.</li></ul> |
 | [Search Index Data Reader](/azure/role-based-access-control/built-in-roles#search-index-data-reader) | Data | <ul><li>Read-only content access.</li><li>Can query indexes and retrieve from knowledge bases.</li><li>Can't load documents, modify object definitions, or retrieve admin keys.</li></ul> |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RBACにおけるSearch Service Contributorの権限の更新"
}
```

### Explanation
この修正は、「articles/search/search-security-rbac.md」文書におけるロールベースのアクセス制御（RBAC）に関する詳細を更新しました。特に、「Search Service Contributor」ロールの権限が明確にされました。

具体的には、今までの説明に加え、「Search Service Contributor」ロールが管理者およびクエリーAPIキーを取得できることが追加されました。この変更により、ユーザーはこのロールを使用することで、どのように管理者キーやクエリキーを取得できるかを理解しやすくなります。ただし、役割ベースのアクセスを通じて文書の読み込み、インデックスのクエリ、知識ベースからの取得は直接行えないことも明示されています。

この修正により、「Search Service Contributor」ロールの機能がより明確にユーザーに提供され、Azure AI Searchのセキュリティモデルに対する理解が深まることが期待されます。全体として、文書は役割と権限に関する重要な情報が強化された形で更新されています。


