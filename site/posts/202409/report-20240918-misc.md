---
date: '2024-09-18'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:135d681...MicrosoftDocs:78943fc
summary: 今回の変更は、Azure AI Studioのクォータ管理機能に関するドキュメントの大幅な更新です。新しいスクリーンショットや具体的な手順が追加され、ユーザーの理解と操作が容易になります。特に、モデルクォータとVMクォータの管理に関する情報が強化され、視覚的に示されることで、初心者や不慣れなユーザーにも利用しやすくなっています。この変更により、Azure
  AI Studioのユーザー体験が向上し、操作も直感的に行えるようになっています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:135d681...MicrosoftDocs:78943fc){target="_blank"}

# ハイライト
今回の変更は、Azure AI Studioのクォータ管理機能に関する包括的なドキュメント更新です。既存のコンテンツに対する改善点や新しい機能の説明、具体的な手順などが追加され、ユーザー体験の向上が図られています。

## 新機能
- モデルクォータに関する新しいスクリーンショットの追加
- VMクォータに関する新しいスクリーンショットの追加
- モデルおよびVMクォータ選択のプロセスを示すスクリーンショットの追加

## 重大な変更
特に重大な変更点はありませんが、クォータ管理に関する情報が詳細にわたり強化されています。

## その他の更新
- モデルクォータおよびVMクォータの管理手順についての具体的なガイドラインの追加
- インタラクティブなチャートの使用方法と詳細フィルタリング方法についての説明

# 洞察
Azure AI Studioのクォータ管理に関するドキュメントが大幅に改善されました。これによりユーザーは、必要な操作情報をより簡単に理解し、実行できるようになるでしょう。具体的には、ユーザーはスクリーンショットを参照しながら、モデルクォータおよびVMクォータの管理操作を視覚的に理解できるようになりました。

### クォータ管理機能の強化
- **背景**: クォータ管理は、リソース利用の最適化と効率化を図るために不可欠な機能です。従来、クォータの設定や確認方法が不明瞭なことが問題として挙げられていました。
- **目的**: 今回の更新で、ユーザーが各種クォータ設定に関連する操作手順を理解しやすくするため、具体的かつ視覚的な情報が追加されました。
- **影響**: 具体的な画像やステップバイステップの説明が追加されたため、ユーザーは操作方法の理解に迷うことなく、クォータ管理を効率よく行えるようになりました。

