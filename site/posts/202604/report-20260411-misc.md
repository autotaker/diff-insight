---
date: '2026-04-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a8bf7fb...MicrosoftDocs:1d705b3
summary: このコード修正では、Azure Document IntelligenceおよびLanguage Serviceに関する文書が更新され、特に新たに既知の問題に関するドキュメントが追加されました。目次が更新され、カスタムニューラルモデルに関する情報が明確化され、過去の価格設定やLUISサービスの退役に関する情報が修正されました。これにより、ユーザーは特定の問題に迅速に対応できるリソースを得ることができ、必要な情報に即座にアクセスできるようになります。全体として、ユーザーエクスペリエンスの向上と情報の透明性が図られています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a8bf7fb...MicrosoftDocs:1d705b3){target="_blank"}

<format>
# ハイライト
このコード修正では、Azure Document IntelligenceおよびLanguage Serviceに関するいくつかの文書が更新されました。主な新機能としては、Azure Document Intelligenceの既知の問題に関するドキュメントが新しく追加されました。その他には、目次の更新、カスタムニューラルモデルドキュメントの明確化、および過去の価格設定やルイス（LUIS）サービスについての情報がより正確に修正されています。

## 新機能
- Azure Document Intelligenceには、新しく既知の問題とそのトラブルシューティングに関するドキュメントが追加されました。これにより、ユーザーは特定の問題に迅速に対応できるようになります。

## 破壊的変更
特に破壊的な変更はありません。ただし、LUISサービスの退役に関する情報が更新された点に注意が必要です。

## その他の更新
- Azure Document Intelligenceの目次に「既知の問題とトラブルシューティング」セクションが追加されました。
- カスタムニューラルモデルのトレーニングに関する文書の文言が修正され、情報がより明確になりました。
- Language Serviceの過去の価格設定とLUISサービスの退役に関する文書の表現が修正され、タイムリーで正確な情報が提供されるようになりました。

# 洞察
このコード修正は、AzureのAIサービスを利用するユーザーに対して、より明確で正確な情報を提供することを目的としています。特に、Azure Document Intelligenceの新しい既知の問題ドキュメントは、ユーザーが直面する可能性のある問題を迅速に特定し、効率的に解決するための資源です。目次の更新により、ユーザーは必要な情報に即座にアクセスできるようになり、時間の節約が期待できます。

カスタムニューラルモデルおよび価格設定に関する文書の表現修正は、情報の透明性を高め、ユーザーの理解を助けるものです。また、LUISサービスの退役に関する具体的な日時の記載は、ユーザーに対して移行の緊急性を理解させ、代替サービスへの移行を計画させるための重要な情報です。

