---
date: '2024-12-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d135a3a...MicrosoftDocs:e69b8c6
summary: Azure AI Foundryに関する記事と要約が更新されました。主な変更点は、用語の明確化と日付の更新です。新機能として、Azure AIサービスのリソース管理に関する具体的な指示が追加されましたが、既存のシステムへの直接的な影響を与えるような破壊的な変更はありません。他にも、「リソース」の表現が「Azure
  AIサービスリソース」に変更され、記事の日付が2024年5月21日から2024年12月9日に更新され、要約も新たに「AIアプリケーションとエージェントを安全に設計、カスタマイズ、管理する」という内容に改訂されました。このアップデートにより、ユーザーはより安全で効率的なAIの活用が可能になると期待されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d135a3a...MicrosoftDocs:e69b8c6){target="_blank"}

# ハイライト

Azure AI Foundryの記事と要約の更新が行われました。主な内容として、用語の明確化および日付の変更を含む記事の更新と、要約部分の表現の改訂が挙げられます。

## 新機能

この更新では、Azure AIサービスのリソース管理における新しい説明を含め、具体的な指示が追加されました。

## 破壊的変更

特に危険性や既存のシステムへの直接的な影響を与える変更は本更新には含まれていません。

## その他の更新

- 「リソース」の表現が「Azure AIサービスリソース」に変更されました。
- 記事の日付が2024年5月21日から2024年12月9日に更新されました。
- 文書の要約が「AIアプリケーションとエージェントを安全に設計、カスタマイズ、管理する」という新しい内容に変更されました。

# 洞察

今回のアップデートでは、Azure AIサービスの自動スケーリングに関する情報がより明確にされ、具体的な手順が詳細に説明されるようになりました。これにより、ユーザーはAzure AIの機能を最大限に活用できるようになります。加えて、日付の更新は使用される資料が最新であることを保証し、信頼性を向上させます。

もう一方で、文書の要約に関する変更では、単に市場競争を強調するのではなく、安全性とカスタマイズ性に焦点を当てた内容となっています。このことは、ユーザーに対してより高い安全性の確保と、個別ニーズに応じた使用方法の重要性を伝えるものです。

これらの変更は、Azure AI Foundryが目指す安全で効率的なAIソリューションの提供という目的をさらに強化するものとなっています。これらの更新を通じて、顧客への情報伝達およびサービスの利用効率が高まることが期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [autoscale.md](#item-ad23fa) | minor update | Auto-scaling Azure AIサービスの管理方法に関する更新 | modified | 4 | 6 | 10 | 
| [index.yml](#item-68b5b4) | minor update | Azure AI Foundry文書の要約更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-studio/how-to/autoscale.md{#item-ad23fa}

<details>
<summary>Diff</summary>
````diff
@@ -8,25 +8,23 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: how-to
-ms.date: 5/21/2024
+ms.date: 12/09/2024
 ms.reviewer: siarora
 ms.author: larryfr
 author: Blackmist
 ---
 
 # Autoscale Azure AI limits
 
-[!INCLUDE [feature-preview](../includes/feature-preview.md)]
-
-This article provides guidance for how you can manage and increase quotas for resources with Azure AI Foundry.
+This article provides guidance for how you can manage and increase quotas for Azure AI services resources with Azure AI Foundry.
 
 ## Overview
 
 Each Azure AI services resource has a preconfigured static call rate (transactions per second) which limits the number of concurrent calls that you can make to the backend service in a given time frame. The autoscale feature automatically increases or decreases your resource's rate limits based on near or real-time resource usage metrics and backend service capacity metrics.
 
 ## Get started with the autoscale feature
 
-This feature is disabled by default for every new resource. Follow these instructions to enable it.
+This feature is disabled by default for every new resource. To enable it, use the following information.
 
 #### [Azure portal](#tab/portal)
 
@@ -61,7 +59,7 @@ By default, Azure AI services resources have a default rate limit of 10 TPS. If
 
 ### Does autoscale increase my Azure spend? 
 
-Azure AI services pricing hasn't changed and can be accessed [here](https://azure.microsoft.com/pricing/details/cognitive-services/). We'll only bill for successful calls made to Azure AI services APIs. However, increased call rate limits mean more transactions are completed, and you might receive a higher bill.
+Azure AI services pricing hasn't changed and can be viewed from the [pricing page](https://azure.microsoft.com/pricing/details/cognitive-services/). We'll only bill for successful calls made to Azure AI services APIs. However, increased call rate limits mean more transactions are completed, and you might receive a higher bill.
 
 Be aware of potential errors and their consequences. If a bug in your client application causes it to call the service hundreds of times per second, that would likely lead to a higher bill, whereas the cost would be much more limited under a fixed rate limit. Errors of this kind are your responsibility. We highly recommend that you perform development and client update tests against a resource with a fixed rate limit prior to using the autoscale feature.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Auto-scaling Azure AIサービスの管理方法に関する更新"
}
```

### Explanation
この変更は、Azure AI Foundryにおける自動スケーリング機能の管理に関する記事を更新するものです。主な変更点として、文言の明確化と日付の更新が含まれています。具体的には、「リソース」を「Azure AIサービスリソース」という表現に修正し、日付を2024年5月21日から2024年12月9日に変更しました。また、いくつかの説明文が改善され、特に新しいリソースを有効にするための指示が明確にされました。この記事は、Azure AIサービスの割合制限や自動スケーリング機能に関する重要な情報を提供しています。

## articles/ai-studio/index.yml{#item-68b5b4}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ### YamlMime:Landing
 
 title: Azure AI Foundry documentation # < 60 chars
-summary:  Build cutting-edge, market-ready, responsible applications for your organization with AI.
+summary:  Safely design, customize, and manage AI applications and agents at scale.
 metadata:
   title: Azure AI Foundry documentation
   description: Azure AI Foundry helps developers and organizations rapidly create intelligent, cutting-edge, market-ready, and responsible applications with out-of-the-box and pre-built and customizable APIs and models. Example applications include generative AI, natural language processing for conversations, search, monitoring, translation, speech, vision, and decision-making.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundry文書の要約更新"
}
```

### Explanation
この変更は、Azure AI Foundryに関する文書の要約部分を更新することを目的としています。具体的には、元の要約から「最先端で市場に出る責任あるアプリケーションを構築する」という文言を、「AIアプリケーションとエージェントを安全に設計、カスタマイズ、管理する」という新しい内容に変更しました。この修正は、利用者に対してより具体的で安全性に配慮したアプローチを強調するものであり、文書のタイトルや説明内容はそのまま維持されています。この更新により、読者はAzure AI Foundryが提供する機能と目的についてより明確に理解できるようになります。


