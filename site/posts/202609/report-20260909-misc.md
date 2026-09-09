---
date: '2026-09-09'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5d64e7f...MicrosoftDocs:e6b3e61
summary: Azure Document Intelligenceに関する最新の更新が行われ、新しいAPIバージョン（v4.0）の使用が推奨されると共に、サービス制限に関する情報が明確化されました。古いAPIバージョンに関する警告が削除され、関連情報が整理されました。また、ドキュメントの日付も最新に更新されました。これにより、ユーザーは必要な情報を容易に把握でき、リソースの最適な配置が可能となり、より計画的なシステム運用が推進されることが期待されます。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5d64e7f...MicrosoftDocs:e6b3e61){target="_blank"}

# ハイライト

## 新機能
- Azure Document Intelligenceの概要に、新しいAPIバージョン（v4.0）を使用する推奨が追加されました。
- サービス制限に関する情報が更新され、リソースの最大数や地域ごとの制限が明確化されました。

## 破壊的変更
- 古いAPIバージョンに関する警告が削除され、重複する情報が整理されました。
- 提供されていた一部の情報は刷新され、最新の状態に基づいた新たな情報が導入されています。

## その他の更新
- ドキュメントの日付が最新の日付に更新され、情報の鮮度が保たれています。

# 洞察

Azure Document Intelligenceの概要とサービス制限に関する更新が行われ、これによってユーザーはより実践的で確実な情報を入手できるようになりました。

概要の文書においては、特にAPIのバージョン情報が整理され、読者がどのバージョンを使用すべきか容易に判断できるような情報提供がなされています。今後の計画的な移行が求められることから、早期の策定が重要です。APIの引退日をはっきり示すことで、ユーザーは長期的な開発の計画を立てやすくなるでしょう。

一方、サービス制限に関する文書では、リソース管理に関する重要な情報が追加されました。特に地域ごとのリソース制限が明確化されたことにより、ユーザーは自分の環境に最適なリソース配置を考えることが可能になります。これらの情報が加わることで、ユーザーは自分の業務に合わせて柔軟にサービスを利用できるようになるでしょう。

