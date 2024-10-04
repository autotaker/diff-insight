---
date: '2024-10-04'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:94dabc3...MicrosoftDocs:7d913a4
summary: Azure AI Studioのドキュメントが更新され、モデルクォータやVMクォータに関する新しいスクリーンショットが追加されました。特に破壊的な変更はなく、情報の追加と改善が行われました。クォータ管理に関する手順と表示が更新され、より明確になり、視覚的な要素が加わることでユーザーの理解が深まります。また、この変更はユーザー体験の向上に寄与し、新規ユーザーや技術的なバックグラウンドを持たないユーザーにとっても有益です。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:94dabc3...MicrosoftDocs:7d913a4){target="_blank"}

# Highlights

## New features
- Azure AI Studioのドキュメントにおいて、モデルクォータやVMクォータのスクリーンショットが新たに追加されました。

## Breaking changes
- 特に破壊的な変更はなく、主に情報の追加と改善が行われました。

## Other updates
- クォータ管理に関する手順と表示が更新され、より明確になりました。具体的には、新たなスクリーンショットが追加され、クォータの表示方法とグループ化機能の説明が強化されました。

# Insights

Azure AI Studioのドキュメントが本更新により、クォータ管理におけるユーザー体験を大幅に向上させることを目指しています。これまでテキスト中心であったクォータ管理の手順に視覚的な要素が加わることで、ユーザーは情報に対する理解を深めることができ、操作の流れを直感的に把握できるようになりました。特に、「モデルクォータ」「VMクォータ」「モデルおよびVMクォータ選択」のスクリーンショットの追加により、ユーザーは具体的な設定画面を参照しながら操作を進めることが可能となります。

この変更は、ドキュメント変更としては小規模に見えるかもしれませんが、実際のユーザー体験には大きな影響を与える可能性があります。視覚的な情報が加わることで、テキストを読み解く負担が軽減され、よりスムーズな操作体験につながります。また、新たに追加されたスクリーンショットは、今後の変更や新機能の実装におけるドキュメント更新の際の基盤にもなるでしょう。

このようなドキュメントの更新は、特に新規ユーザーや技術的なバックグラウンドを持たないユーザーにとって大変有益であり、Azure AI Studioの利用促進にも寄与する重要な要素となります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [quota.md](#item-39c866) | minor update | クォータ管理機能の改善 | modified | 16 | 4 | 20 | 
| [model-quota.png](#item-d9eb98) | new feature | モデルクォータのスクリーンショット追加 | added | 0 | 0 | 0 | 
| [select-model-vm-quota.png](#item-476b34) | new feature | モデルおよびVMクォータ選択のスクリーンショット追加 | added | 0 | 0 | 0 | 
| [vm-quota.png](#item-34af5c) | new feature | VMクォータのスクリーンショット追加 | added | 0 | 0 | 0 | 


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
    "modification_title": "クォータ管理機能の改善"
}
```

### Explanation
この変更は、Azure AI Studioのドキュメントにおけるクォータ管理に関する手順を更新した内容です。具体的には、VMおよびモデルクォータの表示方法を明確にし、新たにスクリーンショットを追加しています。また、クォータの表示オプションやグルーピング機能の説明も強化されました。これにより、ユーザーがクォータを管理する際の理解が深まり、操作が容易になることを目的としています。全体として、文書において16行が追加され、4行が削除され、変更は20行に冒頭されています。

## articles/ai-studio/media/cost-management/model-quota.png{#item-d9eb98}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "モデルクォータのスクリーンショット追加"
}
```

### Explanation
この変更では、Azure AI Studioに関するドキュメントに新たにモデルクォータのスクリーンショットが追加されました。この画像は、ユーザーがモデルクォータを確認・管理する際に役立つ視覚的なサポートを提供します。具体的なコードの変更は行われていませんが、この画像の追加により情報が強化され、ユーザーの理解を助けることを目的としています。画像は、ユーザーが関連情報を視覚的に参照できるため、実際の操作を行う際の利便性が向上します。

## articles/ai-studio/media/cost-management/select-model-vm-quota.png{#item-476b34}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "モデルおよびVMクォータ選択のスクリーンショット追加"
}
```

### Explanation
この変更では、Azure AI Studioのドキュメントにおいて、新たにモデルおよびVMクォータを選択するためのスクリーンショットが追加されました。この画像は、ユーザーがクォータ設定を理解しやすくするための視覚的なガイドとして機能します。具体的なコードの変更はなく、追加された画像によって情報が充実し、ユーザーがどのようにしてモデルとVMクォータを選択するかを明確に示すことが目的です。これにより、ユーザーは操作手順をより簡単に理解できるようになります。

## articles/ai-studio/media/cost-management/vm-quota.png{#item-34af5c}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "VMクォータのスクリーンショット追加"
}
```

### Explanation
この変更では、Azure AI Studioにおけるコスト管理のドキュメントに新たにVMクォータのスクリーンショットが追加されました。この画像は、仮想マシンのクォータ状況を視覚的に示すもので、ユーザーがクォータを確認し、管理する際に役立つ情報を提供します。具体的には、コードの変更はありませんが、追加されたスクリーンショットにより、ユーザーは仮想マシンのクォータを把握しやすくなり、操作上の理解を深めることができます。これにより、ドキュメント全体の情報が強化され、ユーザーにとっての利便性が向上します。


