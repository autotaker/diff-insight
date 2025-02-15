---
date: '2025-02-15'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f2b9798...MicrosoftDocs:b07793e
summary: この差分では、3つの異なるファイルでドキュメントの軽微な更新が行われ、新しい情報と最新の形式性が取り入れられています。特に新機能は追加されていませんが、文書の情報が最新バージョンに対応して更新されています。破壊的変更はないものの、スキルタイプの変更が文書インテリジェンスの実装に影響する可能性があります。主な更新として、文書インテリジェンスレイアウトスキルのスキルタイプ、Azure
  Identityクライアントライブラリの最新化、プライベートSQLへのアクセス手順の改善が含まれています。これにより、ユーザーはより効率的に情報を取得できるようになり、業務上の障害を減らせる支援がされています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f2b9798...MicrosoftDocs:b07793e){target="_blank"}

# ハイライト

この差分においては、ドキュメントの軽微な更新が3つの異なるファイルで行われました。それぞれのドキュメントで新しい情報と最新の形式性が取り入れられています。

## 新機能
特に新しい機能は直接的には追加されていませんが、文書内の情報が新しいバージョンに対応して更新されています。

## 破壊的変更
明確な破壊的変更はありませんが、スキルタイプの変更により、文書インテリジェンスの実装に影響を与える可能性があります。

## その他の更新
- 文書インテリジェンスレイアウトスキルのスキルタイプが更新されました。
- Azure Identityクライアントライブラリのバージョンが最新化されました。
- プライベートSQLへのアクセス手順のフォーマットが改善されました。

# インサイト

この差分では、軽微な更新が行われ、主に文書の更新と形式の改善が行われています。これにより、ユーザーがドキュメントを利用する際により効率的に情報を取得できるようになっています。

新しいスキルタイプ`#Microsoft.Skills.Util.DocumentIntelligenceLayoutSkill`への変更は、機械学習やAI技術によるインテリジェントな文書解析の精度と効果を期待させるものであり、ビジネス用途や情報管理の向上に貢献します。

また、Azure Identityのライブラリが更新されることで、最新のセキュリティアップデートに追随でき、これにより潜在的なセキュリティリスクを軽減できます。この種の定期的なバージョンアップは、特に企業にとって重要で、常に最新の情報セキュリティ要件を満たし続けるために必要です。