このような変更は、Azureのサービスを利用する際のユーザー体験を向上させ、より効率的で計画的なシステム運用を推進する重要なものです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [overview.md](#item-4e36ba) | minor update | ドキュメントインテリジェンスの概要の更新 | modified | 15 | 22 | 37 | 
| [service-limits.md](#item-5ceae5) | minor update | ドキュメントインテリジェンスのサービス制限の更新 | modified | 4 | 1 | 5 | 


# Modified Contents
## articles/ai-services/document-intelligence/overview.md{#item-4e36ba}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: mcleans
 ms.service: azure-document-intelligence-foundry-tools
 ms.topic: overview
-ms.date: 08/15/2026
+ms.date: 09/08/2026
 ms.author: lajanuar
 monikerRange: '<=doc-intel-4.0.0'
 ai-usage: ai-assisted
@@ -43,14 +43,6 @@ ai-usage: ai-assisted
 
 Azure Document Intelligence in Foundry Tools is a cloud-based [Foundry Tools](../../ai-services/index.yml) service that you can use to build intelligent document processing solutions. Massive amounts of data, spanning various data types, are stored in forms and documents. You can use Azure Document Intelligence to effectively manage the speed at which data is collected and processed. Azure Document Intelligence is key to improved operations, informed data-driven decisions, and enlightened innovation. For information on region access, see [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).</br></br>
 
-> [!IMPORTANT]
->
-> * **Document Intelligence REST API v2.1** reaches end of support on **September 15, 2027**.
-> * **Document Intelligence REST API 2022-08-31 v3.0** reaches end of support on **March 30, 2029**.
-> * To avoid production disruption, use **Azure Document Intelligence 2024-11-30 v4.0** for all new development, and migrate existing workloads to **Azure Document Intelligence 2024-11-30 v4.0** before these retirement dates. For more information, see [**Document Intelligence migration guide**](versioning/migration-guide-overview.md).
-
-Azure Document Intelligence in Foundry Tools is a cloud-based [Foundry Tools](../../ai-services/index.yml) service that you can use to build intelligent document processing solutions. Massive amounts of data, spanning various data types, are stored in forms and documents. You can use Azure Document Intelligence to effectively manage the speed at which data is collected and processed. Azure Document Intelligence is key to improved operations, informed data-driven decisions, and enlightened innovation. For information on region access, see [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).</br></br>
-
 | ✔️ [Document analysis models](#document-analysis-models) | ✔️ [Prebuilt models](#prebuilt-models) | ✔️ [Custom models](#custom-model-overview) |
 
 > [!NOTE]
@@ -60,6 +52,20 @@ Azure Document Intelligence in Foundry Tools is a cloud-based [Foundry Tools](..
 > * Together, they make it easier to prepare data for intelligent agents and applications that can read, analyze, and respond to real-world content with precision and speed.
 > * To compare both services and determine which best fits your scenario, see [Choose the right Azure AI tool for document processing](../content-understanding/choosing-right-ai-tool.md).
 
+
+## Version support and retirement
+
+The following table summarizes Document Intelligence API version support:
+
+| Version | Status | End of support |
+|---------|--------|---------------|
+| v4.0 (2024-11-30) | GA — current | No announced date |
+| v3.1 (2023-07-31) | GA — previous | No announced date |
+| v3.0 (2022-08-31) | GA — retiring | March 30, 2029 (announced March 30, 2026) |
+| v2.1 | GA — retiring | September 15, 2027 (announced September 15, 2024) |
+
+To avoid production disruption, migrate to v4.0 before the retirement dates in the preceding table. For migration guidance, see the [Document Intelligence migration guide](versioning/migration-guide-overview.md).
+
 ## Document analysis models
 
 Document analysis (general extraction) models enable text extraction from forms and documents and return structured business-ready content for your organization's action, use, or development.
@@ -577,19 +583,6 @@ To learn more about each model and browse the API references, use the links in t
 
  As with all Foundry Tools, developers who use Document Intelligence should be aware of Microsoft policies on customer data. For more information, see [Data, privacy, and security for Document Intelligence](/azure/ai-foundry/responsible-ai/document-intelligence/data-privacy-security).
 
-## Version support and retirement
-
-The following table summarizes Document Intelligence API version support:
-
-| Version | Status | End of support |
-|---------|--------|---------------|
-| v4.0 (2024-11-30) | GA — current | No announced date |
-| v3.1 (2023-07-31) | GA — previous | No announced date |
-| v3.0 (2022-08-31) | GA — retiring | March 30, 2029 |
-| v2.1 | GA — retiring | September 15, 2027 |
-
-To avoid production disruption, migrate to v4.0 before the retirement dates above. For migration guidance, see the [Document Intelligence migration guide](versioning/migration-guide-overview.md).
-
 ## Related content
 
 :::moniker range=">=doc-intel-3.0.0"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスの概要の更新"
}
```

### Explanation
この変更は、Azure Document Intelligenceの概要に関する文書の修正を示しています。全体として、内容が明確化され、重要な情報が追加されています。特に、APIのバージョンとそのサポートの状態、ならびに引退日が新しいテーブル形式でまとめられました。2024年11月30日にリリースされるv4.0を使用することを推奨し、既存のワークロードを新しいバージョンに移行するための指針も強調されています。

具体的には、修正内容には以下の点が含まれています：
- ドキュメントの日付が2026年8月15日から2026年9月8日に更新されました。
- 新しいバージョンサポートに関するセクションが加わり、復旧日を含むAPIバージョンの状態が整理されました。
- 古いAPIバージョンに関する警告が削除され、情報が重複していた部分が整理されました。

これにより、読者はドキュメントインテリジェンスの最新のサポート状況と移行に関する情報を容易に把握できるようになっています。

## articles/ai-services/document-intelligence/service-limits.md{#item-5ceae5}

<details>
<summary>Diff</summary>
````diff
@@ -6,9 +6,10 @@ author: laujan
 manager: mcleans
 ms.service: azure-document-intelligence-foundry-tools
 ms.topic: limits-and-quotas
-ms.date: 04/30/2026
+ms.date: 09/08/2026
 ms.author: lajanuar
 monikerRange: '<=doc-intel-4.0.0'
+ai-usage: ai-assisted
 ---
 
 
@@ -106,6 +107,8 @@ Document Intelligence billing is calculated monthly based on the model type and
 | Adjustable | No | Yes <sup>2</sup> |
 | **List operations Per Second limit** | 1 | 10 (default value) |
 | Adjustable | No | Yes <sup>2</sup> |
+| **Maximum number of Document Intelligence resources per region** | 20 | 20 |
+| Adjustable | No | No |
 | **Max document size** | 4 MB | 500 MB |
 | Adjustable | No | No |
 | **Max number of pages (Analysis)** | 2 | 2000 |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスのサービス制限の更新"
}
```

### Explanation
この変更は、Azure Document Intelligenceのサービス制限に関する文書を更新したものです。主な変更点は、制限に関する情報に新しい項目が追加され、日付の更新が行われたことです。

具体的には、以下の内容が変更されています：
- ドキュメントの日付が2026年4月30日から2026年9月8日に更新されました。
- ドキュメントインテリジェンスリソースの最大数に関する新しい制限が追加され、地域ごとに最大20のリソースが定義されました。
- いくつかの制限が調整可能かどうかに関する情報が明確に追加されました。

これにより、ユーザーはサービス利用時の制限についての最新情報にアクセスでき、特にリソース管理をする上での重要なポイントが整理されました。