新たに追加されたスクリーンショットや具体的なガイドラインは、初心者やクォータ管理に不慣れなユーザーにとって特に有益です。これにより、Azure AI Studioの利用体験が一層向上すると期待されます。全体として、この変更はユーザーサポートを強化し、より直感的な操作を可能にする重要なステップです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [quota.md](#item-39c866) | minor update | クォータ管理機能の強化 | modified | 16 | 4 | 20 | 
| [model-quota.png](#item-d9eb98) | new feature | モデルクォータのスクリーンショットの追加 | added | 0 | 0 | 0 | 
| [select-model-vm-quota.png](#item-476b34) | new feature | モデルおよびVMクォータ選択のスクリーンショットの追加 | added | 0 | 0 | 0 | 
| [vm-quota.png](#item-34af5c) | new feature | VMクォータのスクリーンショットの追加 | added | 0 | 0 | 0 | 


# Modified Contents
## articles/ai-studio/how-to/quota.md{#item-39c866}

<details>
<summary>Diff</summary>
````diff
@@ -93,13 +93,25 @@ Azure Storage has a limit of 250 storage accounts per region, per subscription.
 
 Use quotas to manage compute target allocation between multiple Azure AI Studio hubs in the same subscription. 
 
-By default, all hubs share the same quota as the subscription-level quota for VM families. However, you can set a maximum quota for individual VM families for more granular cost control and governance on hubs in a subscription. Quotas for individual VM families let you share capacity and avoid resource contention issues. 
+By default, all hubs share the same quota as the subscription-level quota for VM families. However, you can set a maximum quota for individual VM families for more granular cost control and governance on hubs in a subscription. Quotas for individual VM families let you share capacity and avoid resource contention issues.
 
-1. In Azure AI Studio, go to the **Home** page and select **Quota**. 
+1. In Azure AI Studio, go to the **Home** page and select either **Model quota** or **VM quota** from the **Management** section.
 
-1. Select the **Azure ML** tab to view the quota for the VM families. The quota is displayed at the subscription level in the selected Azure region. To request more quota, select the VM family and then select **Request quota**. 
+    :::image type="content" source="../media/cost-management/select-model-vm-quota.png" alt-text="Screenshot of the Model and VM quota entries in the management section." lightbox="../media/cost-management/select-model-vm-quota.png":::
 
-    :::image type="content" source="../media/cost-management/quota-manage.png" alt-text="Screenshot of the page to view and request quota for VM families in Azure AI Studio." lightbox="../media/cost-management/quota-manage.png":::
+1. When you select **Model quota**, you can view the quota for the models in the selected Azure region. To request more quota, select the model and then select **Request quota**. 
+
+    - Use the **Show all quota** toggle to display all quota or only the currently allocated quota.
+    - Use the **Group by** dropdown to group the list by **Quota type, Region & Model**, **Quota type, Model & Region**, or **None**. The **None** grouping displays a list of model deployments.
+    - Expand the groupings to view information on specific model deployments. While viewing a model deployment, select the **pencil icon** in the **Quota allocation** column to edit the quota allocation for the model deployment.
+    - Use the **charts** along the side of the page to view more details about quota usage. The charts are interactive; hovering over a section of the chart displays more information, and selecting the chart filters the list of models. Selecting the chart legend filters the data displayed in the chart.
+    - Use the **Azure OpenAI Provisioned** link to view information about provisioned models, including a **Capacity calculator**.
+  
+    :::image type="content" source="../media/cost-management/model-quota.png" alt-text="Screenshot of the Model quota page in Azure AI Studio." lightbox="../media/cost-management/model-quota.png":::
+
+1. When you select **VM quota**, you can view the quota and usage for the virtual machine families in the selected Azure region. To request more quota, select the VM family and then select **Request quota**. 
+
+    :::image type="content" source="../media/cost-management/vm-quota.png" alt-text="Screenshot of the VM quota page in Azure AI Studio." lightbox="../media/cost-management/vm-quota.png":::
 
 ## Next steps 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クォータ管理機能の強化"
}
```

### Explanation
このコードの変更は、Azure AI Studioにおけるクォータ管理に関する情報を更新したものです。主に、クォータの表示方法や利用方法のステップに関して具体的な手順を追加しました。具体的には、ユーザーが「モデルクォータ」と「VMクォータ」を選択する方法を明確にし、それに伴う新しいオプションを示すために、画像も挿入されています。

変更内容の詳細としては、以下の点が含まれます：

- **モデルクォータ**に関する情報が強化され、ユーザーがどのようにモデルのクォータを表示し、リクエストできるかが明示されています。
- **VMクォータ**についても同様に、仮想マシンファミリーの使用状況を把握し、さらにクォータをリクエストするための手順が追加されています。
- インタラクティブなチャートの使用方法や、クォータの詳細を絞り込む方法が説明されています。
- 画像を通じて、利用者が具体的にどのようにこれらの機能を使用するかを視覚的に理解できるようになっています。

全体として、クォータ管理に関するユーザビリティが向上し、利用者が必要な情報をより簡単に見つけられるように改善されています。

## articles/ai-studio/media/cost-management/model-quota.png{#item-d9eb98}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "モデルクォータのスクリーンショットの追加"
}
```

### Explanation
このコードの変更は、Azure AI Studioに関するドキュメントにモデルクォータの関連画像（スクリーンショット）を新たに追加したものです。この画像は、クォータ管理機能に関する情報を視覚的に補完するために使用され、ユーザーがモデルのクォータを確認する際の理解を助けます。

具体的には、以下のような点が考慮されています：

- **新しい画像の導入**: この変更により、ユーザーはモデルクォータの管理に関連するプロセスを視覚的に把握できるようになります。具体的な画面が示されることにより、手順がより明確になります。
- **ユーザビリティの向上**: ビジュアルコンテンツの追加は、情報の消化を容易にし、ユーザーが必要な操作を直感的に理解できることを目的としています。

ユーザーが効果的にAzure AI Studioの機能を利用できるようにするための重要な手助けとなる変更です。

## articles/ai-studio/media/cost-management/select-model-vm-quota.png{#item-476b34}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "モデルおよびVMクォータ選択のスクリーンショットの追加"
}
```

### Explanation
このコードの変更は、Azure AI Studioに関連するドキュメントに新しいスクリーンショットを追加したものです。この画像は、ユーザーがモデルとVMのクォータを選択するプロセスを視覚的に理解するためのもので、特にクォータ管理における操作を強化します。

具体的な変更内容は以下の通りです：

- **新しい画像の追加**: この変更により、ユーザーは「モデルクォータ」と「VMクォータ」を選択する際のインターフェースを直感的に理解できるようになります。具体的なスクリーンショットが提供されることで、手順が明確になり、ユーザーの混乱を軽減します。
- **視覚的な補足**: スクリーンショットは、クォータ選択の各ステップを視覚的に示すことによって、テキストのみでは伝わりにくい情報を補完します。これにより、ドキュメントの使いやすさが向上し、ユーザーが必要な情報を迅速に見つける手助けとなります。

全体として、この変更はAzure AI Studioのクォータ管理機能に関する理解を深め、ユーザー体験を向上させることを目的としています。

## articles/ai-studio/media/cost-management/vm-quota.png{#item-34af5c}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "VMクォータのスクリーンショットの追加"
}
```

### Explanation
このコードの変更は、Azure AI Studioに関するドキュメントに新たにVMクォータに関するスクリーンショットを追加したものです。この画像は、ユーザーがVMのクォータ管理を行う際の理解を深めるための重要なビジュアル資料です。

具体的には、以下の要点が挙げられます：

- **新しいビジュアルコンテンツの追加**: この変更により、ユーザーはVMクォータに関する設定や情報を視覚的に確認できるようになります。画像提供により、操作手順やインターフェースが明確になります。
- **ユーザーエクスペリエンスの向上**: スクリーンショットが追加されることによって、テキストだけでは伝わりにくかった情報を補完します。これにより、ユーザーが必要な操作を直感的に理解しやすくなります。

全体として、この変更はAzure AI StudioのVMクォータ管理に関するユーザーの理解を深め、実際の操作を円滑に進める手助けとなることを目的としています。