全体として、これらの修正はAzureサービスを利用する人々に対して、より良質なユーザーエクスペリエンスを提供し、将来の変更に備えるための文書として重要な改善を行っています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [known-issues.md](#item-2c1011) | new feature | Azure Document Intelligenceの既知の問題 | added | 40 | 0 | 40 | 
| [toc.yml](#item-81aa7b) | minor update | 目次に既知の問題とトラブルシューティングを追加 | modified | 2 | 0 | 2 | 
| [custom-neural.md](#item-ac0e69) | minor update | カスタムニューラルモデルのトレーニングに関する文言を修正 | modified | 1 | 1 | 2 | 
| [previous-updates.md](#item-af7f3f) | minor update | 価格設定階層の退役に関する文言を過去形に修正 | modified | 1 | 1 | 2 | 
| [migrate.md](#item-8a4128) | minor update | LUISサービスの退役に関する文言を修正 | modified | 1 | 2 | 3 | 


# Modified Contents
## articles/ai-services/document-intelligence/reference/known-issues.md{#item-2c1011}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,40 @@
+---
+title: Azure Document Intelligence in Foundry Tools known issues
+titlesuffix: Foundry Tools
+description: Known and common issues with Azure Document Intelligence in Foundry Tools.
+ai-usage: ai-assisted
+manager: nitinme
+ms.service: azure-ai-document-intelligence
+ms.topic: reference
+ms.date: 04/09/2026
+ms.author: lajanuar
+---
+<!-- markdownlint-disable MD025 -->
+# Azure Document Intelligence known issues and troubleshooting
+
+Azure Document Intelligence is updated continuously, and service changes can affect feature behavior and capability limits. This article tracks known issues in Azure Document Intelligence, describes their impact, and provides mitigation or resolution guidance. Before you submit a support request, review the list to determine whether your issue is a known condition and to identify the recommended remediation.
+
+## Service-level outages and notifications
+
+Azure status and Azure Service Health publish service-level outages and regional disruptions. Use these services to validate current impact, track incident lifecycle updates, and configure proactive notifications for your subscriptions and resources.
+
+* **Service-level outages**: [Azure status page](https://azure.status.microsoft/status).
+* **Outage notifications and alerts**: [Azure Service Health Portal](https://azure.microsoft.com/status/).
+
+## Current known issues
+
+The following table lists active, service-confirmed issues in Azure Document Intelligence. Each entry includes the issue category, observed behavior, documented workaround, and initial publish date.
+
+| Issue ID | Category | Title | Description | Workaround | Publication date |
+| --- | --- | --- | --- | --- | --- |
+| **1001** | File types | `Content Is Not Supported Error With Excel Files` | Excel files are documented as a supported input type. Requests can fail with **Content isn't supported** when file content exceeds an internal character limit. This condition usually occurs with large or densely populated spreadsheets. | **Excel files larger than *~8,000,000 characters* are rejected**.<br><br>**Option A:** Split large Excel files into smaller files and submit them separately.<br><br>**Option B:** Switch to Azure [Content Understanding](../../content-understanding/overview.md), which uses improved parser logic for these files. | April  2026 |
+ | **1002** | Encryption | `ServiceUnavailable error when using CMK` | Operations that rely on **Customer‑Managed Keys (CMK)** can intermittently fail with a **service unavailable** error. This failure occurs when the storage service uses stale cached identity or key material. | **Option A:** Refresh the `CMK` cache. Disable and re-enable `CMK`, assign a new key, or associate a new managed identity.<br><br>**Option B:** Switch to **Microsoft-Managed Keys (MMK)**: Navigate to your Document Intelligence resource in the [Azure portal](https://portal.azure.com/). **Resource Management** → **Encryption** -> **Microsoft Managed Keys**. | April  2026 |
+| **1003** | Model management | `Model Exists Error When Model Copy` | Copying a custom model can fail with a **Model Exists** error. This error occurs when a broken or partially created model remains on the target resource. Customers can't resolve this condition themselves. | No customer-side workaround is available.<br><br>Submit a [support request](mailto:formrecog_contact@microsoft.com) so the product group can remove the broken model from the backend. | April  2026 |
+| **1004** | Model training | `HTTP 500 – InternalServerError during model training (Neural or Template, Preview/GA APIs)` | Model training can fail with **HTTP 500 / InternalServerError**. This failure typically occurs when managed identity isn't configured correctly on the resource, especially in newer training flows. | Enable **Managed Identity** on your Document Intelligence resource.<br><br>Verify that the identity has the required permissions.<br><br>Follow the official [managed-identity configuration guidance](../authentication/managed-identities.md). | April  2026 |
+| **1005** | Model training | `Model training stuck in *Not started* status` | If a model training job fails before execution, the failed job may remain visible in the model list with status **Not started**. This state results from backend lifecycle handling, not customer configuration. | The backend automatically clears failed training jobs after approximately seven (7) days.<br><br>If earlier removal is required, submit an [Azure portal support request](https://ms.portal.azure.com/?quickstart=true#view/Microsoft_Azure_Support/HelpAndSupportBlade/~/overview). CSS or PG engineering can execute backend deletion of the orphaned training record. | April  2026 |
+
+## Related content
+
+* [Azure Service Health Portal](/azure/service-health/service-health-portal-update)
+* [Azure Status overview](/azure/service-health/azure-status-overview)
+* [What's new in Document Intelligence - Foundry Tools | Microsoft Learn](../whats-new.md)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure Document Intelligenceの既知の問題"
}
```

### Explanation
この修正では、Azure Document Intelligenceに関する新しいドキュメントが追加されました。この文書は、FoundryツールでのAzure Document Intelligenceの既知の問題やトラブルシューティング情報をまとめたものであり、特にユーザーにとって影響を与える可能性のある問題を特定し、それに対する解決策を提供します。

新しい文書セクションでは、以下の内容が含まれています：
- Azure Document Intelligenceのサービスレベルの停止や通知についての情報。
- 現在の既知の問題に関する詳細なテーブルがあり、各問題に対して観察された動作、文書化された回避策、および初回公開日が含まれています。

このように、ユーザーは問題が自分の環境に関連しているかどうかを簡単に確認し、推奨される修正手順を把握できるようになります。新しいドキュメントは、ユーザーにとって非常に有用なリソースとなり、 Azure Document Intelligenceの利用をよりスムーズにすることを目的としています。

## articles/ai-services/document-intelligence/toc.yml{#item-81aa7b}

<details>
<summary>Diff</summary>
````diff
@@ -367,6 +367,8 @@ items:
       href: https://go.microsoft.com/fwlink/?linkid=2087185
     - name: Compliance and certification
       href: https://azure.microsoft.com/support/legal/cognitive-services-compliance-and-privacy/
+  - name: Known issues and troubleshooting
+    href: reference/known-issues.md
   - name: Support and help options
     href: ../../ai-services/cognitive-services-support-options.md?context=/azure/ai-services/document-intelligence/context/context
   - name: Privacy and cookies
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次に既知の問題とトラブルシューティングを追加"
}
```

### Explanation
この修正は、Azure Document Intelligenceの目次ファイル（toc.yml）の更新に関するもので、2つの新しいエントリが追加されました。具体的には、「既知の問題とトラブルシューティング」という項目が追加され、それに関連する文書へのリンクも付与されています。

この変更により、ユーザーは文書の目次から直接「既知の問題とトラブルシューティング」セクションにアクセスできるようになり、問題の特定や解決策の確認が容易になります。これにより、ユーザーエクスペリエンスが向上し、必要な情報を迅速に得ることができるようになります。

## articles/ai-services/document-intelligence/train/custom-neural.md{#item-ac0e69}

<details>
<summary>Diff</summary>
````diff
@@ -112,7 +112,7 @@ To use overlapping fields, label your dataset with the overlaps and train the mo
 
 ## Supported regions
 
-As of October 18, 2022, Document Intelligence custom neural model training will only be available in the following Azure regions until further notice:
+As of October 18, 2022, Document Intelligence custom neural model training is only available in the following Azure regions:
 
 * Australia East
 * Brazil South
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムニューラルモデルのトレーニングに関する文言を修正"
}
```

### Explanation
この修正は、Azure Document Intelligenceのカスタムニューラルモデルのトレーニングに関するドキュメント内の言い回しを修正したものです。具体的には、「カスタムニューラルモデルのトレーニングは今後の通知まで特定のAzureリージョンでのみ利用可能」との文言が、「カスタムニューラルモデルのトレーニングは特定のAzureリージョンでのみ利用可能」という形に変更されました。

この変更により、情報の明確さが向上し、ユーザーが利用可能なリージョンに関する理解を深めることが期待されます。文言の修正は特に業務上の重要性を持たないものの、明確さを増すことでユーザー体験を向上させる目的があります。

## articles/ai-services/language-service/concepts/previous-updates.md{#item-af7f3f}

<details>
<summary>Diff</summary>
````diff
@@ -83,7 +83,7 @@ This article contains a list of previously recorded updates for Azure Language i
 * The `2021-01-15` model version for the `PII` feature, which provides:
   * Expanded support for nine new languages
   * Improved AI quality
-* The S0 through S4 pricing tiers are being retired on March 8, 2021.
+* The S0 through S4 pricing tiers were retired on March 8, 2021.
 * The language detection container is now generally available.
 
 ## January 2021
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "価格設定階層の退役に関する文言を過去形に修正"
}
```

### Explanation
この修正は、Azure Language Serviceにおける過去のアップデートを記録したドキュメント内の表現を修正したものです。「S0からS4の価格設定階層は2021年3月8日に退役する」という未来形の表現が、「S0からS4の価格設定階層は2021年3月8日に退役した」と過去形に変更されました。

この修正により、情報がより正確でタイムリーなものとなり、ユーザーがアップデートの履歴を正しく理解できるようになります。予定されていた変更が既に実施されたことが明確になり、利用者に対して適切な歴史的コンテキストが提供されます。

## articles/ai-services/language-service/reference/migrate.md{#item-8a4128}

<details>
<summary>Diff</summary>
````diff
@@ -16,8 +16,7 @@ On November 2, 2021, Azure Language in Foundry Tools was released into public pr
 
 > [!IMPORTANT]
 >
-> * You may experience intermittent interruptions when calling the Language Understanding (LUIS) service. Microsoft is in the final phase of retiring LUIS. These interruptions are temporary but expected during this retirement phase.
-> * Beginning March 31, 2026, LUIS runtime and authoring endpoints (including REST API calls) are fully retired, and all LUIS requests fail.
+> * As of March 31, 2026, LUIS runtime and authoring endpoints (including REST API calls) are fully retired, and all LUIS requests fail.
 > * To ensure uninterrupted operation, export all of your LUIS app data as soon as possible in order to:
 >   * Start using [Conversational Language Understanding (CLU)](../conversational-language-understanding/overview.md), or
 >   * Try out a [Microsoft Foundry](../conversational-language-understanding/quickstart.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "LUISサービスの退役に関する文言を修正"
}
```

### Explanation
この修正は、Azure Languageサービスの移行に関するドキュメント内の重要な情報を更新したものです。具体的には、LUIS（Language Understanding Intelligent Service）に関する部分の表現が変更されました。元々、「LUISサービスを呼び出す際に間欠的な中断が発生する可能性がある」との表現があったのが、「2026年3月31日以降、LUISのランタイムおよび作成エンドポイントが完全に退役し、すべてのLUISリクエストが失敗する」との過去形に修正されました。

この修正によって、ユーザーに対してLUISサービスの退役に関する期限が現実的に示され、対応する必要があることが強調されます。また、LUISからConversational Language Understanding (CLU)への移行を促す情報が引き続き提供されており、利用者の理解を助ける内容となっています。


