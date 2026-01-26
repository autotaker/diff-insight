---
date: '2026-01-26'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b4721ba...MicrosoftDocs:2356f0d
summary: この変更は、Azure Language StudioからMicrosoft Foundryへの移行に関するドキュメントの更新を示しています。主な内容は、用語の一貫性を保つためのフレーズ調整や情報の明確化です。新しい情報が追加され、互換性を壊す変更はありません。また、用語の修正や段落の整理も行われています。このドキュメントは、Azure
  Language Studioが2026年2月16日にサービスを終了することを前提に、移行を行うユーザーに向けて、正確で分かりやすいガイダンスを提供することを目的としています。具体的には、移行準備のステップや手続きの詳細を説明しており、文書全体の読みやすさや情報の一貫性が向上しています。これにより、利用者は新機能や変更点を迅速に把握し、適切に対処することが可能となります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b4721ba...MicrosoftDocs:2356f0d){target="_blank"}

<format>
# ハイライト
この変更は、Azure Language StudioからMicrosoft Foundryへの移行に関するドキュメント内の更新です。特に、用語の一貫性を保つためのフレーズ調整や、情報の明確化を図った編集が行われています。

## 新機能
- 新しい情報の明記

## 互換性を壊す変更
- なし

## その他のアップデート
- 用語の修正および段落の整理

# 洞察
このドキュメントは、Azure Language Studioが2026年2月16日にサービスを終了することを前提としており、その後にMicrosoft Foundryへの移行が必要となるユーザーを対象にしています。更新の主な目的は、ユーザーがこの移行を可能な限りスムーズに進められるよう、正確かつ分かりやすいガイダンスを提供することです。