さらに、プライベートSQLへのアクセス手順の改善は、利用者の可読性を向上させ、より直感的に手順を追いやすくしています。特に接続文字列に関する注記が強調されたことで、間違った設定によるトラブルを防ぐ助けとなります。これにより、ユーザーは正確にSQLインスタンスに接続でき、業務上の障害を減らすことが可能です。このような改善により、ドキュメントの全体的な質が向上し、ユーザーが安心してプラットフォームを活用する支援をしています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [cognitive-search-skill-document-intelligence-layout.md](#item-62c06f) | minor update | 文書インテリジェンスレイアウトスキルに関する変更 | modified | 2 | 2 | 4 | 
| [keyless-connections.md](#item-3f0d72) | minor update | キーなし接続に関する依存関係のバージョン更新 | modified | 2 | 2 | 4 | 
| [search-indexer-how-to-access-private-sql.md](#item-1bd4cc) | minor update | プライベートSQLへのアクセス方法の手順修正 | modified | 1 | 2 | 3 | 


# Modified Contents
## articles/search/cognitive-search-skill-document-intelligence-layout.md{#item-62c06f}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - references_regions
   - ignite-2024
 ms.topic: reference
-ms.date: 11/20/2024
+ms.date: 02/13/2025
 ---
 
 # Document Layout skill
@@ -123,7 +123,7 @@ The file reference object can be generated in one of following ways:
   "skills": [
     {
       "description": "Analyze a document",
-      "@odata.type": "#Microsoft.Skills.Util.DocumentLayoutAnalysisSkill",
+      "@odata.type": "#Microsoft.Skills.Util.DocumentIntelligenceLayoutSkill",
       "context": "/document",
       "outputMode": "oneToMany", 
       "markdownHeaderDepth": "h3", 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文書インテリジェンスレイアウトスキルに関する変更"
}
```

### Explanation
このコードの変更は、`articles/search/cognitive-search-skill-document-intelligence-layout.md`というファイルに対する軽微な更新を示しています。具体的には、文書に関連する2つの日付の変更とスキルのタイプの更新が行われました。

まず、`ms.date`が「2024年11月20日」から「2025年2月13日」に変更され、文書の更新日付が未来に設定されました。次に、`@odata.type`の値が「#Microsoft.Skills.Util.DocumentLayoutAnalysisSkill」から「#Microsoft.Skills.Util.DocumentIntelligenceLayoutSkill」に変更され、これは異なるスキルタイプを示しています。

これらの変更は、機能を備えた文書管理システムにおいて、より正確で最新の情報を提供することを目的としています。

## articles/search/keyless-connections.md{#item-3f0d72}

<details>
<summary>Diff</summary>
````diff
@@ -53,7 +53,7 @@ Install the [Azure Identity client library for Java](https://mvnrepository.com/a
         <dependency>
             <groupId>com.azure</groupId>
             <artifactId>azure-identity</artifactId>
-            <version>1.10.0</version>
+            <version>1.15.1</version>
             <type>pom</type>
             <scope>import</scope>
         </dependency>
@@ -387,4 +387,4 @@ Create environment variables for your deployed and keyless Azure AI Search resou
 
 * [Keyless connections developer guide](/azure/developer/intro/passwordless-overview)
 * [Azure built-in roles](/azure/role-based-access-control/built-in-roles)
-* [Set environment variables](/azure/ai-services/cognitive-services-environment-variables)
\ No newline at end of file
+* [Set environment variables](/azure/ai-services/cognitive-services-environment-variables)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "キーなし接続に関する依存関係のバージョン更新"
}
```

### Explanation
このコードの変更は、`articles/search/keyless-connections.md`というファイルに対する軽微な更新を示しています。主な変更点は、Java用のAzure Identityクライアントライブラリのバージョンを更新したことです。

具体的には、依存関係のセクションにおいて、`azure-identity`ライブラリのバージョンが「1.10.0」から「1.15.1」に変更されました。これにより、最新の機能やセキュリティパッチを含む新しいバージョンが利用できるようになります。

加えて、ファイルの最後にある関係するリンクは、整形が改善され、コードの可読性が向上しました。これらの変更は、ドキュメントの利用者に対して、より適切で安全なライブラリの使用を促進することを目的としています。

## articles/search/search-indexer-how-to-access-private-sql.md{#item-1bd4cc}

<details>
<summary>Diff</summary>
````diff
@@ -126,9 +126,8 @@ You can now configure an indexer and its data source to use an outbound private
 
 This article assumes a [REST client](search-get-started-rest.md) and uses the REST APIs.
 
-1. Get an ADO connection string for your SQL managed instance in the **VNet-local endpoint** syntax. By default, a managed instance listens on port 3342, but on a virtual network it listens on 1433.
 
-1. [Create the data source definition](search-how-to-index-sql-database.md) as you would normally for Azure SQL.
+1. [Create the data source definition](search-how-to-index-sql-database.md) as you would normally for Azure SQL. By default, a managed instance listens on port 3342, but on a virtual network it listens on 1433.
 
     Provide the connection string that you copied earlier with an Initial Catalog set to your database name.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベートSQLへのアクセス方法の手順修正"
}
```

### Explanation
このコードの変更は、`articles/search/search-indexer-how-to-access-private-sql.md`というファイルに対する軽微な更新を示しています。主な変更点は、SQLマネージドインスタンスとの接続手順のフォーマットが改善されたことです。

具体的には、手順の最初の部分が修正され、接続文字列に関する説明が回番号の前に移動されています。これにより、ASD向けの接続文字列についての注意事項がより明確に強調され、理解しやすくなっています。元々「1.」として記載されていた部分が削除され、新しい手順が「1.」として再列挙されています。

これらの変更は、文書の構造と可読性を向上させ、ユーザーがプライベートSQLインスタンスに正しくアクセスできるようにするためのもので、実用的なガイダンスを提供することを目的としています。