具体的には、移行準備のステップや必要な手続きについて詳細に説明されており、これによって新たな環境への移行後も継続して作業を行えるように支援しています。また、編集により文書全体の読みやすさや情報の一貫性が向上し、ユーザーの理解を助ける工夫がなされています。このような改善により、利用者は新機能や変更点を迅速に把握し、適切に対処できるようになります。</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [migration-studio-to-foundry.md](#item-12d575) | minor update | Microsoft Foundryへの移行に関する更新 | modified | 14 | 14 | 28 | 


# Modified Contents
## articles/ai-services/language-service/migration-studio-to-foundry.md{#item-12d575}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.date: 01/20/2026
 ms.author: lajanuar
 ---
 <!-- markdownlint-disable MD025 -->
-# Migrate from Azure Language Studio to Microsoft Foundry
+# Migrate from Language Studio to Microsoft Foundry
 
 Azure Language Studio retires on February 16, 2026. The service is no longer available after this date. All existing capabilities, along with new feature enhancements, are fully available in Microsoft Foundry. This guide provides step-by-step migration instructions to ensure uninterrupted access to Azure AI Language features and seamless project continuity within the Foundry environment.
 
@@ -36,13 +36,13 @@ The migration process consists of the following steps:
 
 > [!NOTE]
 >
-> * If you already have an Azure Language resource, you can continue to use your existing Language resources within the Microsoft Foundry portal **via a Foundry Hub** and **Foundry Hub project**. For more information, *see* [Which type of project do I need?](/azure/ai-foundry/what-is-foundry?view=foundry-classic&preserve-view=true#which-type-of-project-do-i-need).
+> * If you already have an Azure Language resource, you can continue to use your existing Language resources within the Microsoft Foundry portal via a **Foundry Hub** and **Hub project**. For more information, *see* [Which type of project do I need?](/azure/ai-foundry/what-is-foundry?view=foundry-classic&preserve-view=true#which-type-of-project-do-i-need).
 >
 > * If you plan to use a Foundry resource, you can create a new Foundry resource directly in the Microsoft Foundry portal when creating a new project. For more information, *see* [Create a Foundry project](/azure/ai-foundry/how-to/create-projects?view=foundry-classic&preserve-view=true&tabs=foundry).
 >
-> * In the Foundry, a **fine-tuning task** serves as your workspace when customizing your custom models. Previously, a **fine-tuning task** was referred to as a project. You might encounter both terms used interchangeably in older documentation.
+> * In the Foundry, a **fine-tuning task** serves as your workspace when customizing your custom models. Previously, a **fine-tuning task** was referred to as a project. You might encounter both terms used interchangeably in some documentation.
 
-Before you begin the migration process, ensure that the following resources and permissions are in place to complete the steps in this guide:
+**Before you begin the migration process, ensure that the following resources and permissions are in place to complete the steps in this guide:**
 
 * **Azure subscription**. If you don't have one, you can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
@@ -60,25 +60,25 @@ Before migrating to Microsoft Foundry, export all custom projects you want to tr
 1. Select the Azure Language resource containing the project you want to export.
 1. Navigate to **Custom Question Answering**.
 1. On the **Projects** page, select the project to export.
-1. Choose the export format (**Excel** or **TSV**). The file is exported as a `.zip` file containing your project contents.
+1. Choose the export format (**Excel** or **TSV**). The file is exported as a **`.zip`** file containing your project contents.
 
 ### Export a Conversational Language Understanding, Custom Named Entity Recognition, Custom Text Classification, or Orchestration Workflow project
 
 1. Sign in to [Language Studio](https://language.azure.com/).
 1. Select the Azure Language resource containing your CLU project.
-1. Navigate to your **Conversational Language Understanding** project.
+1. Navigate to your project.
 1. On the project home page, select your project from the right page ribbon area.
-1. Select **Download config file** to download the project as a `config.json` file.
+1. Select **Download config file** to download the project as a **`config.json`** file.
 
 ## Step 2: Set up your Foundry environment
 
-Before migrating your Azure AI Language projects to Microsoft Foundry, you need to complete several configuration tasks:
+Before migrating your Azure Language projects to Microsoft Foundry, you need to complete several configuration tasks:
 
 * **Configure Azure resources**. Create the required Foundry or Language resources in the Azure portal.
 * **Establish access control**. Assign the appropriate role-based access control (RBAC) permissions to your resources.
 * **Verify region availability**. Confirm that your target capabilities are supported in your chosen Azure region.
 
-The following sections outline the prerequisites and permissions for both custom model training (fine-tuning) and pretrained model access.
+The following sections outline the necessary prerequisites and permissions for both custom model training (fine-tuning) and pretrained model access.
 
 ### Custom model training (fine-tuning) in Microsoft Foundry
 
@@ -178,10 +178,10 @@ The following table lists the pretrained (prebuilt) capabilities available in Mi
 |**Text Analytics for health (Foundry classic)**|On the Playground tab, you can upload a file or type text directly into the sample window. A storage account isn't required. For more information, *see* [**Text Analytics for health in Foundry**](text-analytics-for-health/quickstart.md).|Available in all [supported Azure regions](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=cognitive-services).|
 
 > [!NOTE]
-> The following Azure AI Language features aren't available in the Microsoft Foundry portal. To use these capabilities, call the Azure AI Language REST API directly:
+> The following Azure AI Language features aren't available in the Microsoft Foundry portal. To use these capabilities, call the [**Azure Language REST API**](/rest/api/language/) directly:
 >
-> * **Custom Text Classification**. For regional availability, *see* [Region support for Custom Text Classification](concepts/regional-support.md).
-> * **Entity linking**. Available in all [supported Azure regions](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=cognitive-services).
+> * [**Custom Text Classification**](/azure/ai-services/language-service/custom-text-classification/quickstart?tabs=multi-classification). For regional availability, *see* [Region support for Custom Text Classification](concepts/regional-support.md).
+> * [**Entity linking**](/azure/ai-services/language-service/entity-linking/quickstart?tabs=windows&pivots=rest-api). Available in all [supported Azure regions](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=cognitive-services).
 
 ## Step 3: Import your projects into Foundry
 
@@ -222,7 +222,7 @@ After adding your source files, you can train and deploy the `CQA` project using
 1. Drag and drop or browse to the `config.json` file you exported from Language Studio.
 1. Select **Create** to import the project.
 
-After importing, you can train and deploy the CLU project using the **Getting started** workflow in Foundry.
+After importing, you can train and deploy your `CLU` project using the **Getting started** workflow in Foundry.
 
 ### Import an Orchestration Workflow project
 
@@ -261,7 +261,7 @@ If you encounter issues connecting your Language resource to Foundry:
 If project import fails:
 
 * Verify the export file format matches the expected import format.
-* Check for any data corruption in the exported `.zip` file.
+* Check for any data corruption in the exported `.zip` or `config,json` file.
 * Ensure the project name doesn't conflict with existing projects.
 
 ## Related content
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Microsoft Foundryへの移行に関する更新"
}
```

### Explanation
この変更は、Azure Language StudioからMicrosoft Foundryへの移行に関するドキュメントの更新です。文書におけるいくつかの文言を修正し、情報を明確にするための編集が行われました。特に、用語の一貫性や読みやすさを向上させるために、特定のフレーズが調整されています。具体的な変更点には、用語の修正、新しい情報の明記、及び段落の整理が含まれています。

このドキュメントは、Azure Language Studioが2026年2月16日にサービスを終了することに伴い、ユーザーがスムーズにMicrosoft Foundryに移行できるように設計されています。移行の手順や必要な準備についても詳細に説明されており、ユーザーが新しい環境での作業を続けられるように支援しています。全体として、変更は情報の正確性と利便性を高めることを目的としています。


